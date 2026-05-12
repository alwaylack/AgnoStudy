# AgnoStudy

这是一个按学习节奏逐步搭建的 Agno 学习项目，目标有两件事：

1. 从 Agno 官方核心能力开始，系统学习 `Agent / Tools / Knowledge / Team / Workflow / Runtime`
2. 保留一套适合兼容 OpenAI 三方模型的本地封装方式，方便边学边改、边学边跑

## 当前状态

当前最新课程：

- [examples/66_product_app_capabilities.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\66_product_app_capabilities.py:1)

当前最适合的下一课：

- 为产品化入口补 smoke test / 整理学习手册

当前主线已经覆盖到：

- Agents / Tools / Knowledge / Teams
- Workflow 基础、组合模式与长链路整合
- Workflow Sessions
- Runtime: Serve as API / Storage + Interfaces / Scheduling
- 回到更完整的小项目升级
- 官方 SDK Introduction: Input & Output / Database / Session Management
- 官方 SDK Advanced: Context Management / State Management / Chat History / Dependency Injection / Hooks / Skills / Reasoning / Multimodal
- 官方 SDK Production: Guardrails / Human in the Loop / Evals / Tracing / Context Compression / Run Cancellation / Background Execution / MCP

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
- [examples/48_session_management_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\48_session_management_basics.py:1)

### 8. 官方 SDK Advanced 对齐线

- [examples/49_context_management_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\49_context_management_basics.py:1)
- [examples/50_state_management_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\50_state_management_basics.py:1)
- [examples/51_chat_history_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\51_chat_history_basics.py:1)
- [examples/52_dependency_injection_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\52_dependency_injection_basics.py:1)
- [examples/53_hooks_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\53_hooks_basics.py:1)
- [examples/54_skills_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\54_skills_basics.py:1)
- [examples/55_reasoning_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\55_reasoning_basics.py:1)
- [examples/56_multimodal_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\56_multimodal_basics.py:1)
- [examples/57_guardrails_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\57_guardrails_basics.py:1)
- [examples/58_human_in_the_loop_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\58_human_in_the_loop_basics.py:1)
- [examples/59_evals_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\59_evals_basics.py:1)
- [examples/60_tracing_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\60_tracing_basics.py:1)
- [examples/61_official_plan_wrap_up.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\61_official_plan_wrap_up.py:1)
- [examples/62_context_compression_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\62_context_compression_basics.py:1)
- [examples/63_run_cancellation_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\63_run_cancellation_basics.py:1)
- [examples/64_background_execution_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\64_background_execution_basics.py:1)
- [examples/65_mcp_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\65_mcp_basics.py:1)
- [examples/66_product_app_capabilities.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\66_product_app_capabilities.py:1)

## 第 48 课：Session Management

这一课对齐官方 [SDK Introduction](https://docs.agno.com/sdk/introduction) 里的 `Session Management`。

重点学习：

- `set_session_name()`：主动给 session 命名
- `update_session_state()`：手动写入 session 状态
- `get_session_state()`：读取当前 session 状态
- `get_session_messages()`：读取最近消息
- `get_session()`：查看当前 session 的整体记录

运行方式：

```bash
python examples/48_session_management_basics.py
```

数据库文件默认保存在：

- [lesson_48_session_management.db](C:\Users\lenovo\Desktop\AgnoStudy\tmp\lesson_48_session_management.db:1)

## 第 49 课：Context Management

这一课对齐官方 [SDK Advanced](https://docs.agno.com/sdk/introduction) 里的 `Context Management`。

重点学习：

- `add_history_to_context`：自动注入历史消息到上下文
- `num_history_runs`：控制注入的历史轮次数量
- 多轮工具调用场景下的上下文清理策略
- 长对话场景下的上下文压缩策略
- 如何观察和对比 token 消耗

运行方式：

```bash
python examples/49_context_management_basics.py
```

数据库文件默认保存在：

- [lesson_49_context_management.db](C:\Users\lenovo\Desktop\AgnoStudy\tmp\lesson_49_context_management.db:1)

## 第 50 课：State Management

这一课对齐官方 [SDK Advanced](https://docs.agno.com/sdk/introduction) 里的 `State Management`。

重点学习：

- `update_session_state()`：手动管理结构化的会话状态
- `enable_agentic_state=True`：让 agent 自动根据对话内容修改状态
- `add_session_state_to_context=True`：将状态注入到 agent 的上下文
- 任务管理场景下的状态管理实践

运行方式：

```bash
python examples/50_state_management_basics.py
```

数据库文件默认保存在：

- [lesson_50_state_management.db](C:\Users\lenovo\Desktop\AgnoStudy\tmp\lesson_50_state_management.db:1)

## 第 51 课：Chat History

这一课对齐官方 [Chat History](https://docs.agno.com/database/chat-history)。

重点学习：

- `add_history_to_context`：把最近历史自动注入上下文
- `read_chat_history`：让 Agent 按需读取当前聊天历史
- `search_session_history`：让 Agent 搜索过去 session
- `get_chat_history()`：程序化读取聊天历史
- `get_last_run_output()`：读取最后一次运行结果

运行方式：

```bash
python examples/51_chat_history_basics.py
```

数据库文件默认保存在：

- [lesson_51_chat_history.db](C:\Users\lenovo\Desktop\AgnoStudy\tmp\lesson_51_chat_history.db:1)

## 第 52 课：Dependency Injection

这一课对齐官方 [Dependency Injection](https://docs.agno.com/context/dependencies/overview)。

重点学习：

- `dependencies`：给 Agent / Team 注入运行时业务上下文
- callable dependency：在运行前动态解析最新上下文
- `add_dependencies_to_context`：把依赖作为 additional context 注入给模型
- `RunContext.dependencies`：让工具函数读取同一份依赖
- Team 级 dependencies：让团队协调者和成员共享课程上下文

运行方式：

```bash
python examples/52_dependency_injection_basics.py
```

## 第 53 课：Hooks

这一课对齐官方 [Hooks](https://docs.agno.com/hooks/overview)。

重点学习：

- `pre_hooks`：在模型运行前做输入校验、脱敏、审计或上下文准备
- `post_hooks`：在模型运行后做输出检查、指标记录或日志采集
- `tool_hooks`：包裹工具调用，统一记录工具入参、结果和错误
- `InputCheckError`：让 pre hook 在模型调用前阻止不合适的输入
- Team hooks：在 Team 层统一处理运行前后的横切逻辑

运行方式：

```bash
python examples/53_hooks_basics.py
```

## 第 54-64 课：官方计划补齐与收尾

这一组课程继续对齐官方 SDK Introduction 中的 Advanced / Production 主线：

- [examples/54_skills_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\54_skills_basics.py:1)：`Skills / LocalSkills / SKILL.md`
- [examples/55_reasoning_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\55_reasoning_basics.py:1)：`reasoning=True / reasoning_steps`
- [examples/56_multimodal_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\56_multimodal_basics.py:1)：`Image / File / send_media_to_model`
- [examples/57_guardrails_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\57_guardrails_basics.py:1)：`PIIDetectionGuardrail / InputCheckError`
- [examples/58_human_in_the_loop_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\58_human_in_the_loop_basics.py:1)：`requires_confirmation / requires_user_input / external_execution`
- [examples/59_evals_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\59_evals_basics.py:1)：`AccuracyEval / PerformanceEval`
- [examples/60_tracing_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\60_tracing_basics.py:1)：`setup_tracing / DatabaseSpanExporter`
- [examples/61_official_plan_wrap_up.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\61_official_plan_wrap_up.py:1)：课程计划收尾检查
- [examples/62_context_compression_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\62_context_compression_basics.py:1)：`CompressionManager / compress_tool_results`
- [examples/63_run_cancellation_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\63_run_cancellation_basics.py:1)：`cancel_run / raise_if_cancelled`
- [examples/64_background_execution_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\64_background_execution_basics.py:1)：`background=True / arun`
- [examples/65_mcp_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\65_mcp_basics.py:1)：`MCPTools / streamable-http / stdio`
- [examples/66_product_app_capabilities.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\66_product_app_capabilities.py:1)：回到 `study_assistant_app` 整合 Skills / Guardrails / Tracing / MCP

运行方式：

```bash
python examples/61_official_plan_wrap_up.py
```

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
- Session Management
- Context Management
- State Management
- Chat History
- Dependency Injection
- Hooks
- Skills
- Reasoning
- Multimodal
- Guardrails
- Human in the Loop
- Evals
- Tracing
- Context Compression
- Run Cancellation
- Background Execution

还没有按官方目录系统补齐的部分：

- 当前 SDK Introduction 主线已经补齐，下一步回到应用产品化整理

## 接下来更合适的课程顺序

下一阶段建议改成下面这条线：

1. ~~`Context Management`~~ ✅ 已完成
2. ~~`State Management`~~ ✅ 已完成
3. ~~`Chat History`~~ ✅ 已完成
4. ~~`Dependency Injection`~~ ✅ 已完成
5. ~~`Hooks`~~ ✅ 已完成
6. ~~`Skills`~~ ✅ 已完成
7. ~~`Reasoning`~~ ✅ 已完成
8. ~~`Multimodal`~~ ✅ 已完成
9. ~~`Guardrails`~~ ✅ 已完成
10. ~~`Human in the Loop`~~ ✅ 已完成
11. ~~`Evals`~~ ✅ 已完成
12. ~~`Tracing`~~ ✅ 已完成
13. ~~`Context Compression`~~ ✅ 已完成
14. ~~`Run Cancellation`~~ ✅ 已完成
15. ~~`Background Execution`~~ ✅ 已完成
16. ~~`MCP`~~ ✅ 已完成
17. ~~`study_assistant_app` 产品化整理~~ ✅ 已完成
18. 为产品化入口补 smoke test / 整理学习手册

如果按最近三节课来排，推荐就是：

1. ~~`Human in the Loop`~~ ✅ 已完成
2. ~~`Evals`~~ ✅ 已完成
3. ~~`Tracing`~~ ✅ 已完成
4. ~~`Context Compression / Run Cancellation / Background Execution`~~ ✅ 已完成
5. 回到 `study_assistant_app` 做产品化整理

## 当前版本注意事项

- 当前本地版本是 `agno 2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`
- 当前项目统一使用 `debug_mode=True`
- 第 44 课已经按 `2.5.17` 改成使用 `ScheduleManager`
- 第 45 课继续沿用 `2.5.17` 兼容写法，把 `ScheduleManager`、`SchedulerTools` 和 `AgentOS` 统一收拢到产品入口
- 第 46 课使用 `input_schema / output_schema / save_response_to_file`
- 第 47 课使用 `SqliteDb / get_session / get_sessions`
- 第 48 课使用 `set_session_name / update_session_state / get_session_state / get_session_messages`，这些接口已确认在 `2.5.17` 可用
- 第 49 课使用 `add_history_to_context / num_history_runs / get_session_messages`，这些接口已确认在 `2.5.17` 可用
- 第 50 课使用 `enable_agentic_state / add_session_state_to_context`，这些接口已确认在 `2.5.17` 可用
- 第 51 课使用 `read_chat_history / search_session_history / get_chat_history / get_last_run_output`，这些接口已确认在 `2.5.17` 可用
- 第 52 课使用 `dependencies / add_dependencies_to_context / RunContext.dependencies`，这些接口已确认在 `2.5.17` 可用
- 第 53 课使用 `pre_hooks / post_hooks / tool_hooks / InputCheckError`，这些接口已确认在 `2.5.17` 可用
- 第 54 课使用 `Skills / LocalSkills / SKILL.md`
- 第 55 课使用 `reasoning / reasoning_min_steps / reasoning_max_steps`
- 第 56 课使用 `Image / File / send_media_to_model`
- 第 57 课使用 `PIIDetectionGuardrail`
- 第 58 课使用 `requires_confirmation / requires_user_input / external_execution`
- 第 59 课使用 `AccuracyEval / PerformanceEval`
- 第 60 课使用 `setup_tracing`
- 第 62 课使用 `CompressionManager / compress_tool_results`
- 第 63 课使用 `cancel_run / raise_if_cancelled`
- 第 64 课使用 `background=True / arun`
- 第 65 课使用 `MCPTools / MultiMCPTools`，live demo 需要额外安装 `mcp`

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
