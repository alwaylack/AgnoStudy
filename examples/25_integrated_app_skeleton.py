from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def estimate_topic_difficulty(topic: str) -> str:
    """根据主题给出一个简单的学习难度判断。"""
    difficulty_map = {
        "agent": "基础，适合作为入门主题。",
        "tools": "基础到中等，适合在掌握 Agent 后学习。",
        "knowledge": "中等，建议在 Tools 和基础 Agent 之后学习。",
        "team": "中等到进阶，建议在单 Agent 和 RAG 基础之后学习。",
        "rag": "中等到进阶，建议在 Knowledge 基础跑通后再做调优。",
    }
    return difficulty_map.get(
        topic.lower(),
        f"{topic} 建议先从最小可运行示例开始，再逐步扩展复杂度。",
    )


def suggest_next_module(current_stage: str) -> str:
    """根据当前阶段给出下一步建议。"""
    stage = current_stage.lower()
    if "team" in stage and "knowledge" in stage:
        return "下一步建议做真实项目骨架：把 Team、Knowledge、Tools 组合进一个稳定入口。"
    if "rag" in stage:
        return "下一步建议把 Knowledge 和 Team 结合起来，体验协作式 RAG。"
    return "下一步建议继续沿主线学习，并优先保持示例最小可运行。"


def build_shared_knowledge() -> Knowledge:
    """构建一个供综合示例使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`") from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_integrated_app"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_integrated_app_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_integrated_app_knowledge",
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


def build_learning_team(model_wrapper: OpenAIModel,
                        knowledge: Knowledge) -> Team:
    """构建一个共享知识库和工具的学习协作团队。"""
    research_agent = model_wrapper.create_agent(
        name="知识研究专家",
        role="负责从知识库中提取关键信息",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你擅长从知识库中提取与问题最相关的信息。",
            "请尽量基于资料内容总结，不要脱离资料随意扩展。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="学习规划专家",
        role="负责结合工具和知识库安排下一步学习路线",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_topic_difficulty, suggest_next_module],
        instructions=[
            "你擅长制定学习计划。",
            "当问题涉及难度或下一步安排时，请优先调用工具。",
        ],
        markdown=True,
    )

    return Team(
        name="Agno 综合学习团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[research_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个综合型学习团队协调者。",
            "请先根据共享知识库理解问题，再协调合适成员完成分析。",
            "最终答案需要同时包含知识解释、难度判断和下一步建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )


def run_integrated_app_skeleton_example() -> None:
    """运行综合项目骨架示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_shared_knowledge()
    team = build_learning_team(model_wrapper, knowledge)

    # 这个问题会同时触发知识库检索、工具判断和 Team 协调。
    team.print_response(
        "我已经学完 Agent、Tools、Knowledge 和 Team 的基础模式。请基于共享知识库和工具，帮我判断我现在学习 Team + Knowledge + Tools 组合课的难度，并给我一个下一步的学习建议。"
    )


if __name__ == "__main__":
    run_integrated_app_skeleton_example()
