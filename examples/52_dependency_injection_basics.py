"""Dependency Injection 基础示例。

演示 Agno 的依赖注入能力，包括：
1. 通过 dependencies 注入运行时业务上下文
2. 通过 callable dependency 动态生成上下文
3. 通过 add_dependencies_to_context 把依赖注入给模型
4. 在工具中通过 RunContext 读取依赖
5. 在 Team 中共享依赖
"""

from datetime import datetime

from agno.run import RunContext
from agno.team import Team, TeamMode

from models import OpenAIModel


def load_learning_snapshot(run_context: RunContext) -> dict[str, object]:
    """动态生成当前学习快照。"""
    return {
        "user_id": run_context.user_id or "anonymous",
        "completed_advanced_lessons": [
            "Context Management",
            "State Management",
            "Chat History",
        ],
        "current_lesson": "Dependency Injection",
        "recommended_next_lesson": "Hooks",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
    }


def build_learning_dependencies() -> dict[str, object]:
    """构建本节课会复用的一组依赖。"""
    return {
        "learner_profile": {
            "name": "Agno 学员",
            "preference": "喜欢用最小可运行示例理解概念",
            "current_track": "SDK Advanced 对齐线",
        },
        "course_plan": {
            "current": "Dependency Injection",
            "next": "Hooks",
            "later": ["Skills", "Reasoning", "Multimodal"],
        },
        "learning_snapshot": load_learning_snapshot,
    }


def inspect_injected_dependencies(run_context: RunContext) -> str:
    """读取本次运行注入的学习依赖，并返回关键信息。"""
    dependencies = run_context.dependencies or {}
    learner_profile = dependencies.get("learner_profile", {})
    course_plan = dependencies.get("course_plan", {})
    learning_snapshot = dependencies.get("learning_snapshot", {})

    return (
        "工具已读取到注入依赖："
        f"学习者={learner_profile.get('name', 'unknown')}；"
        f"当前课程={course_plan.get('current', 'unknown')}；"
        f"下一课={course_plan.get('next', 'unknown')}；"
        f"快照用户={learning_snapshot.get('user_id', 'unknown')}。"
    )


def print_response(label: str, content: object) -> None:
    """统一打印示例响应。"""
    print(f"\n--- {label} ---")
    print(content)


def run_agent_context_demo(model: OpenAIModel) -> None:
    """场景一：把 dependencies 注入到模型上下文中。"""
    print("\n" + "=" * 60)
    print("场景一：Agent 通过 add_dependencies_to_context 读取依赖")
    print("=" * 60)

    agent = model.create_agent(
        name="Dependency Context Agent",
        dependencies=build_learning_dependencies(),
        add_dependencies_to_context=True,
        instructions=[
            "你是 Agno Dependency Injection 示例的学习助教。",
            "请优先基于 additional context 中的依赖信息回答。",
            "回答时明确指出哪些信息来自 dependencies。",
        ],
        markdown=True,
    )

    response = agent.run(
        "请根据注入的学习上下文，用 4 句话说明我当前在学什么、为什么需要它、下一课是什么。",
        user_id="student@example.com",
        session_id="lesson_52_agent_context_demo",
    )
    print_response("Agent 响应", response.content)


def run_runtime_override_demo(model: OpenAIModel) -> None:
    """场景二：在单次 run 中覆盖 Agent 默认依赖。"""
    print("\n" + "=" * 60)
    print("场景二：运行时 dependencies 覆盖 Agent 默认配置")
    print("=" * 60)

    agent = model.create_agent(
        name="Dependency Override Agent",
        dependencies={
            "learner_profile": {
                "name": "默认学员",
                "preference": "默认学习偏好",
            },
            "course_plan": {
                "current": "Dependency Injection",
                "next": "Hooks",
            },
        },
        add_dependencies_to_context=True,
        instructions=[
            "你负责解释本次运行实际收到的 dependencies。",
            "如果上下文中出现学习者姓名和偏好，请直接引用它们。",
        ],
        markdown=True,
    )

    response = agent.run(
        "请说明这次运行实际注入了哪位学习者，以及他的学习偏好是什么。",
        user_id="student@example.com",
        session_id="lesson_52_runtime_override_demo",
        dependencies={
            "learner_profile": {
                "name": "运行时学员",
                "preference": "想先看业务场景，再看参数细节",
            },
            "course_plan": {
                "current": "Dependency Injection",
                "next": "Hooks",
            },
            "learning_snapshot": load_learning_snapshot,
        },
    )
    print_response("覆盖后的 Agent 响应", response.content)


def run_tool_context_demo(model: OpenAIModel) -> None:
    """场景三：工具函数通过 RunContext 读取依赖。"""
    print("\n" + "=" * 60)
    print("场景三：工具通过 RunContext 读取 dependencies")
    print("=" * 60)

    agent = model.create_agent(
        name="Dependency Tool Agent",
        dependencies=build_learning_dependencies(),
        add_dependencies_to_context=True,
        tools=[inspect_injected_dependencies],
        instructions=[
            "当用户要求检查依赖时，请调用 inspect_injected_dependencies 工具。",
            "工具返回后，请用一句话解释这说明 dependencies 不只是提示词文本，也能进入工具运行上下文。",
        ],
        markdown=True,
        debug_mode=True,
    )

    response = agent.run(
        "请调用工具检查本次运行注入了哪些学习依赖。",
        user_id="student@example.com",
        session_id="lesson_52_tool_context_demo",
    )
    print_response("工具场景响应", response.content)


def run_team_dependency_demo(model: OpenAIModel) -> None:
    """场景四：Team 也可以共享 dependencies。"""
    print("\n" + "=" * 60)
    print("场景四：Team 共享 dependencies")
    print("=" * 60)

    concept_agent = model.create_agent(
        name="依赖概念成员",
        role="负责解释 Dependency Injection 的概念。",
        instructions=[
            "请用最小示例视角解释概念。",
            "如果上下文里有学习偏好，请按偏好调整解释方式。",
        ],
        markdown=True,
    )
    planning_agent = model.create_agent(
        name="学习规划成员",
        role="负责根据课程计划给出下一步建议。",
        instructions=[
            "请根据注入的 course_plan 判断下一课。",
            "回答要简洁，聚焦学习路线。",
        ],
        markdown=True,
    )

    team = Team(
        name="Dependency Injection 学习团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[concept_agent, planning_agent],
        dependencies=build_learning_dependencies(),
        add_dependencies_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是学习团队协调者。",
            "请让成员基于 dependencies 中的学习者画像和课程计划回答。",
            "最终回答包含：概念解释、适用场景、下一课。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    response = team.run(
        "请结合我的学习偏好，解释 Dependency Injection 在 Agno 里解决什么问题，并告诉我下一课是什么。",
        user_id="student@example.com",
        session_id="lesson_52_team_dependency_demo",
    )
    print_response("Team 响应", response.content)


def run_dependency_injection_basics_example() -> None:
    """演示 Agno 的 Dependency Injection 基础能力。"""
    model = OpenAIModel.from_env()

    run_agent_context_demo(model)
    run_runtime_override_demo(model)
    run_tool_context_demo(model)
    run_team_dependency_demo(model)

    print("\n" + "=" * 60)
    print("Dependency Injection 基础示例完成")
    print("=" * 60)
    print("\n关键观察点：")
    print("1. dependencies 用来注入运行时业务上下文，不需要写死在用户问题里。")
    print("2. callable dependency 会在运行前被解析，适合读取最新配置、用户画像或外部状态。")
    print("3. add_dependencies_to_context=True 会把依赖作为 additional context 交给模型。")
    print("4. 工具函数可以通过 RunContext 读取同一份 dependencies。")
    print("5. Team 和 Agent 一样可以接收 dependencies。")


if __name__ == "__main__":
    run_dependency_injection_basics_example()
