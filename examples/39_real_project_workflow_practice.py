from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from agno.workflow import Condition, Loop, Parallel, Router, Step, StepOutput, Steps, Workflow

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_real_project_workflow_knowledge() -> Knowledge:
    """构建更长链路真实项目实践课使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_real_project_workflow"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档：{document_path}")

    vector_db = ChromaDb(
        collection="agno_real_project_workflow",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_real_project_workflow",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge


def estimate_weekly_hours(current_stage: str, urgency: str = "normal") -> str:
    """根据阶段和节奏给出建议的每周投入。"""
    stage = current_stage.lower()
    if "workflow" in stage or "project" in stage:
        hours = "4 到 6 小时"
    elif "knowledge" in stage or "rag" in stage:
        hours = "3 到 5 小时"
    else:
        hours = "2 到 4 小时"

    if urgency.lower() in {"high", "紧凑", "intensive"}:
        return f"建议每周投入 {hours}，并额外安排 1 次完整联调。"
    return f"建议每周投入 {hours}，保持持续练习即可。"


def choose_practice_deliverable(goal: str) -> str:
    """根据目标建议更合适的练习产物。"""
    lowered_goal = goal.lower()
    if "workflow" in lowered_goal or "编排" in lowered_goal:
        return "更适合的练习产物是一个包含分流、协作、细化三段流程的最小工作流项目。"
    if "knowledge" in lowered_goal or "rag" in lowered_goal:
        return "更适合的练习产物是一个带共享知识库和可验证检索结果的学习助手示例。"
    if "team" in lowered_goal or "协作" in lowered_goal:
        return "更适合的练习产物是一个包含多成员分工与汇总的 Team 协作示例。"
    return "更适合的练习产物是一个能跑通主链路的小型学习助手应用。"


def should_use_advanced_project_path(step_input) -> bool:
    """判断是否进入更完整的真实项目路径。"""
    user_input = (step_input.input or "").lower()
    advanced_keywords = [
        "workflow",
        "team",
        "knowledge",
        "rag",
        "router",
        "project",
        "项目",
        "工作流",
        "协作",
    ]
    return any(keyword in user_input for keyword in advanced_keywords)


def build_foundation_path_note(step_input) -> StepOutput:
    """生成巩固路径说明。"""
    return StepOutput(
        content=(
            "当前进入巩固路径。\n"
            "建议先回顾已经学过的 Workflow 基础模式和 Team / Knowledge 的职责边界，"
            "再进入更长链路的真实项目实践。"
        ),
        success=True,
    )


def build_project_path_note(step_input) -> StepOutput:
    """生成真实项目路径说明。"""
    return StepOutput(
        content=(
            "当前进入真实项目路径。\n"
            "接下来更适合围绕一个完整目标，把需求识别、分流、知识检索、团队协作、"
            "计划细化和最终输出串成一条主链路。"
        ),
        success=True,
    )


def select_learning_route(step_input) -> str:
    """根据输入目标选择后续更合适的子流程。"""
    user_input = (step_input.input or "").lower()
    if "knowledge" in user_input or "rag" in user_input or "检索" in user_input:
        return "knowledge_route"
    if "team" in user_input or "协作" in user_input or "multi-agent" in user_input:
        return "team_route"
    return "workflow_route"


def refine_project_plan(step_input) -> StepOutput:
    """逐轮细化真实项目实践计划。"""
    previous_content = str(step_input.previous_step_content or "")

    if "第 1 轮细化完成" not in previous_content:
        content = (
            "第 1 轮细化完成。\n"
            "当前先给出一版主链路：\n"
            "1. 先做需求识别与阶段判断。\n"
            "2. 再按目标分流到 Workflow / Knowledge / Team 路线。\n"
            "3. 然后并行分析能力缺口与可交付产物。\n"
            "4. 最后输出一份可以直接开做的小项目计划。\n"
        )
    else:
        content = (
            "第 2 轮细化完成。\n"
            "在第一轮基础上补全执行细节：\n"
            "1. 先保留一个共享知识库，避免各步骤资料来源分散。\n"
            "2. Team 阶段优先负责协作分析，不负责整条流程编排。\n"
            "3. Workflow 阶段负责主链路推进与最终收口。\n"
            "4. 最终产物要包含运行入口、知识来源、协作角色和下一步扩展点。\n"
        )

    return StepOutput(content=content, success=True)


def stop_when_plan_is_clear(outputs: list[StepOutput]) -> bool:
    """当计划已经完成第二轮细化时停止循环。"""
    return any("第 2 轮细化完成" in str(output.content or "") for output in outputs)


def build_project_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建用于真实项目实践阶段的协作团队。"""
    research_agent = model_wrapper.create_agent(
        name="项目资料研究成员",
        role="负责从共享知识库里提炼当前最值得复用的知识点。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请优先基于共享知识库，提炼当前最值得复用到真实项目实践里的知识点。",
            "回答时聚焦在能直接帮助下一步动手的内容上。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="项目规划成员",
        role="负责把目标拆成下一阶段可执行的小项目安排。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_weekly_hours, choose_practice_deliverable],
        instructions=[
            "请基于共享知识库给出真实项目实践阶段的任务拆解。",
            "当涉及每周投入和产物形式时，优先调用工具。",
        ],
        markdown=True,
    )

    review_agent = model_wrapper.create_agent(
        name="项目审查成员",
        role="负责指出当前计划里还缺什么，以及先做什么最稳妥。",
        instructions=[
            "请审查当前项目计划是否已经足够可执行。",
            "如果还不够，请指出最先需要补齐的部分。",
        ],
        markdown=True,
    )

    return Team(
        name="真实项目实践协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[research_agent, planning_agent, review_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的真实项目实践团队。",
            "请围绕下一阶段学习助手项目目标，协作完成研究、规划和审查。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def run_real_project_workflow_practice_example() -> None:
    """运行更长链路的真实项目实践 Workflow 示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_real_project_workflow_knowledge()

    intake_agent = model_wrapper.create_agent(
        name="项目需求识别员",
        role="负责识别当前学习进度、目标和最想解决的问题。",
        instructions=[
            "请先识别用户当前学到哪里了，以及这次最想推进的真实项目目标是什么。",
            "输出尽量简洁，方便后续步骤继续使用。",
        ],
        markdown=True,
    )

    workflow_route_agent = model_wrapper.create_agent(
        name="工作流路线成员",
        role="负责给出更偏 Workflow 编排视角的推进建议。",
        instructions=[
            "请从 Workflow 主链路编排角度，给出下一阶段最合适的推进建议。",
            "回答时要强调步骤顺序和职责边界。",
        ],
        markdown=True,
    )

    knowledge_route_agent = model_wrapper.create_agent(
        name="知识路线成员",
        role="负责给出更偏 Knowledge / RAG 视角的推进建议。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请基于共享知识库，给出更偏 Knowledge / RAG 方向的下一阶段推进建议。",
            "优先说明还缺少哪些资料组织与检索验证。",
        ],
        markdown=True,
    )

    capability_gap_agent = model_wrapper.create_agent(
        name="能力缺口分析员",
        role="负责分析当前离真实项目实践还差哪些关键能力。",
        instructions=[
            "请根据当前上下文，分析离真实项目实践还差哪些关键能力。",
            "回答时优先给出 2 到 4 个最关键缺口。",
        ],
        markdown=True,
    )

    deliverable_agent = model_wrapper.create_agent(
        name="交付物分析员",
        role="负责判断下一阶段最适合做成什么样的可运行产物。",
        tools=[estimate_weekly_hours, choose_practice_deliverable],
        instructions=[
            "请判断下一阶段最适合产出什么样的可运行结果。",
            "涉及每周投入和交付物形式时，优先调用工具。",
        ],
        markdown=True,
    )

    final_summary_agent = model_wrapper.create_agent(
        name="真实项目计划汇总员",
        role="负责整合整条工作流的结果，输出最终学习计划。",
        instructions=[
            "你会收到前面各阶段的结果，请把它们整合成一份清晰的真实项目实践计划。",
            "最终回答需要包含：当前阶段判断、主链路建议、能力缺口、推荐交付物、每周投入、下一课方向。",
        ],
        markdown=True,
    )

    project_team = build_project_team(model_wrapper, knowledge)

    workflow_route = Steps(
        name="workflow_route",
        description="更偏 Workflow 编排的子流程。",
        steps=[
            Step(
                name="工作流路线分析",
                agent=workflow_route_agent,
                description="从 Workflow 主链路编排角度给出推进建议。",
            )
        ],
    )

    knowledge_route = Steps(
        name="knowledge_route",
        description="更偏 Knowledge / RAG 的子流程。",
        steps=[
            Step(
                name="知识路线分析",
                agent=knowledge_route_agent,
                description="从 Knowledge / RAG 角度给出推进建议。",
            )
        ],
    )

    team_route = Steps(
        name="team_route",
        description="更偏 Team 协作实践的子流程。",
        steps=[
            Step(
                name="团队项目协作分析",
                team=project_team,
                description="让团队围绕真实项目目标完成协作分析。",
            )
        ],
    )

    workflow = Workflow(
        name="Agno 真实项目实践长链路课",
        description="把需求识别、分流、知识检索、团队协作、并行分析和循环细化串成一条完整工作流。",
        steps=[
            Step(
                name="项目需求识别",
                agent=intake_agent,
                description="先识别当前进度、目标和本次想推进的方向。",
            ),
            Condition(
                name="项目路径判断",
                description="判断当前是否适合直接进入更完整的真实项目路径。",
                evaluator=should_use_advanced_project_path,
                steps=[
                    Step(
                        name="真实项目路径说明",
                        executor=build_project_path_note,
                        description="进入真实项目路径时补充一条方向说明。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径说明",
                        executor=build_foundation_path_note,
                        description="如果还需要巩固，则补充一条巩固说明。",
                    )
                ],
            ),
            Router(
                name="学习目标分流",
                description="根据当前目标，把请求送到更合适的子流程。",
                selector=select_learning_route,
                choices=[workflow_route, knowledge_route, team_route],
            ),
            Parallel(
                Step(
                    name="能力缺口并行分析",
                    agent=capability_gap_agent,
                    description="并行分析离真实项目实践还缺哪些关键能力。",
                ),
                Step(
                    name="交付物并行分析",
                    agent=deliverable_agent,
                    description="并行分析下一阶段更适合做成什么样的产物。",
                ),
                name="并行收束分析",
                description="在分流结果基础上，同时分析能力缺口和交付物方向。",
            ),
            Loop(
                name="项目计划细化循环",
                description="把前面得到的项目建议逐轮细化成更可执行的计划。",
                steps=[
                    Step(
                        name="项目计划细化器",
                        executor=refine_project_plan,
                        description="逐轮细化下一阶段真实项目实践计划。",
                    )
                ],
                max_iterations=3,
                end_condition=stop_when_plan_is_clear,
                forward_iteration_output=True,
            ),
            Step(
                name="最终项目计划汇总",
                agent=final_summary_agent,
                description="整合整条工作流结果，输出最终真实项目实践计划。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、组合课、Workflow + Team、Workflow + Knowledge、"
            "Workflow + Team + Knowledge、小型工作流、应用骨架整合，以及 Router 编排。"
            "现在我想继续进入更长链路的真实项目实践，请帮我设计下一阶段学习助手项目的推进计划。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_real_project_workflow_practice_example()
