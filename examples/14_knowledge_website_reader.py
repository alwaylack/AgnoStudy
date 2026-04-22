from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.website_reader import WebsiteReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def run_knowledge_website_reader_example() -> None:
    """演示如何使用 WebsiteReader 把网页内容接入 Knowledge。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb beautifulsoup4`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    vector_db_dir = project_root / "tmp" / "chromadb_website_reader"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_study_website_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_study_website_knowledge",
        vector_db=vector_db,
    )

    # 这里显式使用 WebsiteReader，演示如何抓取网页正文并写入 Knowledge。
    website_reader = WebsiteReader(
        max_depth=1,
        max_links=2,
        chunk_size=1200,
    )

    # 使用 Agno 官方文档页面作为学习资料来源。
    knowledge.insert(
        url="https://docs.agno.com/introduction",
        reader=website_reader,
        metadata={"source_type": "website", "site": "docs.agno.com"},
        upsert=True,
    )

    agent = model.create_agent(
        name="Agno Website Knowledge Agent",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请优先根据知识库中的网页资料回答问题。",
            "如果答案来自网页资料，请尽量保持表述贴近资料内容。",
        ],
        markdown=True,
        # debug_mode=True,
    )

    print("\n--- 示例 1：根据网页资料回答概念问题 ---")
    agent.print_response("Agno 是什么？它主要适合构建什么样的软件？")

    print("\n--- 示例 2：根据网页资料回答能力范围问题 ---")
    agent.print_response("根据知识库中的网页资料，Agno 可以构建哪些类型的系统？")


if __name__ == "__main__":
    run_knowledge_website_reader_example()
