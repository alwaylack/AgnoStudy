from agno.team import Team, TeamMode

from models import OpenAIModel


def estimate_learning_load(topic: str, level: str) -> str:
    """根据主题和难度估算学习负担。"""
    load_map = {
        ("team", "basic"): "学习负担中等，适合已经掌握单 Agent 和基础 RAG 的阶段。",
        ("team", "advanced"): "学习负担较高，适合已经熟悉 Team 基本模式之后再进入。",
        ("rag", "advanced"): "学习负担较高，但对已有 Knowledge 基础的学习者很有帮助。",
    }
    return load_map.get(
        (topic.lower(), level.lower()),
        f"{topic} 的 {level} 阶段建议先从最小示例开始，逐步增加复杂度。",
    )


def recommend_next_step(current_stage: str) -> str:
    """根据当前阶段给出下一步学习建议。"""
    stage = current_stage.lower()
    if "team route" in stage or "team broadcast" in stage or "team tasks" in stage:
        return "下一步建议学习 Team 与 Knowledge / Tools 的组合方式，再进入更复杂的协作设计。"
    if "rag" in stage:
        return "下一步建议继续做 Team 协作，这样能把 Knowledge 和协作模式串起来。"
    return "建议继续沿着当前主线学习，并优先选择一个最小可运行示例。"


def run_team_shared_tools_example() -> None:
    """演示如何让多个 Team 成员围绕共享工具协作分析问题。"""
    model = OpenAIModel.from_env()

    analysis_agent = model.create_agent(
        name="负担评估专家",
        role="负责评估学习主题的难度和投入成本",
        tools=[estimate_learning_load],
        instructions=[
            "你擅长评估学习负担。",
            "当问题涉及难度和投入时，请优先调用工具。",
        ],
        markdown=True,
    )

    planning_agent = model.create_agent(
        name="路线建议专家",
        role="负责判断下一步更适合学什么",
        tools=[recommend_next_step],
        instructions=[
            "你擅长判断学习顺序。",
            "当问题涉及下一步安排时，请优先调用工具。",
        ],
        markdown=True,
    )

    # Team 共享成员工具的能力，让协调者更容易理解成员的可用能力边界。
    team = Team(
        name="Agno 共享工具团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[analysis_agent, planning_agent],
        add_member_tools_to_context=True,
        instructions=[
            "你是团队协调者。",
            "请协调成员使用他们各自的工具分析问题。",
            "最终答案需要同时包含难度判断和下一步建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "我已经学完 Team 的 coordinate、route、broadcast、tasks。现在继续学 Team + Knowledge 和 Team + Tools，学习负担如何？下一步最适合怎么安排？"
    )


if __name__ == "__main__":
    run_team_shared_tools_example()
