from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder

from .settings import KNOWLEDGE_FILES, TMP_DIR


def build_study_knowledge() -> Knowledge:
    """构建学习助手共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这一课前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    for document_path in KNOWLEDGE_FILES:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档：{document_path}")

    vector_db_dir = TMP_DIR / "chromadb_study_assistant_app"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    vector_db = ChromaDb(
        collection="agno_study_assistant_app",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_study_assistant_knowledge",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in KNOWLEDGE_FILES:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge
