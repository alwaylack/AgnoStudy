from agno.team import Team, TeamMode

from models import OpenAIModel


def run_team_broadcast_basics_example() -> None:
    """演示如何使用 TeamMode.broadcast 让多个成员同时评估同一个问题。"""
    model = OpenAIModel.from_env()

    opportunity_agent = model.create_agent(
        name="机会分析专家",
        role="负责评估问题中的机会和收益",
        instructions=[
            "你专注于分析机会、优势和潜在收益。",
            "请优先说明这件事值得做的原因。",
        ],
        markdown=True,
    )

    risk_agent = model.create_agent(
        name="风险分析专家",
        role="负责评估问题中的风险和潜在问题",
        instructions=[
            "你专注于分析风险、限制和潜在问题。",
            "请优先指出需要小心的地方。",
        ],
        markdown=True,
    )

    action_agent = model.create_agent(
        name="行动建议专家",
        role="负责给出可执行的下一步建议",
        instructions=[
            "你专注于把问题转化为可执行的建议。",
            "请优先给出清晰的小步行动方案。",
        ],
        markdown=True,
    )

    # broadcast 模式会把同一个问题同时交给所有成员，
    # 然后由 Team 统一汇总他们的观点。
    team = Team(
        name="Agno 广播协作团队",
        mode=TeamMode.broadcast,
        model=model.get_model(),
        members=[opportunity_agent, risk_agent, action_agent],
        instructions=[
            "你是团队协调者。",
            "请把同一个问题同时交给所有成员分析。",
            "最后把不同成员的观点汇总成一个清晰的结论。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "我已经学完 Team 的 coordinate 和 route。现在要不要马上进入 tasks 模式？请从机会、风险和行动建议三个角度一起分析。"
    )


if __name__ == "__main__":
    run_team_broadcast_basics_example()
