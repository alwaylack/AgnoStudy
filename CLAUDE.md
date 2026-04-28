# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目目的
AgnoStudy 是一个结构化的 Agno 框架学习仓库，演示从基础 Agent/工具使用到高级 Workflow + Team 集成的渐进式掌握路径。代码库同时作为教育材料和 Agno 模式的参考实现。

## 架构概览

### 核心结构
- **examples/**：按能力组织的渐进式学习路径
  - `01-09_*`：Agent、工具、会话/记忆基础
  - `10-18_*`：知识/RAG 系统，包含读取器和过滤器
  - `16-24_*`：团队/多智能体协调模式
  - `25-26_*`：集成骨架和项目结构
  - `27-32_*`：工作流模式（顺序 → 条件 → 并行 → 循环 → 多模式）
- **knowledge_docs/**：Knowledge/RAG 示例使用的文档资源目录
- **tmp/**：示例运行时创建的临时文件目录（ChromaDB 向量库等）
- **contexts/**：学习进度和上下文跟踪目录

### 模型层
- **models/openai_model.py**：统一的 OpenAI 兼容模型接口
- **models/openai_embedder.py**：用于 RAG 系统的嵌入模型抽象

### 应用骨架
- **study_assistant_app/**：结合所有模式的真实集成示例

## 开发工作流

### 环境设置
```bash
# 使用 uv（推荐）
uv sync

# 使用 pip
pip install -e .

# 按需安装额外功能
uv pip install -U ddgs chromadb beautifulsoup4 pypdf reportlab
```

### 配置
在项目根目录创建 `.env`：
```env
OPENAI_BASE_URL="https://openrouter.ai/api/v1"
OPENAI_API_KEY="your-api-key"
OPENAI_MODEL_ID="openrouter/your-model"
OPENAI_EMBEDDING_MODEL_ID="your-embedding-model"
OPENAI_EMBEDDING_DIMENSIONS="1536"
```

### 运行示例
```bash
# 运行特定工作流课程
python examples/27_workflow_basics.py
python examples/28_workflow_grouped_steps.py
python examples/29_workflow_condition_basics.py
python examples/30_workflow_parallel_basics.py
python examples/31_workflow_loop_basics.py
python examples/32_workflow_multi_pattern_basics.py

# 运行集成骨架
python examples/25_integrated_app_skeleton.py
python examples/26_real_project_structure_basics.py
```

### 测试单个组件
```bash
# 测试特定示例
python examples/04_tools_basics.py
python examples/10_knowledge_rag_basics.py
python examples/16_team_coordinate_basics.py
```

## 代码模式与约定

### 示例结构模式
每个示例文件都遵循统一的代码结构：
```python
# 1. 导入必要的模块
from models import OpenAIModel

# 2. 定义主函数（命名格式：run_*_example()）
def run_xxx_example() -> None:
    model = OpenAIModel.from_env()
    agent = model.create_agent(...)
    agent.print_response(...)

# 3. 在 __main__ 块中调用
if __name__ == "__main__":
    run_xxx_example()
```

### Agno 模块导入模式
```python
# Workflow 相关
from agno.workflow import Workflow, Step, Steps, Condition, Parallel, Loop, StepOutput

# Team 相关
from agno.team import Team, TeamMode

# Knowledge 相关
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType

# 模型层封装
from models import OpenAIModel, OpenAICompatibleEmbedder
```

### 模型集成
- 使用 `models/openai_model.py` 中的统一 OpenAI 兼容接口
- 嵌入模型遵循 `models/openai_embedder.py` 的模式
- 所有模型引用都使用环境变量进行配置

### 知识/RAG 架构
- 将读取器实现为具有一致接口的独立模块
- 使用 Knowledge 进行文档摄取和检索
- 应用过滤器和调优器进行检索优化
- 支持多种数据源（网页、PDF、网站等）

## 当前学习状态
- **进度**：已完成所有基础模式直到工作流多模式组合
- **下一步重点**：工作流 + 团队集成（高级编排）
- **当前示例**：`examples/32_workflow_multi_pattern_basics.py`

## 依赖与扩展

### 核心依赖
来自 `pyproject.toml` 的完整依赖列表：
- `agno>=1.0.0`：Agno 框架（当前本地版本 2.5.17）
- `openai>=2.30.0`：OpenAI SDK
- `pydantic>=2.0.0`：数据验证和结构化输出
- `sqlalchemy>=2.0.49`：数据库 ORM
- `fastapi>=0.136.0`：Web 框架
- `python-dotenv>=1.0.0`：环境变量管理
- `beautifulsoup4>=4.12.0`：HTML 解析
- `chromadb>=0.5.0`：向量数据库
- `ddgs>=9.13.1`：DuckDuckGo 搜索
- `pypdf>=5.0.0`：PDF 读取
- `reportlab>=4.0.0`：PDF 生成

### 模型提供商
- OpenAI 兼容模型提供商（支持 OpenRouter 等第三方）
- 基于环境变量的配置

### 可选扩展
```bash
# 网页搜索能力
uv pip install -U ddgs

# 向量数据库用于 RAG
uv pip install -U chromadb

# 文档处理
uv pip install -U beautifulsoup4 pypdf reportlab
```

## 版本说明
- Agno 2.5.17 兼容性
- `Agent.__init__()` 不支持 `show_tool_calls`
- 使用 `debug_mode=True` 显示工具调用
- Knowledge 示例使用基于脚本位置的路径解析

## 文件组织原则
- 示例从简单到复杂递进
- 每个示例聚焦单一能力或模式
- 集成示例展示多模式组合
- 模型层抽象化提供商特定细节
- 在 `contexts/learning_progress.md` 中维护进度跟踪

## 如何扩展项目

### 添加新示例
1. 遵循 `examples/XX_主题_basics.py` 命名模式
2. 实现 `run_*_example()` 主函数
3. 使用 `models` 目录中的封装类创建 Agent
4. 在 `if __name__ == "__main__":` 块中调用主函数

### 创建新工作流
参考 `examples/27-32_*` 的工作流模式：
1. 导入 `agno.workflow` 中的必要类
2. 定义步骤函数，返回 `StepOutput`
3. 使用 `Condition`、`Parallel`、`Loop` 等组合步骤
4. 创建 `Workflow` 实例并执行

### 集成新功能
参考 `study_assistant_app/` 的模块化结构：
1. 将功能拆分为独立模块（如 `knowledge.py`、`team.py`）
2. 在 `app.py` 中组装各模块
3. 使用 `__init__.py` 导出公共接口
4. 遵循现有的依赖注入模式

### 添加新知识文档
1. 将文档放入 `knowledge_docs/` 目录
2. 使用 Markdown 格式便于 `MarkdownReader` 读取
3. 在示例中使用基于脚本位置的路径解析