from agno.workflow import Condition, Step, StepOutput, Workflow

from models import OpenAIModel


def should_take_advanced_branch(step_input) -> bool:
    """根据前一步的阶段分析结果判断是否进入进阶分支。"""
    stage_analysis = str(step_input.get_step_content("阶段分析") or "")
    advanced_keywords = ["workflow", "团队", "team", "进阶", "骨架", "整合"]
    return any(keyword in stage_analysis.lower() for keyword in advanced_keywords)


def prepare_beginner_path(step_input) -> StepOutput:
    """整理更适合巩固型学习的下一课建议。"""
    stage_analysis = step_input.get_step_content("阶段分析") or ""
    content = (
        "当前更适合走巩固分支。\n"
        f"阶段分析参考：\n{stage_analysis}\n\n"
        "建议先补强当前阶段的基础理解，再进入更复杂的 Workflow 模式。"
    )
    return StepOutput(content=content, success=True)


def prepare_advanced_path(step_input) -> StepOutput:
    """整理更适合进阶型学习的下一课建议。"""
    stage_analysis = step_input.get_step_content("阶段分析") or ""
    content = (
        "当前更适合走进阶分支。\n"
        f"阶段分析参考：\n{stage_analysis}\n\n"
        "建议继续学习带条件分支、并行和循环的 Workflow，逐步进入更复杂的流程编排。"
    )
    return StepOutput(content=content, success=True)


def run_workflow_condition_basics_example() -> None:
    """运行 Condition 条件分支 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责判断当前学习阶段，并给出阶段特征。",
        instructions=[
            "请根据用户已经完成的课程判断当前学习阶段。",
            "回答时请说明当前阶段、已掌握重点，以及接下来更适合巩固还是继续进阶。",
        ],
        markdown=True,
    )

    final_planner = model_wrapper.create_agent(
        name="分支总结规划员",
        role="负责结合分支结果给出最终下一课建议。",
        instructions=[
            "你会收到前面步骤生成的分支建议。",
            "请基于分支结果给出最终下一课安排，并说明为什么这样安排。",
            "输出要清晰，适合作为继续学习的课程建议。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Condition Workflow 基础课",
        description="学习如何根据条件判断执行不同分支。",
        steps=[
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前学习阶段。",
            ),
            Condition(
                name="学习路径分支",
                description="根据阶段分析结果判断走巩固分支还是进阶分支。",
                evaluator=should_take_advanced_branch,
                steps=[
                    Step(
                        name="进阶路径建议",
                        executor=prepare_advanced_path,
                        description="当阶段已经进入进阶区间时，生成进阶路径建议。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径建议",
                        executor=prepare_beginner_path,
                        description="当阶段仍需要巩固时，生成巩固路径建议。",
                    )
                ],
            ),
            Step(
                name="最终下一课规划",
                agent=final_planner,
                description="综合分支结果，给出最终下一课安排。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及 Workflow 的基础课和 Steps 课程。"
            "请判断我现在应该走巩固分支还是进阶分支，并安排下一课。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_condition_basics_example()
