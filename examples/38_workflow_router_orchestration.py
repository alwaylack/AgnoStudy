from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from agno.workflow import Router, Step, Steps, Workflow

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_router_workflow_knowledge() -> Knowledge:
    """构建供路由式工作流使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_workflow_router"
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
        collection="agno_workflow_router",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_workflow_router",
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


def select_learning_route(step_input) -> str:
    """根据用户目标选择最合适的子流程。"""
    user_input = (step_input.input or "").lower()
    if "knowledge" in user_input or "rag" in user_input or "检索" in user_input:
        return "knowledge_route"
    if "team" in user_input or "协作" in user_input:
        return "team_route"
    return "workflow_route"


def build_learning_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建用于团队协作路线的学习团队。"""
    concept_agent = model_wrapper.create_agent(
        name="协作概念成员",
        role="负责解释团队协作相关的关键概念。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请基于共享知识库解释 Team 协作路线里的关键概念。",
            "回答要聚焦在当前目标真正需要的内容上。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="协作规划成员",
        role="负责给出团队协作路线的下一步安排。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请基于共享知识库给出 Team 协作路线的下一步安排。",
            "回答时要说明为什么这样安排。",
        ],
        markdown=True,
    )

    return Team(
        name="路由学习协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的学习团队。",
            "请从概念理解和路线规划两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def run_workflow_router_orchestration_example() -> None:
    """运行 Router 驱动的复杂工作流编排示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_router_workflow_knowledge()

    intake_agent = model_wrapper.create_agent(
        name="路由背景识别员",
        role="负责先识别当前请求的目标倾向。",
        instructions=[
            "请先识别用户这次更偏向 Workflow、Knowledge 还是 Team 协作目标。",
            "输出尽量简洁，为后续路由阶段提供上下文。",
        ],
        markdown=True,
    )

    workflow_focus_agent = model_wrapper.create_agent(
        name="工作流路线成员",
        role="负责 Workflow 路线的分析与建议。",
        instructions=[
            "请围绕 Workflow 实现路线给出下一阶段学习建议。",
            "回答要偏实现导向。",
        ],
        markdown=True,
    )

    knowledge_focus_agent = model_wrapper.create_agent(
        name="知识路线成员",
        role="负责 Knowledge / RAG 路线的分析与建议。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请基于共享知识库给出 Knowledge / RAG 路线的下一步建议。",
            "回答时优先引用当前阶段最相关的知识点。",
        ],
        markdown=True,
    )

    summary_agent = model_wrapper.create_agent(
        name="路由结果汇总员",
        role="负责整合路由后的子流程结果，输出最终建议。",
        instructions=[
            "你会收到前面的背景识别和路由子流程结果。",
            "请整合这些信息，给出最终的下一阶段学习建议。",
        ],
        markdown=True,
    )

    learning_team = build_learning_team(model_wrapper, knowledge)

    workflow_route = Steps(
        name="workflow_route",
        description="偏 Workflow 实现路线的子流程。",
        steps=[
            Step(
                name="工作流路线分析",
                agent=workflow_focus_agent,
                description="围绕 Workflow 路线生成实现导向建议。",
            )
        ],
    )

    knowledge_route = Steps(
        name="knowledge_route",
        description="偏 Knowledge / RAG 路线的子流程。",
        steps=[
            Step(
                name="知识路线分析",
                agent=knowledge_focus_agent,
                description="围绕共享知识库生成 Knowledge 路线建议。",
            )
        ],
    )

    team_route = Steps(
        name="team_route",
        description="偏 Team 协作路线的子流程。",
        steps=[
            Step(
                name="团队路线分析",
                team=learning_team,
                description="让团队协作完成 Team 路线建议。",
            )
        ],
    )

    workflow = Workflow(
        name="Agno Router 编排进阶课",
        description="学习如何用 Router 把请求分流到不同子流程中。",
        steps=[
            Step(
                name="路由背景识别",
                agent=intake_agent,
                description="先识别这次请求的目标倾向。",
            ),
            Router(
                name="学习路线分流器",
                description="根据目标把请求送进最合适的子流程。",
                selector=select_learning_route,
                choices=[workflow_route, knowledge_route, team_route],
            ),
            Step(
                name="最终路由汇总",
                agent=summary_agent,
                description="整合背景识别和子流程结果，输出最终建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、组合课、Workflow + Team、"
            "Workflow + Knowledge、Workflow + Team + Knowledge，以及应用骨架整合。"
            "现在我更想继续推进 Team 协作方向，请用更复杂的工作流编排方式帮我安排下一阶段学习。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_router_orchestration_example()
