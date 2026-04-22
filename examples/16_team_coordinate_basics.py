from agno.team import Team, TeamMode

from models import OpenAIModel


def run_team_coordinate_basics_example() -> None:
    """演示如何使用 Team 组织多个 Agent 协作完成任务。"""
    model = OpenAIModel.from_env()

    concept_agent = model.create_agent(
        name="概念讲解专家",
        role="负责解释 Agno 概念和模块分工",
        instructions=[
            "你擅长把 Agno 的概念解释清楚。",
            "请尽量用初学者容易理解的方式说明问题。",
        ],
        markdown=True,
    )

    planning_agent = model.create_agent(
        name="学习规划专家",
        role="负责把学习目标拆成可执行步骤",
        instructions=[
            "你擅长把学习目标拆成清晰的步骤。",
            "请优先输出适合初学者执行的小步计划。",
        ],
        markdown=True,
    )

    # Team 负责协调多个成员 Agent，共同完成一个更复杂的问题。
    team = Team(
        name="Agno 学习协作团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[concept_agent, planning_agent],
        instructions=[
            "你是团队协调者。",
            "请先判断需要哪些成员参与，再综合成员结果给出最终回答。",
            "最终回答要同时包含概念说明和可执行建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "我刚学完 Knowledge 和 PDF Reader。请团队一起帮我解释 Team / Multi-Agent 的作用，并给我一个下一步学习建议。"
    )


if __name__ == "__main__":
    run_team_coordinate_basics_example()
