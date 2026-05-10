# Agno 学习进度记录

更新时间：2026-05-10

## 当前停课点

当前最新完成课程：

- [examples/41_workflow_sessions_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\41_workflow_sessions_basics.py:1)
- [examples/42_runtime_serve_api_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\42_runtime_serve_api_basics.py:1)
- [examples/43_runtime_storage_interfaces_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\43_runtime_storage_interfaces_basics.py:1)
- [examples/44_runtime_scheduling_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\44_runtime_scheduling_basics.py:1)
- [examples/45_product_app_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\45_product_app_basics.py:1)
- [examples/46_input_output_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\46_input_output_basics.py:1)
- [examples/47_database_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\47_database_basics.py:1)
- [examples/48_session_management_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\48_session_management_basics.py:1)

## 当前学习阶段

目前已经完成以下主线内容：

- Agent 基础与兼容 OpenAI 模型封装
- Tools 基础、内置工具、自定义 Toolkit
- Session / History / Learning / Memory
- Knowledge / RAG / Readers / 多数据源 / 检索调优
- Team 四种基础模式与组合课
- 项目骨架与 Workflow 基础、组合模式、长链路整合
- Workflow Sessions
- Runtime: Serve as API
- Runtime: Storage + Interfaces
- Scheduling
- 回到更完整的小项目升级
- 官方 SDK Introduction: Input & Output
- 官方 SDK Introduction: Database
- 官方 SDK Introduction: Session Management

## 已完成课程

### 第一阶段：基础能力

- `01_agent_basics.py`
- `02_openai_compatible_agent.py`
- `03_learning_basics.py`
- `04_tools_basics.py`
- `05_structured_output.py`
- `06_builtin_tools_duckduckgo.py`
- `07_custom_toolkit.py`
- `08_sessions_history.py`
- `09_learning_machine_memory.py`

### 第二阶段：Knowledge / RAG

- `10_knowledge_rag_basics.py`
- `11_knowledge_readers_and_filters.py`
- `12_rag_tuning_basics.py`
- `13_knowledge_multi_source_basics.py`
- `14_knowledge_website_reader.py`
- `15_knowledge_pdf_reader.py`
- `17_knowledge_website_deep_crawl.py`
- `18_rag_filtering_advanced.py`

### 第三阶段：Team / Multi-Agent

- `16_team_coordinate_basics.py`
- `19_team_route_basics.py`
- `20_team_broadcast_basics.py`
- `21_team_tasks_basics.py`
- `22_team_shared_knowledge.py`
- `23_team_shared_tools.py`
- `24_team_tasks_with_knowledge.py`

### 第四阶段：项目骨架 / Workflow / Runtime

- `25_integrated_app_skeleton.py`
- `26_real_project_structure_basics.py`
- `27_workflow_basics.py`
- `28_workflow_grouped_steps.py`
- `29_workflow_condition_basics.py`
- `30_workflow_parallel_basics.py`
- `31_workflow_loop_basics.py`
- `32_workflow_multi_pattern_basics.py`
- `33_workflow_team_basics.py`
- `34_workflow_knowledge_basics.py`
- `35_workflow_team_knowledge_basics.py`
- `36_learning_assistant_mini_workflow.py`
- `37_study_assistant_workflow_app.py`
- `38_workflow_router_orchestration.py`
- `39_real_project_workflow_practice.py`
- `40_long_chain_workflow_app.py`
- `41_workflow_sessions_basics.py`
- `42_runtime_serve_api_basics.py`
- `43_runtime_storage_interfaces_basics.py`
- `44_runtime_scheduling_basics.py`
- `45_product_app_basics.py`

### 第五阶段：官方 SDK Introduction 对齐补课

- `46_input_output_basics.py`
- `47_database_basics.py`
- `48_session_management_basics.py`

## 当前已经掌握的重点

- 能用统一封装接入兼容 OpenAI 的三方模型与嵌入模型
- 能注册普通函数工具、内置工具、自定义 Toolkit
- 能区分 `learning`、`history`、`session`、`memory` 的使用场景
- 能构建 Knowledge，接入 Reader，做过滤检索与基础调优
- 能理解 Team 的 `coordinate / route / broadcast / tasks` 四种模式
- 能把 `Workflow / Team / Knowledge` 组合到同一个长链路应用里
- 能给 Workflow 接上 `SqliteDb`、`session_id`、`workflow history` 与 `session_state`
- 能用 `AgentOS` 把 agent / team / workflow 暴露成 FastAPI 服务
- 能理解 Runtime 的统一存储、条件接口注册和 webhook 接入
- 能理解 `ScheduleManager` 与 `SchedulerTools` 的基本调度方式
- 能把 Runtime 能力收拢到 [study_assistant_app/product_app.py](C:\Users\lenovo\Desktop\AgnoStudy\study_assistant_app\product_app.py:1) 这样的统一产品入口里
- 能用 `input_schema / expected_output / output_schema / save_response_to_file` 组织一节完整的 Input & Output 示例
- 能显式创建 `SqliteDb`，并用 `get_session / get_sessions` 观察 Agno 的数据库持久化结果
- 能主动管理 session 的名字、状态、消息与整体记录

## 根据官方 SDK Introduction 调整后的计划

我已经按官方 [SDK Introduction](https://docs.agno.com/sdk/introduction) 重新校准了后续课程顺序。

官方现在更清晰地分成三段：

### Basics

- Agents
- Teams
- Workflows
- Input & Output
- Database
- Memory
- Knowledge
- Learning
- Models
- Tools

### Advanced

- Session Management
- Context Management
- State Management
- Chat History
- Dependency Injection
- Hooks
- Skills
- Reasoning
- Multimodal

### Production

- Guardrails
- Human in the Loop
- Evals
- Tracing
- Scheduler

## 我们当前和官方的差异

已经系统学过的部分：

- Agents
- Teams
- Workflows
- Memory / Learning
- Knowledge
- Models
- Tools
- Scheduler
- Input & Output
- Database
- Session Management

还没有按官方目录系统补齐的部分：

- Context / State / Chat History
- Dependency Injection / Hooks
- Skills / Reasoning / Multimodal
- Guardrails / Human in the Loop / Evals / Tracing

## 下一课安排

后续课程顺序调整为：

1. `Context Management`
2. `State Management`
3. `Chat History`
4. `Dependency Injection`
5. `Hooks`
6. `Skills`
7. `Reasoning`
8. `Multimodal`
9. `Guardrails`
10. `Human in the Loop`
11. `Evals`
12. `Tracing`
13. 最后再回到 `study_assistant_app` 做更完整的产品化整理

如果只看最近三节课，建议就是：

1. `Context Management`
2. `State Management`
3. `Chat History`

## 下次开始时建议先看

- [examples/48_session_management_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\48_session_management_basics.py:1)
- [examples/41_workflow_sessions_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\41_workflow_sessions_basics.py:1)
- [README.md](C:\Users\lenovo\Desktop\AgnoStudy\README.md:1)

## 版本与运行注意事项

- 当前本地版本是 `agno 2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`，统一使用 `debug_mode=True`
- 第 44 课已经按 `2.5.17` 改成使用 `ScheduleManager`
- Runtime 相关课程需要 `agno[os]`、`agno[scheduler]`、`fastapi`、`uvicorn`
- 第 46 课使用的 `input_schema / output_schema / save_response_to_file` 已确认在 `2.5.17` 可用
- 第 47 课使用的 `SqliteDb / get_session / get_sessions` 已确认在 `2.5.17` 可用
- 第 48 课使用的 `set_session_name / update_session_state / get_session_state / get_session_messages` 已确认在 `2.5.17` 可用

## 参考文档

- [Agno SDK Introduction](https://docs.agno.com/sdk/introduction)
- [Agno Sessions Overview](https://docs.agno.com/sessions/overview)
- [Agno Runtime Overview](https://docs.agno.com/runtime/overview)
