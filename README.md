# AgnoStudy

这是一个按学习节奏逐步搭建的 Agno 学习项目，目标有两件事：

1. 从 Agno 官方核心能力开始，系统学习 `Agent / Tools / Knowledge / Team / Workflow / Runtime`
2. 保留一套适合兼容 OpenAI 三方模型的本地封装方式，方便你边学边改

## 当前状态

当前最新课程：

- [examples/44_runtime_scheduling_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\44_runtime_scheduling_basics.py:1)

当前最适合的下一课：

- `回到更完整的小项目升级`

当前主线已经覆盖到：

- Agent / Tools / Knowledge / Team
- Workflow 基础与组合模式
- Workflow Sessions
- Runtime: Serve as API
- Runtime: Storage + Interfaces
- Scheduling

## 学习主线

### 1. 基础 Agent 与模型封装

- [examples/01_agent_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\01_agent_basics.py:1)
- [examples/02_openai_compatible_agent.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\02_openai_compatible_agent.py:1)
- [models/openai_model.py](C:\Users\lenovo\Desktop\AgnoStudy\models\openai_model.py:1)

### 2. Learning / Memory / Session

- [examples/03_learning_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\03_learning_basics.py:1)
- [examples/08_sessions_history.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\08_sessions_history.py:1)
- [examples/09_learning_machine_memory.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\09_learning_machine_memory.py:1)

### 3. Tools

- [examples/04_tools_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\04_tools_basics.py:1)
- [examples/06_builtin_tools_duckduckgo.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\06_builtin_tools_duckduckgo.py:1)
- [examples/07_custom_toolkit.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\07_custom_toolkit.py:1)

### 4. Knowledge / RAG

- [examples/10_knowledge_rag_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\10_knowledge_rag_basics.py:1)
- [examples/11_knowledge_readers_and_filters.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\11_knowledge_readers_and_filters.py:1)
- [examples/12_rag_tuning_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\12_rag_tuning_basics.py:1)
- [examples/13_knowledge_multi_source_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\13_knowledge_multi_source_basics.py:1)
- [examples/14_knowledge_website_reader.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\14_knowledge_website_reader.py:1)
- [examples/15_knowledge_pdf_reader.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\15_knowledge_pdf_reader.py:1)
- [examples/17_knowledge_website_deep_crawl.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\17_knowledge_website_deep_crawl.py:1)
- [examples/18_rag_filtering_advanced.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\18_rag_filtering_advanced.py:1)
- [models/openai_embedder.py](C:\Users\lenovo\Desktop\AgnoStudy\models\openai_embedder.py:1)

### 5. Team / Multi-Agent

- [examples/16_team_coordinate_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\16_team_coordinate_basics.py:1)
- [examples/19_team_route_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\19_team_route_basics.py:1)
- [examples/20_team_broadcast_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\20_team_broadcast_basics.py:1)
- [examples/21_team_tasks_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\21_team_tasks_basics.py:1)
- [examples/22_team_shared_knowledge.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\22_team_shared_knowledge.py:1)
- [examples/23_team_shared_tools.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\23_team_shared_tools.py:1)
- [examples/24_team_tasks_with_knowledge.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\24_team_tasks_with_knowledge.py:1)

### 6. 阶段整合与项目骨架

- [examples/25_integrated_app_skeleton.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\25_integrated_app_skeleton.py:1)
- [examples/26_real_project_structure_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\26_real_project_structure_basics.py:1)
- [study_assistant_app](C:\Users\lenovo\Desktop\AgnoStudy\study_assistant_app)

### 7. Workflow

- [examples/27_workflow_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\27_workflow_basics.py:1)
- [examples/28_workflow_grouped_steps.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\28_workflow_grouped_steps.py:1)
- [examples/29_workflow_condition_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\29_workflow_condition_basics.py:1)
- [examples/30_workflow_parallel_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\30_workflow_parallel_basics.py:1)
- [examples/31_workflow_loop_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\31_workflow_loop_basics.py:1)
- [examples/32_workflow_multi_pattern_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\32_workflow_multi_pattern_basics.py:1)
- [examples/33_workflow_team_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\33_workflow_team_basics.py:1)
- [examples/34_workflow_knowledge_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\34_workflow_knowledge_basics.py:1)
- [examples/35_workflow_team_knowledge_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\35_workflow_team_knowledge_basics.py:1)
- [examples/36_learning_assistant_mini_workflow.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\36_learning_assistant_mini_workflow.py:1)
- [examples/37_study_assistant_workflow_app.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\37_study_assistant_workflow_app.py:1)
- [examples/38_workflow_router_orchestration.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\38_workflow_router_orchestration.py:1)
- [examples/39_real_project_workflow_practice.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\39_real_project_workflow_practice.py:1)
- [examples/40_long_chain_workflow_app.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\40_long_chain_workflow_app.py:1)
- [examples/41_workflow_sessions_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\41_workflow_sessions_basics.py:1)

### 8. Runtime

- [examples/42_runtime_serve_api_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\42_runtime_serve_api_basics.py:1)
- [examples/43_runtime_storage_interfaces_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\43_runtime_storage_interfaces_basics.py:1)
- [examples/44_runtime_scheduling_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\44_runtime_scheduling_basics.py:1)

## 重点课程说明

### 第 41 课：Workflow Sessions

重点学习：

- 给 `Workflow` 接上 `SqliteDb`
- 开启 `add_workflow_history_to_steps=True`
- 通过 `session_id` 复用同一个 Workflow 会话
- 用 `session_state` 在多次运行之间共享状态

### 第 42 课：Runtime / Serve as API

重点学习：

- 用 `AgentOS` 把现有 `agent / team / workflow` 暴露成服务
- 通过 `agent_os.get_app()` 得到 FastAPI 应用
- 理解 AgentOS 自动生成运行接口的思路

### 第 43 课：Runtime / Storage + Interfaces

重点学习：

- 用统一的 `db` 承载 Runtime 状态
- 用“有凭据就注册，没有凭据就跳过”的方式演示接口接入
- 用自定义 webhook 理解 one-off integration

### 第 44 课：Scheduling

重点学习：

- 在 `AgentOS` 中开启 `scheduler=True`
- 用 `ScheduleManager` 做启动即存在的 schedule 注册
- 用 `SchedulerTools` 演示 agent-driven scheduling
- 理解调度最终命中的仍然是 agent / workflow 运行端点

## 环境变量

在项目根目录准备 `.env`：

```env
OPENAI_BASE_URL="https://openrouter.ai/api/v1"
OPENAI_API_KEY="your-api-key"
OPENAI_MODEL_ID="openrouter/your-model"
OPENAI_EMBEDDING_MODEL_ID="your-embedding-model"
OPENAI_EMBEDDING_DIMENSIONS="1536"
```

如果你要体验 Runtime 接口能力，还可能会用到：

```env
AGNO_SLACK_BOT_TOKEN=""
AGNO_SLACK_SIGNING_SECRET=""
```

## 安装依赖

如果使用 `uv`：

```bash
uv sync
```

如果使用 `pip`：

```bash
pip install -e .
```

按能力补充的常见安装命令：

```bash
uv pip install -U ddgs
uv pip install -U chromadb
uv pip install -U beautifulsoup4
uv pip install -U pypdf reportlab
uv pip install -U "agno[os]" fastapi uvicorn
uv pip install -U "agno[scheduler]"
```

## 运行方式

### 基础 Workflow 课程

```bash
python examples/27_workflow_basics.py
python examples/28_workflow_grouped_steps.py
python examples/29_workflow_condition_basics.py
python examples/30_workflow_parallel_basics.py
python examples/31_workflow_loop_basics.py
python examples/32_workflow_multi_pattern_basics.py
python examples/33_workflow_team_basics.py
python examples/34_workflow_knowledge_basics.py
python examples/35_workflow_team_knowledge_basics.py
python examples/36_learning_assistant_mini_workflow.py
python examples/37_study_assistant_workflow_app.py
python examples/38_workflow_router_orchestration.py
python examples/39_real_project_workflow_practice.py
python examples/40_long_chain_workflow_app.py
python examples/41_workflow_sessions_basics.py
```

### Runtime 课程

先看说明：

```bash
python examples/42_runtime_serve_api_basics.py
python examples/43_runtime_storage_interfaces_basics.py
python examples/44_runtime_scheduling_basics.py
```

真正启动服务时用：

```bash
fastapi dev examples/42_runtime_serve_api_basics.py
fastapi dev examples/43_runtime_storage_interfaces_basics.py
fastapi dev examples/44_runtime_scheduling_basics.py
```

### 回顾项目骨架

```bash
python examples/25_integrated_app_skeleton.py
python examples/26_real_project_structure_basics.py
```

## 当前版本注意事项

- 当前本地版本是 `agno 2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`
- 当前项目统一使用 `debug_mode=True`
- 第 44 课已经按 `2.5.17` 改成使用 `ScheduleManager`，不再依赖不存在的 `register_schedule`

## 下一阶段建议

下一阶段建议进入“回到更完整的小项目升级”，原因是：

- 你已经把 SDK 主线学到了 `Workflow`
- 你已经补了 `Workflow Sessions`
- 你已经补了 `Runtime: Serve as API`
- 你已经补了 `Runtime: Storage + Interfaces`
- 你已经补了 `Scheduling`
- 现在更适合把这些 Runtime 能力重新接回一个更完整的小项目结构

推荐接下来的学习顺序：

1. 回到更完整的小项目升级
2. 再补一层更清晰的模块职责和运行入口
3. 最后再做更复杂的工程化整理

## 官方文档方向

- [Agno 首页](https://docs.agno.com/)
- [Agno Sessions Overview](https://docs.agno.com/sessions/overview)
- [Agno Workflows Overview](https://docs.agno.com/workflows/overview)
- [Agno Runtime Overview](https://docs.agno.com/runtime/overview)
- [Agno Scheduling](https://docs.agno.com/runtime/scheduling)
