from agno.workflow import Parallel, Step, Workflow

from models import OpenAIModel


def run_workflow_parallel_basics_example() -> None:
    """运行 Parallel 并行 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    capability_analyst = model_wrapper.create_agent(
        name="能力盘点分析员",
        role="负责分析当前已经掌握的能力。",
        instructions=[
            "请根据用户已经完成的学习内容，梳理当前已经掌握的核心能力。",
            "输出时尽量按要点整理，帮助后续步骤快速使用。",
        ],
        markdown=True,
    )

    next_stage_analyst = model_wrapper.create_agent(
        name="下一阶段分析员",
        role="负责分析当前最值得继续推进的方向。",
        instructions=[
            "请根据用户当前进度，判断下一阶段最值得继续推进的主题。",
            "输出时请说明为什么这个方向最适合现在继续学习。",
        ],
        markdown=True,
    )

    final_planner = model_wrapper.create_agent(
        name="并行结果汇总员",
        role="负责整合多个并行分支的结果，给出最终学习建议。",
        instructions=[
            "你会收到多个并行步骤的分析结果。",
            "请整合这些结果，给出一份清晰的下一课建议。",
            "最终回答要同时包含：当前能力总结、下一阶段重点、下一课安排。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Parallel Workflow 基础课",
        description="学习如何让多个独立步骤并行执行，再统一汇总结果。",
        steps=[
            Parallel(
                Step(
                    name="能力盘点",
                    agent=capability_analyst,
                    description="并行分析当前已经掌握的能力。",
                ),
                Step(
                    name="下一阶段重点分析",
                    agent=next_stage_analyst,
                    description="并行分析下一阶段最值得推进的方向。",
                ),
                name="并行分析阶段",
                description="让多个独立分析步骤同时执行。",
            ),
            Step(
                name="最终并行汇总",
                agent=final_planner,
                description="整合并行阶段结果，生成最终下一课建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及 Workflow 的基础课、Steps 和 Condition。"
            "请并行分析我当前已经掌握的能力和下一阶段最适合继续推进的方向，"
            "然后给我一个最终的下一课建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_parallel_basics_example()
