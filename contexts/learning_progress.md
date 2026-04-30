# Agno 学习进度记录

更新时间：2026-04-30

## 今日停课点

今天的学习已经推进到 `Workflow` 主线的第 12 课。

当前最新完成课程：

- [examples/38_workflow_router_orchestration.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\38_workflow_router_orchestration.py:1)

## 当前学习阶段

目前已经完成以下主线内容：

- Agent 基础与兼容 OpenAI 模型封装
- Tools 基础、内置工具、自定义 Toolkit
- Session / History / Learning / Memory
- Knowledge / RAG / Readers / 多数据源 / 检索调优
- Team 四种基础模式与组合课
- 阶段性整合课与真实项目骨架深化课
- Workflow 基础与 Grouped Steps
- Workflow 条件分支
- Workflow 并行执行
- Workflow 循环执行
- Workflow 多模式组合
- Workflow 与 Team 结合
- Workflow 与 Knowledge 结合
- Workflow 与 Team、Knowledge 结合
- 更接近真实项目的小型工作流
- 回到完整应用骨架的工作流整合
- 更复杂的工作流编排

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

### 第四阶段：阶段性整合

- `25_integrated_app_skeleton.py`

### 第五阶段：真实项目骨架深化

- `26_real_project_structure_basics.py`

### 第六阶段：Workflow 入门

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

## 当前已经掌握的重点

- 能用统一封装接入兼容 OpenAI 的三方模型与嵌入模型。
- 能注册普通函数工具、内置工具、自定义 Toolkit。
- 能区分 `learning`、`history`、`session`、`memory` 的使用场景。
- 能构建 Knowledge、接入 Reader、做过滤检索与基础调优。
- 能理解 Team 的 `coordinate / route / broadcast / tasks` 四种模式。
- 能把 Team 与 Knowledge、Tools、Tasks 组合起来。
- 能把项目从“单文件整合示例”继续拆成更接近真实项目的小应用结构。
- 能用 `Workflow` 组织顺序步骤，并用 `Steps` 封装一段可复用的小流程。
- 能用 `Condition` 根据前一步结果决定执行不同分支。
- 能用 `Parallel` 让多个独立步骤同时执行，并在后续步骤中统一汇总结果。
- 能用 `Loop` 重复执行同一组步骤，并理解 `max_iterations`、`end_condition`、`forward_iteration_output`。
- 能把 `Condition + Parallel + Loop` 组合到同一个 Workflow 里。
- 能把 `Team` 作为 Workflow 的一个步骤阶段来使用。
- 能把 `Knowledge` 作为 Workflow 某个阶段的共享信息源来使用。
- 能把 `Workflow`、`Team`、`Knowledge` 三者组合到同一个流程里。
- 能围绕一个更完整的目标组织小型学习助手工作流。
- 能把工作流能力接回应用骨架，而不是只停留在单独示例文件中。
- 能用 `Router` 把请求分流到不同子流程中完成更复杂的工作流编排。

## 当前项目里的关键封装

- [models/openai_model.py](C:\Users\lenovo\Desktop\AgnoStudy\models\openai_model.py:1)
- [models/openai_embedder.py](C:\Users\lenovo\Desktop\AgnoStudy\models\openai_embedder.py:1)
- [study_assistant_app](C:\Users\lenovo\Desktop\AgnoStudy\study_assistant_app)

## 已解决的版本与运行问题

- 当前本地版本是 `agno 2.5.17`。
- `Agent.__init__()` 不支持 `show_tool_calls`，当前项目统一使用 `debug_mode=True`。
- Knowledge 示例中的本地路径已经改为基于脚本位置推导绝对路径。
- `WebsiteReader`、`PDFReader`、DuckDuckGo 等能力需要额外依赖。

## 当前环境变量注意事项

除基础模型配置外，Knowledge / RAG 课程还需要注意：

- `OPENAI_EMBEDDING_MODEL_ID`
- `OPENAI_EMBEDDING_DIMENSIONS`

## 常用依赖补充

```bash
uv pip install -U ddgs
uv pip install -U chromadb
uv pip install -U beautifulsoup4
uv pip install -U pypdf reportlab
```

## 下一课安排

下一课建议进入“更长链路的真实项目实践”。

安排理由：

- 你已经学完了最基础的顺序型 Workflow。
- 你已经学会了如何用 `Steps` 把一段小流程封装起来。
- 你也已经完成了 `Condition`。
- 你也已经完成了 `Parallel`。
- 你也已经完成了 `Loop`。
- 你也已经完成了第一节多模式组合课。
- 你也已经完成了 `Workflow + Team`。
- 你也已经完成了 `Workflow + Knowledge`。
- 你也已经完成了 `Workflow + Team + Knowledge`。
- 你也已经完成了第一节更接近真实项目的小型工作流。
- 你也已经完成了把工作流接回应用骨架的整合。
- 你也已经完成了第一节 Router 驱动的复杂编排。
- 现在最适合把这些能力放到更长链路的真实项目实践里。

建议下次学习顺序：

1. `Condition / 条件分支 Workflow`
2. `Parallel / 并行 Workflow`
3. `Loop / 循环 Workflow`
4. `Workflow 组合模式`
5. `Workflow + Team`
6. `Workflow + Knowledge`
7. `Workflow + Team + Knowledge`
8. 更接近真实项目的小型工作流
9. 回到更完整的应用骨架整合
10. 更复杂的工作流编排
11. 更长链路的真实项目实践

参考方向：

- [Agno Workflows Overview](https://docs.agno.com/basics/workflows/overview)
- [Agno Workflow Patterns](https://docs.agno.com/workflows/workflow-patterns/overview)
- [Agno Conditional Workflow](https://docs.agno.com/workflows/workflow-patterns/conditional-workflow)
- [Agno Parallel Workflow](https://docs.agno.com/workflows/workflow-patterns/parallel-workflow)
- [Agno Loop Workflow](https://docs.agno.com/workflows/workflow-patterns/loop-workflow)
- [Agno Iterative Workflow](https://docs.agno.com/workflows/workflow-patterns/iterative-workflow)
- [Agno Workflow Patterns Overview](https://docs.agno.com/workflows/workflow-patterns/overview)

## 下次开始时建议先看

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
- [README.md](C:\Users\lenovo\Desktop\AgnoStudy\README.md:1)
