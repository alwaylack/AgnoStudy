# AgnoStudy

这是一个按学习节奏逐步搭建的 Agno 学习项目，目标有两件事：

1. 从 Agno 官方核心能力开始，系统学习 `Agent / Tools / Knowledge / Team / Workflow / Runtime`
2. 保留一套适合兼容 OpenAI 三方模型的本地封装方式，方便边学边改、边学边跑

## 当前状态

当前最新课程：

- [examples/47_database_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\47_database_basics.py:1)

当前最适合的下一课：

- `Session Management`

当前主线已经覆盖到：

- Agents / Tools / Knowledge / Teams
- Workflow 基础、组合模式与长链路整合
- Workflow Sessions
- Runtime: Serve as API / Storage + Interfaces / Scheduling
- 回到更完整的小项目升级
- 官方 SDK Introduction: Input & Output / Database

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

### 6. 项目骨架 / Workflow / Runtime

- [examples/25_integrated_app_skeleton.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\25_integrated_app_skeleton.py:1)
- [examples/26_real_project_structure_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\26_real_project_structure_basics.py:1)
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
- [examples/42_runtime_serve_api_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\42_runtime_serve_api_basics.py:1)
- [examples/43_runtime_storage_interfaces_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\43_runtime_storage_interfaces_basics.py:1)
- [examples/44_runtime_scheduling_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\44_runtime_scheduling_basics.py:1)
- [examples/45_product_app_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\45_product_app_basics.py:1)

### 7. 官方 SDK Introduction 对齐补课线

- [examples/46_input_output_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\46_input_output_basics.py:1)
- [examples/47_database_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\47_database_basics.py:1)

## 第 47 课：Database

这一课对齐官方 [SDK Introduction](https://docs.agno.com/sdk/introduction) 里的 `Database`。

重点学习：

- 显式创建 `SqliteDb`
- 把 `db` 传给 Agent，而不是只在别的课程里顺带使用
- 用 `get_session()` 读取当前 session 的持久化结果
- 用 `get_sessions()` 查看数据库里已经保存的 session 列表

运行方式：

```bash
python examples/47_database_basics.py
```

这节课会输出数据库文件路径，默认保存在：

- [lesson_47_database.db](C:\Users\lenovo\Desktop\AgnoStudy\tmp\lesson_47_database.db:1)

## 官方 SDK Introduction 对齐后的下一阶段计划

根据官方 [SDK Introduction](https://docs.agno.com/sdk/introduction)，Agno SDK 当前更清晰地分成三层学习路径：

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

还没有按官方目录系统补齐的部分：

- Session Management 的更细分能力
- Context / State / Chat History
- Dependency Injection / Hooks
- Skills / Reasoning / Multimodal
- Guardrails / Human in the Loop / Evals / Tracing

## 接下来更合适的课程顺序

下一阶段建议改成下面这条线：

1. `Session Management`
2. `Context Management`
3. `State Management`
4. `Chat History`
5. `Dependency Injection`
6. `Hooks`
7. `Skills`
8. `Reasoning`
9. `Multimodal`
10. `Guardrails`
11. `Human in the Loop`
12. `Evals`
13. `Tracing`
14. 最后再回到 `study_assistant_app` 做更完整的产品化整理

如果按最近三节课来排，推荐就是：

1. `Session Management`
2. `Context Management`
3. `State Management`

## 当前版本注意事项

- 当前本地版本是 `agno 2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`
- 当前项目统一使用 `debug_mode=True`
- 第 44 课已经按 `2.5.17` 改成使用 `ScheduleManager`
- 第 45 课继续沿用 `2.5.17` 兼容写法，把 `ScheduleManager`、`SchedulerTools` 和 `AgentOS` 统一收拢到产品入口
- 第 46 课使用 `input_schema / output_schema / save_response_to_file`
- 第 47 课使用 `SqliteDb / get_session / get_sessions`，这些接口已确认在 `2.5.17` 可用

## 参考文档

- [Agno SDK Introduction](https://docs.agno.com/sdk/introduction)
- [Agno Sessions Overview](https://docs.agno.com/sessions/overview)
- [Agno Runtime Overview](https://docs.agno.com/runtime/overview)
