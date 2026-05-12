# AgnoStudy

从零到一系统学习 [Agno](https://docs.agno.com/sdk/introduction) 框架的渐进式示例仓库。覆盖 Agent / Tools / Knowledge / Team / Workflow / Runtime 全部核心能力，以及官方 SDK 的 Advanced 和 Production 主线。

所有示例使用兼容 OpenAI 的三方模型（如 OpenRouter），通过统一封装 `models/openai_model.py` 接入。

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/AgnoStudy.git
cd AgnoStudy

# 2. 安装依赖
uv sync

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env，填入你的 API Key

# 4. 运行第一个示例
python examples/01_agent_basics.py
```

### 环境变量配置

在项目根目录创建 `.env`：

```env
OPENAI_BASE_URL="https://openrouter.ai/api/v1"
OPENAI_API_KEY="your-api-key"
OPENAI_MODEL_ID="openrouter/your-model"
OPENAI_EMBEDDING_MODEL_ID="your-embedding-model"
OPENAI_EMBEDDING_DIMENSIONS="1536"
```

### 可选依赖

```bash
# 网页搜索
uv pip install -U ddgs

# 向量数据库（RAG 示例需要）
uv pip install -U chromadb

# 文档处理
uv pip install -U beautifulsoup4 pypdf reportlab

# MCP 工具（第 65 课需要）
uv pip install mcp
```

## 学习路径

共 66 个示例，按 10 个阶段递进。每个示例聚焦单一能力，可独立运行。

### 第一阶段：Agent 基础（01-09）

> 创建 Agent、模型封装、工具使用、会话管理和记忆系统。

| # | 示例 | 核心能力 |
|---|------|----------|
| 01 | `01_agent_basics.py` | Agent 创建与基础对话 |
| 02 | `02_openai_compatible_agent.py` | OpenAI 兼容模型接入 |
| 03 | `03_learning_basics.py` | Learning 能力 |
| 04 | `04_tools_basics.py` | 工具注册与调用 |
| 05 | `05_structured_output.py` | 结构化输出 |
| 06 | `06_builtin_tools_duckduckgo.py` | 内置工具（DuckDuckGo） |
| 07 | `07_custom_toolkit.py` | 自定义 Toolkit |
| 08 | `08_sessions_history.py` | 会话历史 |
| 09 | `09_learning_machine_memory.py` | 学习记忆 |

### 第二阶段：Knowledge / RAG（10-18）

> 知识库构建、文档读取、向量检索和 RAG 调优。

| # | 示例 | 核心能力 |
|---|------|----------|
| 10 | `10_knowledge_rag_basics.py` | RAG 基础流程 |
| 11 | `11_knowledge_readers_and_filters.py` | 读取器与过滤器 |
| 12 | `12_rag_tuning_basics.py` | RAG 调优参数 |
| 13 | `13_knowledge_multi_source_basics.py` | 多数据源 |
| 14 | `14_knowledge_website_reader.py` | 网页读取器 |
| 15 | `15_knowledge_pdf_reader.py` | PDF 读取器 |
| 17 | `17_knowledge_website_deep_crawl.py` | 网站深度爬取 |
| 18 | `18_rag_filtering_advanced.py` | 高级过滤策略 |

### 第三阶段：Team / 多智能体（16-24）

> 多 Agent 协作的四种基础模式及其组合。

| # | 示例 | 核心能力 |
|---|------|----------|
| 16 | `16_team_coordinate_basics.py` | Coordinate 协调模式 |
| 19 | `19_team_route_basics.py` | Route 路由模式 |
| 20 | `20_team_broadcast_basics.py` | Broadcast 广播模式 |
| 21 | `21_team_tasks_basics.py` | Tasks 任务模式 |
| 22 | `22_team_shared_knowledge.py` | 团队共享知识 |
| 23 | `23_team_shared_tools.py` | 团队共享工具 |
| 24 | `24_team_tasks_with_knowledge.py` | Tasks + Knowledge 组合 |

### 第四阶段：集成与项目结构（25-26）

> 把 Agent / Team / Knowledge / Tools 组合成可维护的项目。

| # | 示例 | 核心能力 |
|---|------|----------|
| 25 | `25_integrated_app_skeleton.py` | 应用骨架 |
| 26 | `26_real_project_structure_basics.py` | 模块化项目结构 |

### 第五阶段：Workflow（27-45）

> 工作流系统：顺序、分组、条件、并行、循环等模式，以及与 Team / Knowledge 的集成。

| # | 示例 | 核心能力 |
|---|------|----------|
| 27 | `27_workflow_basics.py` | 基础顺序工作流 |
| 28 | `28_workflow_grouped_steps.py` | 分组步骤 |
| 29 | `29_workflow_condition_basics.py` | 条件分支 |
| 30 | `30_workflow_parallel_basics.py` | 并行执行 |
| 31 | `31_workflow_loop_basics.py` | 循环执行 |
| 32 | `32_workflow_multi_pattern_basics.py` | 多模式组合 |
| 33 | `33_workflow_team_basics.py` | Workflow + Team |
| 34 | `34_workflow_knowledge_basics.py` | Workflow + Knowledge |
| 35 | `35_workflow_team_knowledge_basics.py` | Workflow + Team + Knowledge |
| 36 | `36_learning_assistant_mini_workflow.py` | 真实项目小型工作流 |
| 37 | `37_study_assistant_workflow_app.py` | 应用骨架工作流 |
| 38 | `38_workflow_router_orchestration.py` | Router 路由编排 |
| 39 | `39_real_project_workflow_practice.py` | 真实项目长链路实践 |
| 40 | `40_long_chain_workflow_app.py` | 长链路应用骨架 |
| 41 | `41_workflow_sessions_basics.py` | Workflow Sessions |
| 42 | `42_runtime_serve_api_basics.py` | Runtime: Serve as API |
| 43 | `43_runtime_storage_interfaces_basics.py` | Runtime: Storage + Interfaces |
| 44 | `44_runtime_scheduling_basics.py` | Runtime: Scheduling |
| 45 | `45_product_app_basics.py` | 产品应用基础 |

### 第六阶段：SDK Introduction 对齐（46-48）

> 对齐官方 SDK Introduction 中的 Input & Output、Database、Session Management。

| # | 示例 | 核心能力 |
|---|------|----------|
| 46 | `46_input_output_basics.py` | 结构化输入输出 |
| 47 | `47_database_basics.py` | 数据库持久化 |
| 48 | `48_session_management_basics.py` | Session 管理 |

### 第七阶段：SDK Advanced 对齐（49-56）

> 对齐官方 SDK Advanced 中的 Context / State / Chat History / Dependency Injection / Hooks / Skills / Reasoning / Multimodal。

| # | 示例 | 核心能力 |
|---|------|----------|
| 49 | `49_context_management_basics.py` | 上下文管理与压缩 |
| 50 | `50_state_management_basics.py` | 状态管理（手动 + 自动） |
| 51 | `51_chat_history_basics.py` | 聊天历史读取与搜索 |
| 52 | `52_dependency_injection_basics.py` | 依赖注入 |
| 53 | `53_hooks_basics.py` | Pre/Post/Tool Hooks |
| 54 | `54_skills_basics.py` | Skills 加载（SKILL.md） |
| 55 | `55_reasoning_basics.py` | 显式推理 |
| 56 | `56_multimodal_basics.py` | 多模态输入（图片/文件） |

### 第八阶段：SDK Production 对齐（57-65）

> 对齐官方 SDK Production 中的 Guardrails / HITL / Evals / Tracing，以及 Context Compression、Run Cancellation、Background Execution、MCP。

| # | 示例 | 核心能力 |
|---|------|----------|
| 57 | `57_guardrails_basics.py` | PII 检测防护栏 |
| 58 | `58_human_in_the_loop_basics.py` | 人工介入（确认/输入/外部执行） |
| 59 | `59_evals_basics.py` | 准确性与性能评估 |
| 60 | `60_tracing_basics.py` | OpenTelemetry 追踪 |
| 61 | `61_official_plan_wrap_up.py` | 课程计划收尾检查 |
| 62 | `62_context_compression_basics.py` | 工具结果压缩 |
| 63 | `63_run_cancellation_basics.py` | 运行取消 |
| 64 | `64_background_execution_basics.py` | 后台异步执行 |
| 65 | `65_mcp_basics.py` | MCP 协议集成 |

### 第九阶段：产品化整合（66）

> 把所有能力整合回 `study_assistant_app`，通过配置开关渐进启用。

| # | 示例 | 核心能力 |
|---|------|----------|
| 66 | `66_product_app_capabilities.py` | Skills / Guardrails / Tracing / MCP 可选能力整合 |

## 项目结构

```
AgnoStudy/
├── examples/                          # 所有学习示例
│   ├── 01_agent_basics.py             # 第一阶段：Agent 基础
│   ├── ...
│   ├── 66_product_app_capabilities.py # 第九阶段：产品化整合
│   └── skills/                        # Skills 示例资源
│       └── agno_lesson_planner/
│           ├── SKILL.md
│           └── references/
├── models/                            # 模型层封装
│   ├── openai_model.py                # OpenAI 兼容模型接口
│   └── openai_embedder.py             # 嵌入模型接口
├── study_assistant_app/               # 产品化集成示例
│   ├── app.py                         # 应用入口
│   ├── product_app.py                 # 产品入口（含可选能力开关）
│   ├── knowledge.py                   # 知识库构建
│   ├── team.py                        # 团队配置
│   └── __init__.py
├── knowledge_docs/                    # RAG 示例使用的文档资源
├── contexts/                          # 学习进度跟踪
│   └── learning_progress.md
├── docs/
│   └── learning_handbook.md           # 深度学习手册（含每课详解）
├── tmp/                               # 运行时生成的临时文件
├── pyproject.toml
└── .env                               # 环境变量配置
```

## 模型层封装

所有示例通过 `models/openai_model.py` 统一接入模型，避免每个示例重复配置：

```python
from models import OpenAIModel

model = OpenAIModel.from_env()
agent = model.create_agent(
    name="My Agent",
    instructions=["你是一个有帮助的助手。"],
    markdown=True,
)
agent.print_response("你好！")
```

## 参考文档

- [Agno SDK Introduction](https://docs.agno.com/sdk/introduction)
- [Agno Sessions Overview](https://docs.agno.com/sessions/overview)
- [Agno Runtime Overview](https://docs.agno.com/runtime/overview)
- [Agno Context Management](https://docs.agno.com/context/overview)
- [Agno Chat History](https://docs.agno.com/database/chat-history)
- [Agno Dependency Injection](https://docs.agno.com/context/dependencies/overview)
- [Agno Hooks](https://docs.agno.com/hooks/overview)
- [Agno Skills](https://docs.agno.com/skills/overview)
- [Agno Reasoning](https://docs.agno.com/reasoning/overview)
- [Agno Multimodal](https://docs.agno.com/multimodal/overview)
- [Agno Guardrails](https://docs.agno.com/guardrails/overview)
- [Agno Human in the Loop](https://docs.agno.com/hitl/overview)
- [Agno Evals](https://docs.agno.com/evals/overview)
- [Agno Tracing](https://docs.agno.com/tracing/overview)
- [Agno Context Compression](https://docs.agno.com/context/compression/overview)
- [Agno Run Cancellation](https://docs.agno.com/runtime/cancellation)
- [Agno Background Execution](https://docs.agno.com/runtime/background)
- [Agno MCP](https://docs.agno.com/mcp)

## 版本说明

- Agno 版本：`2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`，统一使用 `debug_mode=True`
- 深度学习手册和课程进度跟踪见 [docs/learning_handbook.md](docs/learning_handbook.md)
