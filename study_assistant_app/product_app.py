import os
from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import OpenAIModel

from .agents import build_research_agent
from .knowledge import build_study_knowledge
from .team import build_study_team
from .workflow_app import build_study_assistant_workflow_app


@dataclass
class StudyAssistantProductConfig:
    """统一管理最小产品骨架会用到的关键开关。"""

    enable_scheduler: bool = True
    enable_interfaces: bool = True
    enable_skills: bool = True
    enable_guardrails: bool = True
    enable_tracing: bool = False
    enable_mcp_docs: bool = False
    scheduler_timezone: str = "Asia/Shanghai"


def create_study_assistant_product_app(
    config: StudyAssistantProductConfig | None = None,
):
    """创建更接近最小产品形态的学习助手应用。"""
    runtime_config = config or StudyAssistantProductConfig()

    try:
        from agno.agent import Agent
        from agno.db.sqlite import SqliteDb
        from agno.os import AgentOS
        from agno.scheduler import ScheduleManager
        from agno.tools.scheduler import SchedulerTools
    except ImportError as exc:
        raise ImportError(
            "运行这一课前，请先安装 Runtime 依赖：`uv pip install -U \"agno[os]\" \"agno[scheduler]\" fastapi uvicorn`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    db_path = project_root / "tmp" / "study_assistant_product.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    db = SqliteDb(db_file=str(db_path))
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_study_knowledge()

    optional_status: dict[str, str] = {}
    product_tools: list[Any] = []
    product_pre_hooks: list[Any] = []
    product_skills = None

    if runtime_config.enable_skills:
        try:
            from agno.skills import LocalSkills, Skills

            skills_path = project_root / "examples" / "skills"
            product_skills = Skills(loaders=[LocalSkills(path=str(skills_path), validate=False)])
            optional_status["skills"] = f"enabled ({', '.join(product_skills.get_skill_names())})"
        except Exception as exc:
            optional_status["skills"] = f"unavailable ({exc})"
    else:
        optional_status["skills"] = "disabled by config"

    if runtime_config.enable_guardrails:
        try:
            from agno.guardrails import PIIDetectionGuardrail

            product_pre_hooks.append(PIIDetectionGuardrail(mask_pii=True))
            optional_status["guardrails"] = "enabled (PII masking)"
        except Exception as exc:
            optional_status["guardrails"] = f"unavailable ({exc})"
    else:
        optional_status["guardrails"] = "disabled by config"

    if runtime_config.enable_tracing:
        try:
            from agno.tracing import setup_tracing

            setup_tracing(db=db, batch_processing=False)
            optional_status["tracing"] = "enabled"
        except Exception as exc:
            optional_status["tracing"] = f"unavailable ({exc})"
    else:
        optional_status["tracing"] = "disabled by config"

    if runtime_config.enable_mcp_docs:
        try:
            from agno.tools.mcp import MCPTools

            product_tools.append(
                MCPTools(
                    transport="streamable-http",
                    url="https://docs.agno.com/mcp",
                    include_tools=["search_docs", "read_page"],
                )
            )
            optional_status["mcp_docs"] = "enabled (Agno docs MCP)"
        except Exception as exc:
            optional_status["mcp_docs"] = f"unavailable ({exc})"
    else:
        optional_status["mcp_docs"] = "disabled by config"

    research_agent = build_research_agent(model_wrapper, knowledge)
    study_team = build_study_team(model_wrapper, knowledge)
    workflow = build_study_assistant_workflow_app(model_wrapper)
    workflow_run_endpoint = f"/workflows/{workflow.id}/runs"

    product_coach_agent = Agent(
        id="study-assistant-product-coach",
        name="学习助手产品教练",
        model=model_wrapper.get_model(),
        db=db,
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        skills=product_skills,
        tools=product_tools,
        pre_hooks=product_pre_hooks or None,
        instructions=[
            "你是学习助手产品入口里的综合教练。",
            "请结合知识库、Skills 和安全策略回答学习路线问题。",
            "如果 MCP 文档工具可用，可以优先用它核对官方文档。",
        ],
        markdown=True,
        debug_mode=True,
    )

    scheduler_agent = Agent(
        id="study-assistant-product-scheduler",
        name="学习助手产品调度员",
        model=model_wrapper.get_model(),
        db=db,
        tools=[
            SchedulerTools(
                db=db,
                default_endpoint=workflow_run_endpoint,
                default_method="POST",
                default_timezone=runtime_config.scheduler_timezone,
            )
        ],
        instructions=[
            "你负责帮助用户管理学习助手产品里的调度任务。",
            "当用户表达定时执行需求时，请优先使用 SchedulerTools。",
        ],
        markdown=True,
        debug_mode=True,
    )

    interfaces = []
    interface_status: list[str] = []
    if runtime_config.enable_interfaces:
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
                interface_status.append("slack: credentials found, but package is unavailable")
        else:
            interface_status.append("slack: skipped (missing credentials)")
    else:
        interface_status.append("interfaces: disabled by config")

    @asynccontextmanager
    async def lifespan(app, agent_os=None):
        # 把之前分散的 Runtime 能力合在一起：
        # 一个统一 db、一个统一 workflow 入口，以及一个启动即存在的 schedule。
        if runtime_config.enable_scheduler:
            schedule_manager = ScheduleManager(db=db)
            schedule_manager.create(
                name="study_assistant_product_daily_digest",
                cron="0 9 * * 1-5",
                endpoint=workflow_run_endpoint,
                method="POST",
                description="工作日早上自动生成一条学习推进建议。",
                payload={"message": "请生成今天的学习推进建议，并提醒我当前最重要的下一步。"},
                timezone=runtime_config.scheduler_timezone,
                if_exists="update",
            )
        yield

    agent_os = AgentOS(
        name="study-assistant-product",
        agents=[research_agent, product_coach_agent, scheduler_agent],
        teams=[study_team],
        workflows=[workflow],
        db=db,
        interfaces=interfaces,
        scheduler=runtime_config.enable_scheduler,
        scheduler_poll_interval=15,
        lifespan=lifespan,
    )

    app = agent_os.get_app()

    @app.get("/study-assistant/product/health")
    async def product_health():
        """产品级健康检查。"""
        return {
            "status": "ok",
            "service": "study-assistant-product",
            "components": ["agent", "team", "workflow", "runtime", "skills", "guardrails", "tracing", "mcp"],
        }

    @app.get("/study-assistant/product/config")
    async def product_config():
        """暴露当前最小产品骨架的关键配置。"""
        return {
            "db_file": str(db_path),
            "workflow_run_endpoint": workflow_run_endpoint,
            "enable_scheduler": runtime_config.enable_scheduler,
            "enable_interfaces": runtime_config.enable_interfaces,
            "interfaces": interface_status,
            "optional_capabilities": optional_status,
            "timezone": runtime_config.scheduler_timezone,
        }

    return app
