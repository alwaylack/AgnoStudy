from agno.team import Team, TeamMode
from agno.workflow import Step, Workflow

from models import OpenAIModel


def build_study_team(model_wrapper: OpenAIModel) -> Team:
    """构建一个专门用于学习规划的协作团队。"""
    concept_agent = model_wrapper.create_agent(
        name="概念讲解成员",
        role="负责解释当前阶段最重要的概念重点。",
        instructions=[
            "请根据用户当前进度，解释当前阶段最需要理解的核心概念。",
            "输出要清晰、简洁，方便后续步骤继续使用。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="课程规划成员",
        role="负责给出下一阶段学习安排。",
        instructions=[
            "请根据用户当前进度，给出下一阶段最值得优先学习的课程安排。",
            "输出要说明为什么这样安排。",
        ],
        markdown=True,
    )

    return Team(
        name="Workflow 学习协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, planning_agent],
        instructions=[
            "你是一个学习协作团队。",
            "请协调不同成员，从概念理解和课程安排两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def run_workflow_team_basics_example() -> None:
    """运行 Workflow + Team 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    kickoff_agent = model_wrapper.create_agent(
        name="流程启动员",
        role="负责识别当前学习请求的背景。",
        instructions=[
            "请先简要识别用户当前已经学到什么位置，以及这次请求的目标。",
            "输出尽量简洁，作为后续团队协作的上下文。",
        ],
        markdown=True,
    )

    summary_agent = model_wrapper.create_agent(
        name="流程总结员",
        role="负责整合 Team 的结果，给出最终学习建议。",
        instructions=[
            "你会收到前面 Workflow 和 Team 阶段的结果。",
            "请整合这些信息，给出最终下一课建议，并说明后续主线安排。",
        ],
        markdown=True,
    )

    study_team = build_study_team(model_wrapper)

    workflow = Workflow(
        name="Agno Workflow + Team 基础课",
        description="学习如何在 Workflow 中把某个阶段交给 Team 协作完成。",
        steps=[
            Step(
                name="流程启动分析",
                agent=kickoff_agent,
                description="先识别当前学习背景和本次请求目标。",
            ),
            Step(
                name="团队协作分析",
                team=study_team,
                description="把核心分析阶段交给 Team 协作完成。",
            ),
            Step(
                name="最终流程总结",
                agent=summary_agent,
                description="整合 Workflow 和 Team 阶段结果，生成最终建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop，"
            "以及多模式组合课。请用 Workflow + Team 的方式帮我安排下一阶段学习。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_team_basics_example()
