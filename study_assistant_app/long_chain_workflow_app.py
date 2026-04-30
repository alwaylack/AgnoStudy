from agno.knowledge.knowledge import Knowledge
from agno.team import Team, TeamMode
from agno.workflow import Condition, Loop, Parallel, Router, Step, StepOutput, Steps, Workflow

from models import OpenAIModel

from .knowledge import build_study_knowledge
from .tools import estimate_stage_difficulty, suggest_next_lesson


def _should_use_project_path(step_input) -> bool:
    """判断当前是否适合直接进入真实项目路径。"""
    user_input = (step_input.input or "").lower()
    project_keywords = [
        "workflow",
        "team",
        "knowledge",
        "rag",
        "router",
        "project",
        "项目",
        "应用",
        "协作",
    ]
    return any(keyword in user_input for keyword in project_keywords)


def _build_foundation_note(step_input) -> StepOutput:
    """生成巩固路径说明。"""
    return StepOutput(
        content=(
            "当前进入巩固路径。\n"
            "建议先回顾已有的 Workflow、Knowledge 和 Team 职责边界，"
            "再进入更完整的应用级长链路整合。"
        ),
        success=True,
    )


def _build_project_note(step_input) -> StepOutput:
    """生成真实项目路径说明。"""
    return StepOutput(
        content=(
            "当前进入真实项目路径。\n"
            "接下来更适合把需求识别、目标分流、协作分析、计划细化和最终输出"
            "统一放回应用骨架中组织。"
        ),
        success=True,
    )


def _select_route(step_input) -> str:
    """根据当前目标选择更合适的应用内子流程。"""
    user_input = (step_input.input or "").lower()
    if "knowledge" in user_input or "rag" in user_input or "检索" in user_input:
        return "knowledge_route"
    if "team" in user_input or "协作" in user_input or "multi-agent" in user_input:
        return "team_route"
    return "workflow_route"


def _refine_app_plan(step_input) -> StepOutput:
    """逐轮细化应用级长链路计划。"""
    previous_content = str(step_input.previous_step_content or "")

    if "第 1 轮整合完成" not in previous_content:
        content = (
            "第 1 轮整合完成。\n"
            "当前先明确应用主链路：\n"
            "1. 先识别当前学习阶段和本次项目目标。\n"
            "2. 再按目标分流到 Workflow、Knowledge 或 Team 子流程。\n"
            "3. 然后并行分析下一步要补的能力和建议交付物。\n"
            "4. 最后统一输出应用级推进计划。\n"
        )
    else:
        content = (
            "第 2 轮整合完成。\n"
            "在第一轮基础上补齐应用结构细节：\n"
            "1. 统一使用共享知识库，避免资料来源分散。\n"
            "2. Team 负责协作分析，Workflow 负责主链路编排。\n"
            "3. 应用入口负责承接输入、触发流程并输出最终结果。\n"
            "4. 下一步可以继续拆出更完整的小项目模块。\n"
        )

    return StepOutput(content=content, success=True)


def _is_plan_clear(outputs: list[StepOutput]) -> bool:
    """当计划完成第二轮整合时停止循环。"""
    return any("第 2 轮整合完成" in str(output.content or "") for output in outputs)


def _build_project_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建用于应用级长链路整合的协作团队。"""
    knowledge_agent = model_wrapper.create_agent(
        name="应用资料成员",
        role="负责从共享知识库里提炼当前最值得复用的内容。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请优先基于共享知识库，提炼当前最值得复用到应用整合里的知识点。",
            "回答时聚焦在能直接帮助下一步实现的内容上。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="应用规划成员",
        role="负责把目标整理成应用级推进计划。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_stage_difficulty, suggest_next_lesson],
        instructions=[
            "请基于共享知识库，给出应用级长链路整合的推进安排。",
            "涉及难度判断和下一课建议时，优先调用工具。",
        ],
        markdown=True,
    )

    review_agent = model_wrapper.create_agent(
        name="应用审查成员",
        role="负责指出当前整合方案还缺少什么。",
        instructions=[
            "请审查当前应用级整合方案是否足够可执行。",
            "如果还不够，请指出最先需要补齐的部分。",
        ],
        markdown=True,
    )

    return Team(
        name="应用级长链路协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[knowledge_agent, planning_agent, review_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的应用级长链路团队。",
            "请围绕学习助手应用的下一阶段整合目标，完成研究、规划和审查。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def build_study_assistant_long_chain_workflow_app(
    model_wrapper: OpenAIModel | None = None,
) -> Workflow:
    """构建回接到应用骨架中的长链路 Workflow。"""
    wrapper = model_wrapper or OpenAIModel.from_env()
    knowledge = build_study_knowledge()
    project_team = _build_project_team(wrapper, knowledge)

    intake_agent = wrapper.create_agent(
        name="应用长链路需求识别员",
        role="负责识别当前阶段、目标和最想推进的问题。",
        instructions=[
            "请先识别当前学习进度，以及这次最想推进的应用级整合目标。",
            "输出尽量简洁，方便后续步骤继续使用。",
        ],
        markdown=True,
    )

    workflow_route_agent = wrapper.create_agent(
        name="应用工作流路线成员",
        role="负责给出更偏 Workflow 编排视角的建议。",
        instructions=[
            "请从应用级 Workflow 编排角度，给出下一阶段最合适的推进建议。",
            "回答时要强调步骤顺序和职责边界。",
        ],
        markdown=True,
    )

    knowledge_route_agent = wrapper.create_agent(
        name="应用知识路线成员",
        role="负责给出更偏 Knowledge / RAG 视角的建议。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请基于共享知识库，给出更偏 Knowledge / RAG 的应用整合建议。",
            "优先说明如何让知识库在应用骨架中更稳定复用。",
        ],
        markdown=True,
    )

    gap_agent = wrapper.create_agent(
        name="应用能力缺口分析员",
        role="负责分析当前离完整应用还差哪些关键能力。",
        instructions=[
            "请根据当前上下文，分析离更完整的小应用还差哪些关键能力。",
            "回答时优先给出 2 到 4 个关键缺口。",
        ],
        markdown=True,
    )

    deliverable_agent = wrapper.create_agent(
        name="应用交付物分析员",
        role="负责判断下一阶段最适合做成什么样的产物。",
        tools=[estimate_stage_difficulty, suggest_next_lesson],
        instructions=[
            "请判断下一阶段最适合做成什么样的应用级产物。",
            "涉及难度和下一课安排时，优先调用工具。",
        ],
        markdown=True,
    )

    summary_agent = wrapper.create_agent(
        name="应用长链路汇总员",
        role="负责整合整条工作流结果，输出最终应用推进计划。",
        instructions=[
            "你会收到前面各阶段的结果，请把它们整合成一份清晰的应用级推进计划。",
            "最终回答需要包含：当前阶段判断、主链路建议、能力缺口、推荐产物、下一课方向。",
        ],
        markdown=True,
    )

    workflow_route = Steps(
        name="workflow_route",
        description="更偏 Workflow 编排的应用子流程。",
        steps=[
            Step(
                name="应用工作流路线分析",
                agent=workflow_route_agent,
                description="从应用级 Workflow 编排角度给出推进建议。",
            )
        ],
    )

    knowledge_route = Steps(
        name="knowledge_route",
        description="更偏 Knowledge / RAG 的应用子流程。",
        steps=[
            Step(
                name="应用知识路线分析",
                agent=knowledge_route_agent,
                description="从应用级 Knowledge / RAG 角度给出推进建议。",
            )
        ],
    )

    team_route = Steps(
        name="team_route",
        description="更偏 Team 协作的应用子流程。",
        steps=[
            Step(
                name="应用团队协作分析",
                team=project_team,
                description="让团队围绕应用级目标完成协作分析。",
            )
        ],
    )

    return Workflow(
        name="Agno 学习助手应用级长链路 Workflow",
        description="把长链路 Workflow 重新接回应用骨架中的学习助手工作流。",
        steps=[
            Step(
                name="应用长链路需求识别",
                agent=intake_agent,
                description="先识别当前进度、目标和本次最想推进的方向。",
            ),
            Condition(
                name="应用长链路路径判断",
                description="判断当前是否适合直接进入更完整的应用整合路径。",
                evaluator=_should_use_project_path,
                steps=[
                    Step(
                        name="应用真实项目路径说明",
                        executor=_build_project_note,
                        description="进入真实项目路径时补充一条方向说明。",
                    )
                ],
                else_steps=[
                    Step(
                        name="应用巩固路径说明",
                        executor=_build_foundation_note,
                        description="如果还需要巩固，则补充一条说明。",
                    )
                ],
            ),
            Router(
                name="应用学习目标分流",
                description="根据当前目标，把请求送到更合适的应用内子流程。",
                selector=_select_route,
                choices=[workflow_route, knowledge_route, team_route],
            ),
            Parallel(
                Step(
                    name="应用能力缺口并行分析",
                    agent=gap_agent,
                    description="并行分析当前离更完整应用还缺哪些关键能力。",
                ),
                Step(
                    name="应用交付物并行分析",
                    agent=deliverable_agent,
                    description="并行分析下一阶段更适合做成什么样的应用产物。",
                ),
                name="应用并行收束分析",
                description="在分流结果基础上，同时分析能力缺口和建议产物。",
            ),
            Loop(
                name="应用计划细化循环",
                description="把前面得到的应用建议逐轮细化成更可执行的计划。",
                steps=[
                    Step(
                        name="应用计划细化器",
                        executor=_refine_app_plan,
                        description="逐轮细化下一阶段应用级整合计划。",
                    )
                ],
                max_iterations=3,
                end_condition=_is_plan_clear,
                forward_iteration_output=True,
            ),
            Step(
                name="应用最终计划汇总",
                agent=summary_agent,
                description="整合整条工作流结果，输出最终应用推进计划。",
            ),
        ],
        debug_mode=True,
    )


def run_study_assistant_long_chain_workflow_app() -> None:
    """运行回接到应用骨架中的长链路 Workflow。"""
    workflow = build_study_assistant_long_chain_workflow_app()
    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、组合课、Workflow + Team、Workflow + Knowledge、"
            "Workflow + Team + Knowledge、长链路真实项目实践，以及应用骨架整合。"
            "现在我想把这条长链路重新接回更完整的小应用，请帮我安排下一阶段推进计划。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
