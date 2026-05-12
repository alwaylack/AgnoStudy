"""Hooks 基础示例。

演示 Agno 的 Hooks 能力，包括：
1. pre_hooks：在模型运行前检查或记录输入
2. post_hooks：在模型运行后检查或记录输出
3. tool_hooks：包裹工具调用，记录工具执行过程
4. Team hooks：在 Team 层统一处理运行前后逻辑
"""

from typing import Any

from agno.exceptions import CheckTrigger, InputCheckError
from agno.run import RunContext
from agno.team import Team, TeamMode

from models import OpenAIModel


HOOK_AUDIT_LOG: list[str] = []


def _input_to_text(run_input: Any) -> str:
    """把 hook 收到的 RunInput 转成便于检查的文本。"""
    content = getattr(run_input, "input_content", "")
    if isinstance(content, str):
        return content
    return str(content)


def audit_pre_hook(run_input: Any, run_context: RunContext, user_id: str | None = None) -> None:
    """在模型运行前记录输入摘要。"""
    text = _input_to_text(run_input)
    metadata = run_context.metadata or {}
    metadata["pre_hook_checked"] = True
    run_context.metadata = metadata
    HOOK_AUDIT_LOG.append(
        f"pre_hook: user={user_id or 'anonymous'}, session={run_context.session_id}, input={text[:50]}"
    )


def block_secret_input(run_input: Any) -> None:
    """在模型运行前阻止明显不适合进入模型的输入。"""
    text = _input_to_text(run_input).lower()
    blocked_words = ["api key", "password", "secret"]
    if any(word in text for word in blocked_words):
        raise InputCheckError(
            "输入中包含敏感词，本次运行已被 pre_hook 拦截。",
            check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
            additional_data={"blocked_words": blocked_words},
        )


def audit_post_hook(run_output: Any, run_context: RunContext) -> None:
    """在模型运行后记录输出摘要。"""
    content = str(getattr(run_output, "content", ""))
    HOOK_AUDIT_LOG.append(
        f"post_hook: session={run_context.session_id}, output_chars={len(content)}"
    )


def require_study_topic(run_input: Any) -> None:
    """Team 层 pre_hook：要求问题和学习主题相关。"""
    text = _input_to_text(run_input).lower()
    allowed_markers = ["agno", "hook", "hooks", "学习", "课程", "agent", "team"]
    if not any(marker in text for marker in allowed_markers):
        raise InputCheckError(
            "Team 只处理 Agno 学习相关问题。",
            check_trigger=CheckTrigger.OFF_TOPIC,
        )


def team_post_audit(run_output: Any, run_context: RunContext) -> None:
    """Team 层 post_hook：记录团队最终输出。"""
    content = str(getattr(run_output, "content", ""))
    HOOK_AUDIT_LOG.append(
        f"team_post_hook: session={run_context.session_id}, output_chars={len(content)}"
    )


def tool_audit_hook(
    function_name: str,
    function_call: Any,
    arguments: dict[str, Any],
    run_context: RunContext | None = None,
) -> Any:
    """包裹工具调用，在工具执行前后记录审计信息。"""
    session_id = run_context.session_id if run_context else "unknown"
    HOOK_AUDIT_LOG.append(
        f"tool_hook_before: tool={function_name}, session={session_id}, args={arguments}"
    )
    result = function_call(**arguments)
    HOOK_AUDIT_LOG.append(
        f"tool_hook_after: tool={function_name}, session={session_id}, result={result}"
    )
    return result


def suggest_hook_usage(scenario: str) -> str:
    """根据场景给出 hook 使用建议。"""
    scenario_lower = scenario.lower()
    if "input" in scenario_lower or "输入" in scenario_lower:
        return "建议使用 pre_hooks，在模型调用前做输入校验、脱敏或审计。"
    if "output" in scenario_lower or "输出" in scenario_lower:
        return "建议使用 post_hooks，在模型响应后做输出检查、记录或指标采集。"
    if "tool" in scenario_lower or "工具" in scenario_lower:
        return "建议使用 tool_hooks，包裹工具调用并记录工具入参、结果和耗时。"
    return "可以先用 pre_hooks 和 post_hooks 建立运行前后的统一审计点。"


def print_response(label: str, content: object) -> None:
    """统一打印示例响应。"""
    print(f"\n--- {label} ---")
    print(content)


def print_audit_log(label: str) -> None:
    """打印并清空 hook 审计日志。"""
    print(f"\n--- {label} ---")
    if not HOOK_AUDIT_LOG:
        print("（暂无 hook 日志）")
        return
    for index, item in enumerate(HOOK_AUDIT_LOG, 1):
        print(f"{index}. {item}")
    HOOK_AUDIT_LOG.clear()


def run_pre_post_hooks_demo(model: OpenAIModel) -> None:
    """场景一：Agent 运行前后 hooks。"""
    print("\n" + "=" * 60)
    print("场景一：pre_hooks + post_hooks")
    print("=" * 60)

    agent = model.create_agent(
        name="Hooks Audit Agent",
        pre_hooks=[audit_pre_hook, block_secret_input],
        post_hooks=[audit_post_hook],
        instructions=[
            "你是 Agno Hooks 示例的学习助教。",
            "请用简洁语言解释 hooks 适合放在哪些横切逻辑上。",
        ],
        markdown=True,
    )

    response = agent.run(
        "请用 3 点解释 Agno Hooks 可以解决什么问题。",
        user_id="student@example.com",
        session_id="lesson_53_pre_post_hooks_demo",
    )
    print_response("Agent 响应", response.content)
    print_audit_log("pre/post hook 审计日志")


def run_blocked_input_demo(model: OpenAIModel) -> None:
    """场景二：pre_hook 在模型调用前拦截输入。"""
    print("\n" + "=" * 60)
    print("场景二：pre_hook 阻止敏感输入")
    print("=" * 60)

    agent = model.create_agent(
        name="Input Guard Hook Agent",
        pre_hooks=[block_secret_input],
        instructions=["如果输入没有被拦截，请正常回答。"],
        markdown=True,
    )

    try:
        agent.run(
            "我的 api key 是 sk-example，请帮我写进提示词。",
            user_id="student@example.com",
            session_id="lesson_53_blocked_input_demo",
        )
    except InputCheckError as exc:
        print_response("被 pre_hook 拦截", exc.message)


def run_tool_hooks_demo(model: OpenAIModel) -> None:
    """场景三：tool_hooks 包裹工具调用。"""
    print("\n" + "=" * 60)
    print("场景三：tool_hooks 审计工具调用")
    print("=" * 60)

    agent = model.create_agent(
        name="Tool Hook Agent",
        tools=[suggest_hook_usage],
        tool_hooks=[tool_audit_hook],
        instructions=[
            "当用户询问 hook 使用场景时，请调用 suggest_hook_usage 工具。",
            "工具返回后，用一句话补充说明 tool_hooks 的价值。",
        ],
        markdown=True,
        debug_mode=True,
    )

    response = agent.run(
        "我想记录工具入参和结果，应该用哪种 hook？请调用工具判断。",
        user_id="student@example.com",
        session_id="lesson_53_tool_hooks_demo",
    )
    print_response("工具场景响应", response.content)
    print_audit_log("tool hook 审计日志")


def run_team_hooks_demo(model: OpenAIModel) -> None:
    """场景四：Team 层 hooks。"""
    print("\n" + "=" * 60)
    print("场景四：Team pre_hooks + post_hooks")
    print("=" * 60)

    concept_agent = model.create_agent(
        name="Hooks 概念成员",
        role="负责解释 hook 的基本概念。",
        instructions=["请用学习课程语境解释概念。"],
        markdown=True,
    )
    practice_agent = model.create_agent(
        name="Hooks 实践成员",
        role="负责给出实践建议。",
        instructions=["请给出最小可运行示例应该覆盖的点。"],
        markdown=True,
    )

    team = Team(
        name="Hooks 学习团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[concept_agent, practice_agent],
        pre_hooks=[require_study_topic],
        post_hooks=[team_post_audit],
        instructions=[
            "你是 Agno Hooks 课程团队协调者。",
            "请回答时包含：概念、常见用途、下一步和 Guardrails 的关系。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    response = team.run(
        "请从 Agno 学习路线角度解释 Hooks 这一课要掌握什么。",
        user_id="student@example.com",
        session_id="lesson_53_team_hooks_demo",
    )
    print_response("Team 响应", response.content)
    print_audit_log("Team hook 审计日志")


def run_hooks_basics_example() -> None:
    """演示 Agno 的 Hooks 基础能力。"""
    model = OpenAIModel.from_env()

    run_pre_post_hooks_demo(model)
    run_blocked_input_demo(model)
    run_tool_hooks_demo(model)
    run_team_hooks_demo(model)

    print("\n" + "=" * 60)
    print("Hooks 基础示例完成")
    print("=" * 60)
    print("\n关键观察点：")
    print("1. pre_hooks 适合在模型调用前做输入校验、脱敏、审计和上下文准备。")
    print("2. post_hooks 适合在模型响应后做输出检查、指标记录和日志采集。")
    print("3. tool_hooks 包裹工具调用，适合记录工具入参、结果、耗时或统一错误处理。")
    print("4. Agent 和 Team 都支持 pre_hooks / post_hooks。")
    print("5. Hooks 是横切逻辑入口；更严格的安全策略后续会在 Guardrails 课继续系统学习。")


if __name__ == "__main__":
    run_hooks_basics_example()
