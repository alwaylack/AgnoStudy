from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def run_knowledge_pdf_reader_example() -> None:
    """演示如何使用 PDFReader 把 PDF 文档接入 Knowledge。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb pypdf reportlab`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    pdf_path = project_root / "output" / "pdf" / "agno_knowledge_sample.pdf"
    vector_db_dir = project_root / "tmp" / "chromadb_pdf_reader"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    if not pdf_path.exists():
        raise FileNotFoundError(
            "没有找到示例 PDF。请先运行：`python scripts/generate_knowledge_sample_pdf.py`"
        )

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_study_pdf_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_study_pdf_knowledge",
        vector_db=vector_db,
    )

    pdf_reader = PDFReader(chunk_size=1200)

    knowledge.insert(
        path=str(pdf_path),
        reader=pdf_reader,
        metadata={"source_type": "pdf"},
        upsert=True,
    )

    agent = model.create_agent(
        name="Agno PDF Knowledge Agent",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请优先根据 PDF 知识资料回答问题。",
            "如果答案来自 PDF 内容，请尽量贴近文档表述。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：根据 PDF 资料回答概念问题 ---")
    agent.print_response("Knowledge、Memory、Tools 三者分别更关注什么？")

    print("\n--- 示例 2：根据 PDF 资料回答学习建议问题 ---")
    agent.print_response("PDF 资料里给出的 Agno 学习建议有哪些？")


if __name__ == "__main__":
    run_knowledge_pdf_reader_example()
