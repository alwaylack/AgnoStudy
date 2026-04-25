# AgnoStudy

这是一个按学习节奏逐步搭建的 Agno 练习项目，目标有两件事：

1. 从最基础的官方能力开始学习 `Agent / Tools / Knowledge / Team / Workflow`
2. 保留一套适合兼容 OpenAI 三方模型的本地封装方式

## 当前学习主线

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

### 6. 阶段性整合与项目骨架

- [examples/25_integrated_app_skeleton.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\25_integrated_app_skeleton.py:1)
- [examples/26_real_project_structure_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\26_real_project_structure_basics.py:1)
- [study_assistant_app](C:\Users\lenovo\Desktop\AgnoStudy\study_assistant_app)

### 7. Workflow

- [examples/27_workflow_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\27_workflow_basics.py:1)
- [examples/28_workflow_grouped_steps.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\28_workflow_grouped_steps.py:1)
- [examples/29_workflow_condition_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\29_workflow_condition_basics.py:1)
- [examples/30_workflow_parallel_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\30_workflow_parallel_basics.py:1)

## 当前停课点

当前最新课程：

- [examples/30_workflow_parallel_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\30_workflow_parallel_basics.py:1)

当前最适合的下一课：

- `Loop / 循环 Workflow`

## 第 27 课和第 28 课在学什么

第 27 课重点是最基础的顺序型 Workflow：

- 先分析当前学习阶段
- 再用函数步骤整理中间结果
- 最后生成下一课建议

第 28 课重点是 `Steps`：

- 外层 `Workflow` 负责主干流程
- 内层 `Steps` 负责封装一段可复用的小流程

第 29 课重点是 `Condition`：

- 先做阶段分析
- 再根据条件判断走不同分支
- 最后统一汇总成下一课建议

第 30 课重点是 `Parallel`：

- 让多个独立步骤同时执行
- 再把多个分支结果统一汇总
- 建立“并行采集 -> 汇总结论”的 Workflow 直觉

## 环境变量

在项目根目录准备 `.env`：

```env
OPENAI_BASE_URL="https://openrouter.ai/api/v1"
OPENAI_API_KEY="your-api-key"
OPENAI_MODEL_ID="openrouter/your-model"
OPENAI_EMBEDDING_MODEL_ID="your-embedding-model"
OPENAI_EMBEDDING_DIMENSIONS="1536"
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

补充能力时常见的安装命令：

```bash
uv pip install -U ddgs
uv pip install -U chromadb
uv pip install -U beautifulsoup4
uv pip install -U pypdf reportlab
```

## 运行方式

运行当前 Workflow 课程：

```bash
python examples/27_workflow_basics.py
python examples/28_workflow_grouped_steps.py
python examples/29_workflow_condition_basics.py
python examples/30_workflow_parallel_basics.py
```

如果只想回顾当前阶段的整合骨架：

```bash
python examples/25_integrated_app_skeleton.py
python examples/26_real_project_structure_basics.py
```

## 当前版本注意事项

- 当前本地版本为 `agno 2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`
- 当前示例统一使用 `debug_mode=True`

## 下次学习建议

下次建议直接从 `Loop / 循环 Workflow` 开始，原因是：

- 你已经掌握了顺序型 Workflow
- 你已经掌握了 `Steps`
- 你已经掌握了 `Condition`
- 你已经掌握了 `Parallel`
- 继续学 `Loop` 最适合把 Workflow 从一次性流程推进到可重复迭代流程

推荐接下来的学习顺序：

1. `Loop / 循环 Workflow`
2. 之后再回头看更复杂的组合模式
3. 再进一步尝试 Workflow 与 Team / Knowledge 的组合

参考官方文档：

- [Agno Workflows Overview](https://docs.agno.com/basics/workflows/overview)
- [Agno Workflow Patterns](https://docs.agno.com/workflows/workflow-patterns/overview)
- [Agno Conditional Workflow](https://docs.agno.com/workflows/workflow-patterns/conditional-workflow)
- [Agno Parallel Workflow](https://docs.agno.com/workflows/workflow-patterns/parallel-workflow)
