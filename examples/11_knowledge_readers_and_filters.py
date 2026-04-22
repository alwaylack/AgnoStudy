from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def run_knowledge_readers_and_filters_example() -> None:
    """演示如何使用 Reader 导入多份文档，并通过 knowledge_filters 控制检索范围。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_multi_docs"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    tools_doc = knowledge_dir / "agno_tools_notes.md"
    memory_doc = knowledge_dir / "agno_memory_notes.md"

    for document_path in [tools_doc, memory_doc]:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_study_knowledge_multi_docs",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.vector,
    )

    knowledge = Knowledge(
        name="agno_study_knowledge_multi_docs",
        vector_db=vector_db,
    )

    # 显式使用 MarkdownReader，方便学习 Reader 在 Knowledge 中的作用。
    markdown_reader = MarkdownReader(chunk_size=1200)

    # 把多份文档写入同一个知识库，并通过 metadata 标记资料主题。
    knowledge.insert(
        path=str(tools_doc),
        metadata={"topic": "tools"},
        reader=markdown_reader,
        upsert=True,
    )
    knowledge.insert(
        path=str(memory_doc),
        metadata={"topic": "memory"},
        reader=markdown_reader,
        upsert=True,
    )

    tools_agent = model.create_agent(
        name="Agno Tools Knowledge Agent",
        knowledge=knowledge,
        # 只允许检索 topic=tools 的知识。
        knowledge_filters={"topic": "tools"},
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "你当前只能使用 tools 主题的知识库内容回答问题。",
        ],
        markdown=True,
        debug_mode=True,
    )

    memory_agent = model.create_agent(
        name="Agno Memory Knowledge Agent",
        knowledge=knowledge,
        # 只允许检索 topic=memory 的知识。
        knowledge_filters={"topic": "memory"},
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "你当前只能使用 memory 主题的知识库内容回答问题。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：只检索 Tools 主题资料 ---")
    tools_agent.print_response("请根据知识库说明 Agno 里的 Tools 有什么作用，以及初学者应该怎么开始学习。")

    print("\n--- 示例 2：只检索 Memory 主题资料 ---")
    memory_agent.print_response("请根据知识库说明 Agno 里的 Memory 更适合保存什么信息。")


if __name__ == "__main__":
    run_knowledge_readers_and_filters_example()
