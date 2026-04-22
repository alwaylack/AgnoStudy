from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_team_knowledge() -> Knowledge:
    """构建供 Team 共享使用的知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_team_shared_knowledge"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_team_shared_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_team_shared_knowledge",
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


def run_team_shared_knowledge_example() -> None:
    """演示如何让 Team 共享同一个 Knowledge。"""
    model = OpenAIModel.from_env()
    knowledge = build_team_knowledge()

    concept_agent = model.create_agent(
        name="概念专家",
        role="负责解释概念和模块关系",
        instructions=[
            "你擅长解释 Agno 中不同模块的分工。",
            "请尽量把概念关系讲清楚。",
        ],
        markdown=True,
    )

    roadmap_agent = model.create_agent(
        name="路线规划专家",
        role="负责给出学习顺序和下一步行动建议",
        instructions=[
            "你擅长安排学习路线。",
            "请优先给出清晰的下一步学习安排。",
        ],
        markdown=True,
    )

    # Team 共享同一个 Knowledge，这样多个成员可以围绕同一份资料协作。
    team = Team(
        name="Agno 共享知识团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[concept_agent, roadmap_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是团队协调者。",
            "请基于共享知识库协调成员回答问题。",
            "最终答案要同时包含概念解释和下一步学习建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "请基于共享知识库，解释 Knowledge、Memory 和 Team 三者在 Agno 学习路径中的位置，并给我一个下一阶段学习建议。"
    )


if __name__ == "__main__":
    run_team_shared_knowledge_example()
