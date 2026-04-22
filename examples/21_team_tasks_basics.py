from agno.team import Team, TeamMode

from models import OpenAIModel


def run_team_tasks_basics_example() -> None:
    """演示如何使用 TeamMode.tasks 让团队自动拆解任务并执行。"""
    model = OpenAIModel.from_env()

    research_agent = model.create_agent(
        name="资料研究专家",
        role="负责梳理已有学习内容和相关知识点",
        instructions=[
            "你擅长整理资料和梳理上下文。",
            "请优先提取已经学过的内容和接下来相关的主题。",
        ],
        markdown=True,
    )

    planning_agent = model.create_agent(
        name="任务规划专家",
        role="负责把学习目标拆成清晰任务",
        instructions=[
            "你擅长把目标拆成小任务。",
            "请优先输出可执行、可验证的任务步骤。",
        ],
        markdown=True,
    )

    review_agent = model.create_agent(
        name="复盘审查专家",
        role="负责检查计划是否完整、是否适合当前学习阶段",
        instructions=[
            "你擅长检查方案是否完整。",
            "请优先指出遗漏点，并补充更稳妥的建议。",
        ],
        markdown=True,
    )

    # tasks 模式的重点是：Team 领导者自己拆任务、分配任务、跟踪执行并汇总结果。
    team = Team(
        name="Agno 任务执行团队",
        mode=TeamMode.tasks,
        model=model.get_model(),
        members=[research_agent, planning_agent, review_agent],
        instructions=[
            "你是任务型团队领导者。",
            "请先把用户目标拆成清晰任务，再分配给最合适的成员。",
            "请在完成所有任务后，再统一输出最终结果。",
            "如果某个步骤缺信息，请明确指出需要补充什么。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
        max_iterations=8,
    )

    team.print_response(
        "请为我制定一个接下来的 Agno 学习执行计划，要求覆盖 Team 学习线的后续内容，并确保顺序合理。"
    )


if __name__ == "__main__":
    run_team_tasks_basics_example()
