from agno.knowledge.knowledge import Knowledge
from agno.team import Team, TeamMode
from agno.workflow import Condition, Step, Workflow

from models import OpenAIModel

from .knowledge import build_study_knowledge
from .tools import estimate_stage_difficulty, suggest_next_lesson


def _needs_advanced_path(step_input) -> bool:
    """根据输入判断当前是否更适合进入进阶路径。"""
    user_input = (step_input.input or "").lower()
    advanced_keywords = ["workflow", "team", "knowledge", "project", "骨架", "整合"]
    return any(keyword in user_input for keyword in advanced_keywords)


def _build_beginner_note(step_input):
    """生成巩固路径提示。"""
    from agno.workflow import StepOutput

    return StepOutput(
        content=(
            "当前进入巩固路径。\n"
            "建议先回顾当前已经学过的模式边界，再进入更复杂的应用骨架整合。"
        ),
        success=True,
    )


def _build_advanced_note(step_input):
    """生成进阶路径提示。"""
    from agno.workflow import StepOutput

    return StepOutput(
        content=(
            "当前进入进阶路径。\n"
            "建议开始把 Workflow、Team、Knowledge 放回完整应用骨架中统一组织。"
        ),
        success=True,
    )


def build_workflow_learning_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建用于应用骨架工作流的学习规划团队。"""
    concept_agent = model_wrapper.create_agent(
        name="应用概念成员",
        role="负责解释当前阶段最值得理解的关键概念。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请基于共享知识库解释当前阶段最关键的概念重点。",
            "回答尽量围绕当前阶段真正影响下一步实现的内容。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="应用规划成员",
        role="负责给出下一阶段实现安排。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_stage_difficulty, suggest_next_lesson],
        instructions=[
            "请基于共享知识库给出下一阶段实现安排。",
            "涉及难度判断和下一课建议时，请优先调用工具。",
        ],
        markdown=True,
    )

    return Team(
        name="应用骨架学习团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的应用骨架学习团队。",
            "请从概念理解和实现规划两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def build_study_assistant_workflow_app(model_wrapper: OpenAIModel | None = None) -> Workflow:
    """构建接入应用骨架的学习助手工作流。"""
    wrapper = model_wrapper or OpenAIModel.from_env()
    knowledge = build_study_knowledge()
    study_team = build_workflow_learning_team(wrapper, knowledge)

    intake_agent = wrapper.create_agent(
        name="应用需求识别员",
        role="负责识别当前背景和这次目标。",
        instructions=[
            "请先识别用户现在学到了哪里，以及这次最想推进的目标是什么。",
            "输出尽量简洁，为后续步骤提供上下文。",
        ],
        markdown=True,
    )

    summary_agent = wrapper.create_agent(
        name="应用计划汇总员",
        role="负责整合工作流结果并给出最终建议。",
        instructions=[
            "你会收到前面多个工作流阶段的结果。",
            "请整理成一份清晰的最终建议，包含当前阶段、学习重点、下一课安排和建议产出形式。",
        ],
        markdown=True,
    )

    return Workflow(
        name="Agno 学习助手应用骨架工作流",
        description="把 Workflow、Team、Knowledge 接回完整应用骨架中的学习助手工作流。",
        steps=[
            Step(
                name="应用需求识别",
                agent=intake_agent,
                description="先识别当前学习背景与本次目标。",
            ),
            Condition(
                name="应用路径判断",
                description="判断当前更适合巩固还是继续进阶。",
                evaluator=_needs_advanced_path,
                steps=[
                    Step(
                        name="进阶路径提示",
                        executor=_build_advanced_note,
                        description="进入进阶路径时补充一条提示。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径提示",
                        executor=_build_beginner_note,
                        description="进入巩固路径时补充一条提示。",
                    )
                ],
            ),
            Step(
                name="应用骨架协作规划",
                team=study_team,
                description="让团队基于共享知识库协作完成核心分析和规划。",
            ),
            Step(
                name="应用最终建议",
                agent=summary_agent,
                description="整合整个工作流结果，输出最终学习建议。",
            ),
        ],
        debug_mode=True,
    )


def run_study_assistant_workflow_app() -> None:
    """运行接入应用骨架后的学习助手工作流。"""
    workflow = build_study_assistant_workflow_app()
    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、组合课，以及 Workflow + Team、"
            "Workflow + Knowledge、Workflow + Team + Knowledge，还有更接近真实项目的小型工作流。"
            "现在我想把这些能力重新放回完整应用骨架里，请帮我安排下一阶段学习。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
