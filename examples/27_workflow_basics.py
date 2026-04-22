from agno.workflow import Step, StepOutput, Workflow

from models import OpenAIModel


def extract_stage_summary(step_input) -> StepOutput:
    """从前一个步骤输出里整理出更适合继续规划的阶段摘要。"""
    previous_content = step_input.previous_step_content or ""

    summary = (
        "当前学习阶段摘要：\n"
        f"{previous_content}\n\n"
        "请在后续步骤里基于这份摘要继续给出更清晰的学习建议。"
    )
    return StepOutput(content=summary, success=True)


def run_workflow_basics_example() -> None:
    """运行最基础的顺序型 Workflow 示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责判断用户当前处于什么学习阶段。",
        instructions=[
            "请根据用户提供的学习进度，判断当前所处阶段。",
            "输出时请给出阶段名称、已经掌握的重点、当前最需要巩固的能力。",
        ],
        markdown=True,
    )

    lesson_planner = model_wrapper.create_agent(
        name="课程规划员",
        role="负责基于前面步骤的结果安排下一课。",
        instructions=[
            "你会收到前一个步骤整理好的学习阶段摘要。",
            "请基于摘要给出下一课建议，并说明为什么这样安排。",
            "回答尽量清晰、具体，适合继续按课程节奏学习。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Workflow 基础课",
        description="用顺序步骤把学习阶段分析和下一课规划串起来。",
        steps=[
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前进度处于哪一个学习阶段。",
            ),
            Step(
                name="摘要整理",
                executor=extract_stage_summary,
                description="把上一步结果整理成更适合继续规划的摘要。",
            ),
            Step(
                name="下一课规划",
                agent=lesson_planner,
                description="基于前面步骤输出安排下一课。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team，"
            "并且完成了整合课和真实项目骨架深化课。"
            "请帮我判断我现在处于什么阶段，并安排下一课。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_basics_example()
