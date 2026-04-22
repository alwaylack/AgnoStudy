from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_filtered_knowledge() -> Knowledge:
    """构建带 metadata 分类的知识库，便于演示精准检索。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_rag_filtering"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    beginner_doc = knowledge_dir / "agno_beginner_track.md"
    advanced_doc = knowledge_dir / "agno_advanced_track.md"

    for document_path in [beginner_doc, advanced_doc]:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_study_rag_filtering",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_study_rag_filtering",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)

    knowledge.insert(
        path=str(beginner_doc),
        metadata={"track": "beginner"},
        reader=reader,
        upsert=True,
    )
    knowledge.insert(
        path=str(advanced_doc),
        metadata={"track": "advanced"},
        reader=reader,
        upsert=True,
    )

    return knowledge


def run_rag_filtering_advanced_example() -> None:
    """演示如何通过 metadata 过滤提升 RAG 检索精度。"""
    model = OpenAIModel.from_env()
    knowledge = build_filtered_knowledge()

    manual_filter_agent = model.create_agent(
        name="Agno Manual Filter Agent",
        knowledge=knowledge,
        # 手动限制只检索 beginner 资料。
        knowledge_filters={"track": "beginner"},
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "你当前只能使用 beginner 资料回答问题。",
        ],
        markdown=True,
        debug_mode=True,
    )

    agentic_filter_agent = model.create_agent(
        name="Agno Agentic Filter Agent",
        knowledge=knowledge,
        # 让 Agent 在检索时根据问题自己决定更合适的 metadata 过滤范围。
        enable_agentic_knowledge_filters=True,
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "如果问题明显属于初学者或进阶阶段，请尽量选择更合适的知识过滤范围。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：手动过滤，只看 beginner 资料 ---")
    manual_filter_agent.print_response("我是初学者，下一步应该优先学习什么？")

    print("\n--- 示例 2：Agentic 过滤，自主选择更合适的资料 ---")
    agentic_filter_agent.print_response("我已经学完基础课程，下一阶段更适合先优化 RAG 还是先做多 Agent？")


if __name__ == "__main__":
    run_rag_filtering_advanced_example()
