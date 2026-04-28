from agno.workflow import Loop, Step, StepOutput, Workflow

from models import OpenAIModel


def expand_study_plan(step_input) -> StepOutput:
    """模拟按轮次逐步细化学习计划。"""
    previous_content = str(step_input.previous_step_content or "")

    if "第1轮迭代完成" not in previous_content:
        content = (
            "第1轮迭代完成。\n"
            "当前先给出一个基础学习计划：\n"
            "1. 回顾 Workflow 的顺序、分组、条件、并行四种模式。\n"
            "2. 明确下一步要学习循环执行模式。\n"
            "3. 先建立 Loop 的使用直觉，再继续复杂组合。\n"
        )
    else:
        content = (
            "第2轮迭代完成。\n"
            "在上一轮基础上进一步细化学习计划：\n"
            "1. 先理解 Loop 会重复执行同一组步骤。\n"
            "2. 再理解 max_iterations 和 end_condition 的关系。\n"
            "3. 最后观察 forward_iteration_output 如何把上一轮结果传给下一轮。\n"
            "4. 学完后继续进入更复杂的 Workflow 组合模式。\n"
        )

    return StepOutput(content=content, success=True)


def is_loop_good_enough(outputs: list[StepOutput]) -> bool:
    """当迭代计划已经进入第二轮细化时结束循环。"""
    for output in outputs:
        if output.content and "第2轮迭代完成" in str(output.content):
            return True
    return False


def run_workflow_loop_basics_example() -> None:
    """运行 Loop 循环 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    final_planner = model_wrapper.create_agent(
        name="循环结果汇总员",
        role="负责整合多轮迭代结果，给出最终学习建议。",
        instructions=[
            "你会收到 Loop 多轮迭代后的结果。",
            "请基于最终迭代内容，输出一份清晰的下一课学习建议。",
            "回答需要说明：本轮学习重点、为什么这样安排、下一步继续学什么。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Loop Workflow 基础课",
        description="学习如何通过循环步骤逐轮细化同一个任务。",
        steps=[
            Loop(
                name="学习计划细化循环",
                description="重复执行同一步骤，逐轮把学习计划变得更具体。",
                steps=[
                    Step(
                        name="学习计划迭代器",
                        executor=expand_study_plan,
                        description="每一轮都把学习计划再细化一点。",
                    )
                ],
                max_iterations=3,
                end_condition=is_loop_good_enough,
                forward_iteration_output=True,
            ),
            Step(
                name="最终循环汇总",
                agent=final_planner,
                description="整合循环后的最终结果，给出下一课建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition 和 Parallel。"
            "请用循环方式逐轮细化我的下一阶段学习计划，"
            "然后给我一个最终的下一课建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_loop_basics_example()
