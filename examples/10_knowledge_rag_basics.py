from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def run_knowledge_rag_basics_example() -> None:
    """演示如何使用本地文档构建最小可运行的 Agno Knowledge / RAG 示例。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    # 基于当前脚本位置反推项目根目录，避免受执行时工作目录影响。
    project_root = Path(__file__).resolve().parents[1]
    document_path = project_root / "knowledge_docs" / "agno_rag_basics.md"
    vector_db_dir = project_root / "tmp" / "chromadb"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    if not document_path.exists():
        raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    # 这里使用本地持久化 Chroma，适合作为知识库入门示例。
    vector_db = ChromaDb(
        collection="agno_study_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.vector,
    )

    knowledge = Knowledge(
        name="agno_study_knowledge",
        vector_db=vector_db,
    )

    # 首次运行时把本地资料写入知识库。
    knowledge.insert(
        path=str(document_path),
        upsert=True,
    )

    agent = model.create_agent(
        name="Agno Knowledge Agent",
        knowledge=knowledge,
        # 让 Agent 在回答问题时自动搜索知识库。
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请优先根据知识库中的内容回答问题。",
            "如果知识库中没有答案，再明确说明资料中未提到。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：询问 Knowledge 的作用 ---")
    agent.print_response("Agno 里的 Knowledge 更关注什么？它和 Memory 有什么区别？")

    print("\n--- 示例 2：询问 RAG 的基本流程 ---")
    agent.print_response("请根据知识库内容总结 Agno 中 RAG 的基本流程。")


if __name__ == "__main__":
    run_knowledge_rag_basics_example()
