from agno.team import Team, TeamMode

from models import OpenAIModel


def run_team_route_basics_example() -> None:
    """演示如何使用 TeamMode.route 把问题路由给最合适的成员。"""
    model = OpenAIModel.from_env()

    beginner_agent = model.create_agent(
        name="初学者辅导专家",
        role="只负责回答适合 Agno 初学者的问题",
        instructions=[
            "你只回答适合初学者的问题。",
            "请优先给出简单、直接、低负担的建议。",
        ],
        markdown=True,
    )

    advanced_agent = model.create_agent(
        name="进阶实践专家",
        role="只负责回答 Agno 进阶实践和架构问题",
        instructions=[
            "你只回答进阶实践问题。",
            "请优先关注检索优化、架构设计和复杂协作。",
        ],
        markdown=True,
    )

    # route 模式的重点是：团队领导者只负责把请求路由给一个最合适的成员，
    # 然后直接返回该成员的回答，而不是再做综合整理。
    team = Team(
        name="Agno 路由团队",
        mode=TeamMode.route,
        model=model.get_model(),
        members=[beginner_agent, advanced_agent],
        instructions=[
            "你是团队路由器。",
            "请根据用户问题，把请求交给最合适的一个成员处理。",
            "不要综合多个成员结果，直接返回最合适成员的回答。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：路由到初学者专家 ---")
    team.print_response("我是初学者，刚学完 Agent 和 Tools，下一步最适合先学什么？")

    print("\n--- 示例 2：路由到进阶专家 ---")
    team.print_response("我已经学完基础课程，下一步更适合先优化 RAG，还是先设计多 Agent 架构？")


if __name__ == "__main__":
    run_team_route_basics_example()
