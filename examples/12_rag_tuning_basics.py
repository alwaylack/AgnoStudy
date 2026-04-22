from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_knowledge(collection_name: str, search_type: SearchType) -> Knowledge:
    """根据指定的检索模式创建一个知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / f"chromadb_{collection_name}"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection=collection_name,
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=search_type,
    )

    knowledge = Knowledge(
        name=collection_name,
        vector_db=vector_db,
    )

    markdown_reader = MarkdownReader(chunk_size=1200)

    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=markdown_reader,
            upsert=True,
        )

    return knowledge


def run_rag_tuning_basics_example() -> None:
    """演示如何通过不同检索模式和上下文注入方式调优 RAG。"""
    model = OpenAIModel.from_env()

    vector_knowledge = build_knowledge(
        collection_name="agno_study_vector_rag",
        search_type=SearchType.vector,
    )
    hybrid_knowledge = build_knowledge(
        collection_name="agno_study_hybrid_rag",
        search_type=SearchType.hybrid,
    )

    vector_agent = model.create_agent(
        name="Agno Vector RAG Agent",
        knowledge=vector_knowledge,
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请基于知识库回答问题。",
        ],
        markdown=True,
        # debug_mode=True,
    )

    hybrid_context_agent = model.create_agent(
        name="Agno Hybrid Context Agent",
        knowledge=hybrid_knowledge,
        # 这里不只是搜索知识库，还把检索结果直接注入上下文。
        add_knowledge_to_context=True,
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请尽量依据已检索到的知识库内容组织回答。",
            "如果答案来自知识库，请保持表述贴近资料内容。",
        ],
        markdown=True,
        debug_mode=True,
    )

    query = "请解释 Knowledge、Memory、Tools 三者在真实项目中的分工。"

    print("\n--- 示例 1：Vector 检索 ---")
    vector_agent.print_response(query)

    print("\n--- 示例 2：Hybrid 检索 + 上下文注入 ---")
    hybrid_context_agent.print_response(query)


if __name__ == "__main__":
    run_rag_tuning_basics_example()
