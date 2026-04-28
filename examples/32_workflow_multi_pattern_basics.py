from agno.workflow import Condition, Loop, Parallel, Step, StepOutput, Workflow

from models import OpenAIModel


def should_use_advanced_path(step_input) -> bool:
    """根据输入判断是否进入进阶学习路径。"""
    user_input = (step_input.input or "").lower()
    advanced_keywords = ["workflow", "parallel", "condition", "loop", "team", "knowledge"]
    return any(keyword in user_input for keyword in advanced_keywords)


def build_beginner_direction(step_input) -> StepOutput:
    """生成更适合巩固阶段的方向说明。"""
    content = (
        "当前进入巩固路径。\n"
        "建议优先回顾已经学过的基础模式，确保对顺序、条件、并行、循环的差别足够清楚。"
    )
    return StepOutput(content=content, success=True)


def build_advanced_direction(step_input) -> StepOutput:
    """生成更适合进阶阶段的方向说明。"""
    content = (
        "当前进入进阶路径。\n"
        "建议开始学习如何把多种 Workflow 模式组合在同一个真实流程里。"
    )
    return StepOutput(content=content, success=True)


def refine_combined_plan(step_input) -> StepOutput:
    """把前面汇总的计划再细化一轮。"""
    previous_content = str(step_input.previous_step_content or "")

    if "第1轮细化完成" not in previous_content:
        content = (
            "第1轮细化完成。\n"
            "建议下一步先做一节多模式组合课，重点观察 Condition、Parallel、Loop 如何串联。\n"
            "再继续尝试把 Workflow 和 Team、Knowledge 组合起来。"
        )
    else:
        content = (
            "第2轮细化完成。\n"
            "最终学习建议：\n"
            "1. 先掌握多模式组合 Workflow。\n"
            "2. 再进入 Workflow + Team。\n"
            "3. 最后进入 Workflow + Knowledge，做更接近真实项目的编排。"
        )

    return StepOutput(content=content, success=True)


def stop_when_refined_enough(outputs: list[StepOutput]) -> bool:
    """当计划已经完成第二轮细化时结束循环。"""
    return any("第2轮细化完成" in str(output.content or "") for output in outputs)


def run_workflow_multi_pattern_basics_example() -> None:
    """运行多模式组合 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    capability_analyst = model_wrapper.create_agent(
        name="能力分析员",
        role="负责分析当前已经掌握的 Workflow 能力。",
        instructions=[
            "请总结用户当前已经掌握的 Workflow 模式和能力。",
            "输出尽量精炼，方便后续步骤引用。",
        ],
        markdown=True,
    )

    priority_analyst = model_wrapper.create_agent(
        name="重点分析员",
        role="负责判断下一阶段最值得优先推进的方向。",
        instructions=[
            "请根据用户当前进度，分析下一阶段最适合优先学习的方向。",
            "输出要说明为什么这个方向最值得优先学习。",
        ],
        markdown=True,
    )

    final_planner = model_wrapper.create_agent(
        name="组合流程汇总员",
        role="负责整合多模式流程的全部结果并给出最终建议。",
        instructions=[
            "你会收到条件分支、并行分析和循环细化后的结果。",
            "请整合这些信息，给出最终的下一课和后续阶段安排。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Multi-Pattern Workflow 基础课",
        description="学习如何把 Condition、Parallel、Loop 组合在同一个流程里。",
        steps=[
            Condition(
                name="学习路径选择",
                description="先判断当前更适合巩固还是进阶。",
                evaluator=should_use_advanced_path,
                steps=[
                    Step(
                        name="进阶路径说明",
                        executor=build_advanced_direction,
                        description="进入进阶路径时给出方向说明。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径说明",
                        executor=build_beginner_direction,
                        description="进入巩固路径时给出方向说明。",
                    )
                ],
            ),
            Parallel(
                Step(
                    name="能力盘点",
                    agent=capability_analyst,
                    description="并行分析当前已经掌握的 Workflow 能力。",
                ),
                Step(
                    name="优先级判断",
                    agent=priority_analyst,
                    description="并行判断下一阶段最值得优先推进的方向。",
                ),
                name="并行分析阶段",
                description="在确定路径后，同时做两路分析。",
            ),
            Loop(
                name="学习计划细化循环",
                description="把前面得到的学习建议再逐轮细化。",
                steps=[
                    Step(
                        name="组合计划细化器",
                        executor=refine_combined_plan,
                        description="逐轮细化下一阶段学习计划。",
                    )
                ],
                max_iterations=3,
                end_condition=stop_when_refined_enough,
                forward_iteration_output=True,
            ),
            Step(
                name="最终组合汇总",
                agent=final_planner,
                description="整合多模式流程结果，生成最终建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel 和 Loop。"
            "请用一个组合式 Workflow 帮我判断下一阶段最适合怎么继续学习，"
            "并给出最终的课程安排建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_multi_pattern_basics_example()
