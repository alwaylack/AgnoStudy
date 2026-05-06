import os
from pathlib import Path

from models import OpenAIModel

from .agents import build_research_agent
from .knowledge import build_study_knowledge
from .team import build_study_team
from .workflow_app import build_study_assistant_workflow_app


def create_study_assistant_runtime_storage_interfaces_app():
    """创建带统一存储和条件接口注册的 AgentOS Runtime 应用。"""
    try:
        from agno.db.sqlite import SqliteDb
        from agno.os import AgentOS
    except ImportError as exc:
        raise ImportError(
            "运行这一课前，请先安装 Runtime 依赖：`uv pip install -U \"agno[os]\" fastapi uvicorn`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "study_assistant_runtime_interfaces.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model_wrapper = OpenAIModel.from_env()
    knowledge = build_study_knowledge()

    research_agent = build_research_agent(model_wrapper, knowledge)
    study_team = build_study_team(model_wrapper, knowledge)
    workflow = build_study_assistant_workflow_app(model_wrapper)

    db = SqliteDb(db_file=str(db_path))
    interfaces = []
    interface_status: list[str] = []

    # 这一课优先演示“条件注册”这个思路：
    # 有凭据就挂接口，没有凭据也不影响本地开发启动。
    slack_token = os.getenv("AGNO_SLACK_BOT_TOKEN")
    slack_signing_secret = os.getenv("AGNO_SLACK_SIGNING_SECRET")

    if slack_token and slack_signing_secret:
        try:
            from agno.os.interfaces.slack import Slack

            interfaces.append(
                Slack(
                    agent=research_agent,
                    token=slack_token,
                    signing_secret=slack_signing_secret,
                )
            )
            interface_status.append("slack: enabled")
        except ImportError:
            interface_status.append("slack: credentials found, but Slack interface package is unavailable")
    else:
        interface_status.append("slack: skipped (missing credentials)")

    try:
        from agno.os.interfaces.agui import AGUI

        interfaces.append(AGUI(agent=research_agent))
        interface_status.append("agui: enabled")
    except ImportError:
        interface_status.append("agui: unavailable in current install")

    agent_os = AgentOS(
        agents=[research_agent],
        teams=[study_team],
        workflows=[workflow],
        db=db,
        interfaces=interfaces,
    )

    app = agent_os.get_app()

    @app.get("/study-assistant/runtime/overview")
    async def runtime_overview():
        """用一个自定义路由解释 Runtime 的存储和接口配置。"""
        return {
            "status": "ok",
            "db_backend": "sqlite",
            "db_file": str(db_path),
            "registered_interfaces": interface_status,
            "components": ["agent", "team", "workflow"],
        }

    @app.post("/study-assistant/webhooks/lesson-note")
    async def lesson_note_webhook(payload: dict):
        """演示官方文档提到的 one-off webhook 集成方式。"""
        note = payload.get("note", "")
        lesson = payload.get("lesson", "unknown")
        response = await research_agent.arun(
            f"请基于这条课程笔记做一个简短总结。课程：{lesson}。笔记：{note}",
            user_id="webhook-system",
            session_id=f"lesson-note-{lesson}",
        )
        return {
            "ok": True,
            "lesson": lesson,
            "summary": response.content,
        }

    return app
