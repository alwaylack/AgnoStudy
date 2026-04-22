from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.website_reader import WebsiteReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def run_knowledge_website_deep_crawl_example() -> None:
    """演示如何使用 WebsiteReader 进行更深入的网站抓取。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb beautifulsoup4`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    vector_db_dir = project_root / "tmp" / "chromadb_website_deep_crawl"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_study_website_deep_crawl",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_study_website_deep_crawl",
        vector_db=vector_db,
    )

    # 相比上一课，这里提高 max_depth 和 max_links，让抓取覆盖多个相关页面。
    website_reader = WebsiteReader(
        max_depth=2,
        max_links=6,
        chunk_size=1200,
    )

    knowledge.insert(
        url="https://docs.agno.com/introduction",
        reader=website_reader,
        metadata={"source_type": "website", "crawl_mode": "deep"},
        upsert=True,
    )

    agent = model.create_agent(
        name="Agno Deep Crawl Agent",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请优先根据深度抓取到的网页知识库回答问题。",
            "如果回答中涉及多个能力模块，请尽量整合知识库中不同页面的信息。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：使用深度抓取后的知识库回答综合问题 ---")
    agent.print_response("请综合知识库内容，说明 Agno 主要适合构建哪些类型的软件系统。")

    print("\n--- 示例 2：观察深度抓取后对回答覆盖面的帮助 ---")
    agent.print_response("请根据知识库内容，概括 Agno 在 Agent、Knowledge 和 Tools 这几个方向上的能力范围。")


if __name__ == "__main__":
    run_knowledge_website_deep_crawl_example()
