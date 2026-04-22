from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType

from models import OpenAICompatibleEmbedder, OpenAIModel


def build_team_tasks_knowledge() -> Knowledge:
    """构建供任务型 Team 使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_team_tasks_knowledge"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
        knowledge_dir / "agno_tools_notes.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_team_tasks_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_team_tasks_knowledge",
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


def run_team_tasks_with_knowledge_example() -> None:
    """演示如何让任务型 Team 基于共享 Knowledge 执行任务。"""
    model = OpenAIModel.from_env()
    knowledge = build_team_tasks_knowledge()

    research_agent = model.create_agent(
        name="知识研究专家",
        role="负责从知识库中提取与学习目标相关的信息",
        instructions=[
            "你擅长从资料中提取关键知识点。",
            "请尽量基于知识库内容进行总结。",
        ],
        markdown=True,
    )

    planning_agent = model.create_agent(
        name="计划设计专家",
        role="负责把研究结果整理成可执行计划",
        instructions=[
            "你擅长把信息整理成可执行的学习计划。",
            "请优先输出清晰的小步执行方案。",
        ],
        markdown=True,
    )

    review_agent = model.create_agent(
        name="复盘审查专家",
        role="负责检查最终计划是否完整合理",
        instructions=[
            "你擅长检查方案是否完整。",
            "请指出遗漏点，并补充更稳妥的建议。",
        ],
        markdown=True,
    )

    # 这一课把 TeamMode.tasks 和共享 Knowledge 结合起来，
    # 更接近真实项目中的协作执行流程。
    team = Team(
        name="Agno 任务知识团队",
        mode=TeamMode.tasks,
        model=model.get_model(),
        members=[research_agent, planning_agent, review_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是任务型团队领导者。",
            "请先基于共享知识库理解任务背景，再拆解任务并分配给合适成员。",
            "请在所有任务完成后，再统一输出最终计划。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
        max_iterations=8,
    )

    team.print_response(
        "请基于共享知识库，为我制定一个接下来的 Agno 学习执行计划，重点覆盖 Team 组合能力和更复杂的真实项目用法。"
    )


if __name__ == "__main__":
    run_team_tasks_with_knowledge_example()
