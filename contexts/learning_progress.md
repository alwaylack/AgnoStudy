# Agno 学习进度记录

更新时间：2026-04-22

## 今日停课点

今天的学习停在 `Workflow` 主线的第 2 课。

当前最新完成课程：

- [examples/28_workflow_grouped_steps.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\28_workflow_grouped_steps.py:1)

## 当前学习阶段

目前已经完成以下主线内容：

- Agent 基础与兼容 OpenAI 模型封装
- Tools 基础、内置工具、自定义 Toolkit
- Session / History / Learning / Memory
- Knowledge / RAG / Readers / 多数据源 / 检索调优
- Team 四种基础模式与组合课
- 阶段性整合课与真实项目骨架深化课
- Workflow 基础与 Grouped Steps

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

## 当前已经掌握的重点

- 能用统一封装接入兼容 OpenAI 的三方模型与嵌入模型。
- 能注册普通函数工具、内置工具、自定义 Toolkit。
- 能区分 `learning`、`history`、`session`、`memory` 的使用场景。
- 能构建 Knowledge、接入 Reader、做过滤检索与基础调优。
- 能理解 Team 的 `coordinate / route / broadcast / tasks` 四种模式。
- 能把 Team 与 Knowledge、Tools、Tasks 组合起来。
- 能把项目从“单文件整合示例”继续拆成更接近真实项目的小应用结构。
- 能用 `Workflow` 组织顺序步骤，并用 `Steps` 封装一段可复用的小流程。

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

下一课建议继续进入 `Condition / 条件分支 Workflow`。

安排理由：

- 你已经学完了最基础的顺序型 Workflow。
- 你也已经学会了如何用 `Steps` 把一段小流程封装起来。
- 这时候继续学 `Condition` 最自然，因为它会把 Workflow 从“固定顺序”推进到“按条件分支执行”。

建议下次学习顺序：

1. `Condition / 条件分支 Workflow`
2. `Parallel / 并行 Workflow`
3. `Loop / 循环 Workflow`

参考方向：

- [Agno Workflows Overview](https://docs.agno.com/basics/workflows/overview)
- [Agno Workflow Patterns](https://docs.agno.com/workflows/workflow-patterns/overview)
- [Agno Conditional Workflow](https://docs.agno.com/workflows/workflow-patterns/conditional-workflow)

## 下次开始时建议先看

- [examples/27_workflow_basics.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\27_workflow_basics.py:1)
- [examples/28_workflow_grouped_steps.py](C:\Users\lenovo\Desktop\AgnoStudy\examples\28_workflow_grouped_steps.py:1)
- [README.md](C:\Users\lenovo\Desktop\AgnoStudy\README.md:1)
