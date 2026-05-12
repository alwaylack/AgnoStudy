"""MCP 基础示例。

演示 Agno 的 Model Context Protocol (MCP) 能力，包括：
1. MCPTools 的 streamable-http 配置
2. MCPTools 的 stdio 配置
3. include_tools / exclude_tools / refresh_connection 等常用参数
4. 显式 connect() / close() 的生命周期管理
5. AgentOS 中 MCPTools 生命周期由 AgentOS 接管的注意事项

默认运行不会连接远程 MCP 服务，避免在缺少 mcp 包、网络或模型配置时失败。
如需 live demo，请先安装依赖并设置 RUN_MCP_LIVE=1。
"""

import asyncio
import os
import sys
from pathlib import Path
from textwrap import dedent

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import OpenAIModel


AGNO_DOCS_MCP_URL = "https://docs.agno.com/mcp"


def print_mcp_configuration_examples() -> None:
    """打印官方推荐的几种 MCPTools 配置方式。"""
    print("\n--- Streamable HTTP MCP 服务 ---")
    print(
        dedent(
            f"""\
            MCPTools(
                transport="streamable-http",
                url="{AGNO_DOCS_MCP_URL}",
            )
            """
        )
    )

    print("\n--- 本地 stdio MCP 服务 ---")
    print(
        dedent(
            """\
            MCPTools(
                command="uvx mcp-server-git",
            )
            """
        )
    )

    print("\n--- 工具过滤与连接刷新 ---")
    print(
        dedent(
            """\
            MCPTools(
                transport="streamable-http",
                url="https://example.com/mcp",
                include_tools=["search_docs", "read_page"],
                refresh_connection=True,
            )
            """
        )
    )


def check_mcp_dependency() -> bool:
    """检查当前环境是否安装了 MCP Python 包。"""
    try:
        import mcp  # noqa: F401
    except ImportError:
        print("\n--- MCP 依赖检查 ---")
        print("当前环境没有安装 `mcp` 包。")
        print("如需运行 Agno MCPTools live demo，请先执行：")
        print("uv pip install mcp")
        return False

    print("\n--- MCP 依赖检查 ---")
    print("`mcp` 包已安装，可以运行 MCPTools live demo。")
    return True


async def run_live_mcp_docs_demo() -> None:
    """连接 Agno 官方文档 MCP 服务并让 Agent 调用 MCP tools。"""
    from agno.tools.mcp import MCPTools

    model = OpenAIModel.from_env()
    mcp_tools = MCPTools(
        transport="streamable-http",
        url=AGNO_DOCS_MCP_URL,
        include_tools=["search_docs", "read_page"],
    )

    await mcp_tools.connect()
    try:
        agent = model.create_agent(
            name="Agno MCP Docs Agent",
            tools=[mcp_tools],
            instructions=[
                "你是 Agno MCP 示例助教。",
                "请优先使用 MCP 工具查询官方文档，再回答用户问题。",
            ],
            markdown=True,
            debug_mode=True,
        )
        response = await agent.arun(
            "请用官方文档说明 Agno MCPTools 支持哪些 transport。",
            user_id="student@example.com",
            session_id="lesson_65_mcp_docs_demo",
            stream=False,
        )
        print("\n--- Live MCP Agent 响应 ---")
        print(response.content)
    finally:
        await mcp_tools.close()


def run_mcp_basics_example() -> None:
    """演示 Agno 的 MCP 基础能力。"""
    print_mcp_configuration_examples()
    mcp_available = check_mcp_dependency()

    if os.getenv("RUN_MCP_LIVE") == "1":
        if not mcp_available:
            print("\n已设置 RUN_MCP_LIVE=1，但缺少 `mcp` 包，跳过 live demo。")
        else:
            asyncio.run(run_live_mcp_docs_demo())
    else:
        print("\n--- Live demo 默认跳过 ---")
        print("设置 RUN_MCP_LIVE=1 后，本脚本会尝试连接 Agno 官方文档 MCP 服务。")

    print("\n--- 关键观察点 ---")
    print("1. MCP 是把外部系统的 tools / resources / prompts 标准化暴露给 Agent 的协议。")
    print("2. Agno 用 MCPTools 包装 MCP server，让 Agent 像调用普通工具一样调用 MCP 工具。")
    print("3. 官方推荐显式 await mcp_tools.connect()，并在 finally 中 await mcp_tools.close()。")
    print("4. transport 可用 stdio、streamable-http、sse；新服务优先考虑 streamable-http。")
    print("5. AgentOS 中 MCPTools 生命周期由 AgentOS 接管，但不要用 reload=True 破坏连接生命周期。")


if __name__ == "__main__":
    run_mcp_basics_example()
