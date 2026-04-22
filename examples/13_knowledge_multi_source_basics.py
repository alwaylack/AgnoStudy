from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.json_reader import JSONReader
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def run_knowledge_multi_source_basics_example() -> None:
    """演示如何把 Markdown 和 JSON 一起接入同一个 Knowledge。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_multi_source"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    markdown_doc = knowledge_dir / "agno_rag_basics.md"
    json_doc = knowledge_dir / "agno_course_map.json"

    for document_path in [markdown_doc, json_doc]:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_study_multi_source_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_study_multi_source_knowledge",
        vector_db=vector_db,
    )

    # MarkdownReader 适合导入说明类资料。
    knowledge.insert(
        path=str(markdown_doc),
        metadata={"source_type": "markdown"},
        reader=MarkdownReader(chunk_size=1200),
        upsert=True,
    )

    # JSONReader 适合导入结构化数据资料。
    knowledge.insert(
        path=str(json_doc),
        metadata={"source_type": "json"},
        reader=JSONReader(),
        upsert=True,
    )

    agent = model.create_agent(
        name="Agno Multi Source Knowledge Agent",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请优先根据知识库内容回答问题。",
            "如果问题涉及课程安排或编号，请优先利用 JSON 资料。",
        ],
        markdown=True,
        # debug_mode=True,
    )

    print("\n--- 示例 1：从 Markdown 资料回答概念问题 ---")
    agent.print_response("Knowledge 和 Memory 的区别是什么？")

    print("\n--- 示例 2：从 JSON 资料回答课程规划问题 ---")
    agent.print_response("课程地图里第 4 课讲什么，学习目标是什么？")


if __name__ == "__main__":
    run_knowledge_multi_source_basics_example()
