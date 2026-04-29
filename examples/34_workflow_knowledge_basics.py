from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType
from agno.workflow import Step, Workflow

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_workflow_knowledge() -> Knowledge:
    """构建供 Workflow 示例使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_workflow_knowledge"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档：{document_path}")

    vector_db = ChromaDb(
        collection="agno_workflow_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_workflow_knowledge",
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


def run_workflow_knowledge_basics_example() -> None:
    """运行 Workflow + Knowledge 入门示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_workflow_knowledge()

    retrieval_agent = model_wrapper.create_agent(
        name="资料检索员",
        role="负责先从知识库中找到和问题最相关的资料。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请先根据用户问题检索知识库。",
            "输出时优先总结和当前问题最相关的知识点。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="知识规划员",
        role="负责基于检索结果给出下一阶段学习建议。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你会收到前面步骤检索出的关键知识点。",
            "请基于这些内容给出下一阶段学习建议。",
            "回答里要同时说明：当前最该理解什么，以及下一课适合学什么。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Workflow + Knowledge 基础课",
        description="学习如何让 Workflow 在某个阶段显式使用共享知识库。",
        steps=[
            Step(
                name="知识检索阶段",
                agent=retrieval_agent,
                description="先从知识库中检索和当前问题最相关的资料。",
            ),
            Step(
                name="知识规划阶段",
                agent=planning_agent,
                description="再基于检索结果生成下一阶段学习建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop、"
            "多模式组合课，以及 Workflow + Team。"
            "请基于知识库先检索当前最相关的学习重点，再给我下一阶段学习建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )


if __name__ == "__main__":
    run_workflow_knowledge_basics_example()
