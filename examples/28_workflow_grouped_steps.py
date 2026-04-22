from agno.workflow import Step, StepOutput, Steps, Workflow

from models import OpenAIModel


def build_stage_brief(step_input) -> StepOutput:
    """把阶段分析结果整理成更适合继续规划的简报。"""
    stage_analysis = step_input.get_step_content("阶段分析") or step_input.previous_step_content or ""
    brief = (
        "学习阶段简报：\n"
        f"{stage_analysis}\n\n"
        "下面请继续基于这份简报，拆出下一课规划所需的关键点。"
    )
    return StepOutput(content=brief, success=True)


def extract_planning_focus(step_input) -> StepOutput:
    """从阶段简报里提炼下一课规划重点。"""
    brief = step_input.get_step_content("阶段简报") or step_input.previous_step_content or ""
    focus = (
        "下一课规划重点：\n"
        f"{brief}\n\n"
        "请优先安排一个既能承接当前阶段、又能自然扩展后续能力的主题。"
    )
    return StepOutput(content=focus, success=True)


def run_workflow_grouped_steps_example() -> None:
    """运行 Grouped Steps 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责判断用户当前处于哪个学习阶段。",
        instructions=[
            "请根据用户已经学过的内容判断当前学习阶段。",
            "输出时请说明当前阶段、已经掌握的重点、下一阶段最值得切入的方向。",
        ],
        markdown=True,
    )

    lesson_planner = model_wrapper.create_agent(
        name="课程规划员",
        role="负责根据步骤组整理出的重点安排下一课。",
        instructions=[
            "你会收到一个由步骤组整理好的规划重点。",
            "请基于这些重点给出下一课建议，并说明为什么这样安排。",
            "输出尽量清晰，适合作为继续学习的课程安排。",
        ],
        markdown=True,
    )

    planning_steps = Steps(
        name="下一课规划步骤组",
        description="把阶段分析结果整理成更适合生成课程建议的中间信息。",
        steps=[
            Step(
                name="阶段简报",
                executor=build_stage_brief,
                description="先把阶段分析整理成一份简报。",
            ),
            Step(
                name="规划重点提炼",
                executor=extract_planning_focus,
                description="再从简报里提炼下一课规划重点。",
            ),
        ],
    )

    workflow = Workflow(
        name="Agno Grouped Steps 基础课",
        description="学习如何把多个顺序步骤封装成一个可复用的步骤组。",
        steps=[
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前学习进度所处阶段。",
            ),
            planning_steps,
            Step(
                name="下一课规划",
                agent=lesson_planner,
                description="基于步骤组整理出的重点安排下一课。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经完成了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及最基础的 Workflow 顺序课。"
            "请帮我判断我现在的学习阶段，并安排下一课。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_grouped_steps_example()
