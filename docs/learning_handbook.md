# AgnoStudy 深度学习手册

> 本手册专为 AgnoStudy 项目设计，涵盖从基础 Agent 到高级 Workflow + Team 集成的完整学习路径。
> 语言说明：中文为主，Agno 专有名词保留英文原文。

---

## 难度标记说明

| 标记 | 级别 | 说明 |
|:----:|:----:|:-----|
| ⭐ | 入门级 | 零基础可学，核心概念介绍 |
| ⭐⭐ | 基础级 | 需要了解 Python 基础 |
| ⭐⭐⭐ | 中级 | 需要完成前置课程 |
| ⭐⭐⭐⭐ | 高级 | 需要理解多种模式的组合 |
| ⭐⭐⭐⭐⭐ | 专家级 | 需要具备系统设计能力 |

---

## 学习路径总览

```
┌─────────────────────────────────────────────────────────────────┐
│                         AgnoStudy 学习路径                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  第一阶段：Agent 基础（01-09）                  ⭐ ~ ⭐⭐⭐       │
│  ├── 01 Agent 基础                               ⭐             │
│  ├── 02 OpenAI 兼容模型                           ⭐             │
│  ├── 03 学习能力                                  ⭐⭐           │
│  ├── 04 工具基础                                  ⭐⭐           │
│  ├── 05 结构化输出                                ⭐⭐           │
│  ├── 06 内置工具                                  ⭐⭐           │
│  ├── 07 自定义 Toolkit                            ⭐⭐⭐         │
│  ├── 08 会话历史                                  ⭐⭐           │
│  └── 09 学习记忆                                  ⭐⭐⭐         │
│                                                                 │
│  第二阶段：Knowledge / RAG（10-18）              ⭐⭐⭐ ~ ⭐⭐⭐⭐ │
│  ├── 10 RAG 基础                                  ⭐⭐⭐         │
│  ├── 11 读取器与过滤器                             ⭐⭐⭐         │
│  ├── 12 RAG 调优                                  ⭐⭐⭐⭐       │
│  ├── 13 多数据源                                  ⭐⭐⭐         │
│  ├── 14 网页读取器                                ⭐⭐⭐         │
│  ├── 15 PDF 读取器                                ⭐⭐⭐         │
│  ├── 17 深度爬取                                  ⭐⭐⭐⭐       │
│  └── 18 高级过滤                                  ⭐⭐⭐⭐       │
│                                                                 │
│  第三阶段：Team / 多智能体（16-24）              ⭐⭐⭐ ~ ⭐⭐⭐⭐⭐│
│  ├── 16 Coordinate 模式                           ⭐⭐⭐         │
│  ├── 19 Route 模式                                ⭐⭐⭐         │
│  ├── 20 Broadcast 模式                            ⭐⭐⭐         │
│  ├── 21 Tasks 模式                                ⭐⭐⭐⭐       │
│  ├── 22 共享知识                                  ⭐⭐⭐⭐       │
│  ├── 23 共享工具                                  ⭐⭐⭐⭐       │
│  └── 24 Tasks 与知识                              ⭐⭐⭐⭐⭐     │
│                                                                 │
│  第四阶段：集成与项目结构（25-26）               ⭐⭐⭐⭐         │
│  ├── 25 应用骨架                                  ⭐⭐⭐⭐       │
│  └── 26 项目结构                                  ⭐⭐⭐⭐       │
│                                                                 │
│  第五阶段：Workflow（27-38）                     ⭐⭐⭐ ~ ⭐⭐⭐⭐⭐│
│  ├── 27 基础工作流                                ⭐⭐⭐         │
│  ├── 28 分组步骤                                  ⭐⭐⭐         │
│  ├── 29 条件分支                                  ⭐⭐⭐⭐       │
│  ├── 30 并行执行                                  ⭐⭐⭐⭐       │
│  ├── 31 循环执行                                  ⭐⭐⭐⭐       │
│  ├── 32 多模式组合                                ⭐⭐⭐⭐⭐     │
│  ├── 33 Workflow + Team                           ⭐⭐⭐⭐⭐     │
│  ├── 34 Workflow + Knowledge                      ⭐⭐⭐⭐⭐     │
│  ├── 35 Workflow + Team + Knowledge               ⭐⭐⭐⭐⭐     │
│  ├── 36 真实项目小型工作流                         ⭐⭐⭐⭐⭐     │
│  ├── 37 应用骨架工作流                             ⭐⭐⭐⭐⭐     │
│  └── 38 Router 路由编排                            ⭐⭐⭐⭐⭐     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 目录

- [第一阶段：Agent 基础（01-09）](#第一阶段agent-基础01-09)
- [第二阶段：Knowledge / RAG（10-18）](#第二阶段knowledge--rag10-18)
- [第三阶段：Team / 多智能体（16-24）](#第三阶段team--多智能体16-24)
- [第四阶段：集成与项目结构（25-26）](#第四阶段集成与项目结构25-26)
- [第五阶段：Workflow（27-38）](#第五阶段workflow27-38)
- [附录](#附录)

---

# 第一阶段：Agent 基础（01-09）

> 本阶段目标：掌握 Agno Agent 的核心概念，包括模型封装、工具使用、会话管理和记忆系统。

---

## 1.1 Agent 基础能力 ⭐

**对应示例**：`examples/01_agent_basics.py`

### 学习目标

- 理解 Agno Agent 的基本概念
- 掌握 Agent 的创建和配置方法
- 学会使用 Agent 进行基础对话

### 核心概念

**Agent** 是 Agno 中的智能体核心，负责理解用户输入、调用工具、生成响应。

### 代码解析

```python
from models import OpenAIModel

def run_basic_example() -> None:
    """运行最基础的 Agent 示例。"""
    # 使用环境变量创建模型实例
    model = OpenAIModel.from_env()

    # 创建 Agent，配置名称、指令和输出格式
    agent = model.create_agent(
        name="Agno Agent",
        instructions=["你是一个有帮助的 AI 助手。"],
        markdown=True,
    )

    # 打印 Agent 的响应
    agent.print_response("你好，请介绍一下 Agno 框架。")
```

### 关键参数

| 参数 | 说明 |
|------|------|
| `name` | Agent 的唯一标识名称 |
| `instructions` | Agent 的行为指导指令 |
| `markdown` | 是否启用 Markdown 格式输出 |

### 动手实践

1. 运行示例：`python examples/01_agent_basics.py`
2. 尝试修改 `instructions`，观察 Agent 行为变化
3. 测试不同类型的输入（问题、指令、闲聊）

---

## 1.2 OpenAI 兼容模型 ⭐

**对应示例**：`examples/02_openai_compatible_agent.py`

### 学习目标

- 理解 OpenAI 兼容模型的概念
- 掌握模型封装层的使用方法
- 学会通过环境变量配置模型

### 核心概念

**OpenAI Compatible Model** 指支持 OpenAI API 格式的第三方模型服务（如 OpenRouter、Azure OpenAI 等）。

### 代码解析

```python
from models import OpenAIModel

def run_openai_compatible_example() -> None:
    """演示如何用 OpenAILike 接入兼容 OpenAI 的第三方模型。"""
    # 复用模型封装类，避免每个示例都重复写配置代码
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="OpenAI 兼容 Agent",
        instructions=[
            "你的回答需要简洁明了，帮助用户专注学习 Agno。"
        ],
        markdown=True,
    )

    agent.print_response("给我制定一个今天的 Agno 学习小计划。")
```

### 模型封装层

`models/openai_model.py` 提供了统一的模型接口：

```python
class OpenAIModel:
    """封装兼容 OpenAI 的模型，方便在不同的 Agno 示例中复用。"""

    def __init__(self, model_id=None, api_key=None, base_url=None, **model_kwargs):
        self.model_id = model_id or os.getenv("OPENAI_MODEL_ID")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")

    def get_model(self) -> OpenAILike:
        """构建 Agno 的 OpenAILike 模型实例。"""
        return OpenAILike(
            id=self.model_id,
            api_key=self.api_key,
            base_url=self.base_url,
            **self.model_kwargs,
        )

    def create_agent(self, name="Agno Agent", **kwargs) -> Agent:
        """创建一个使用当前模型的 Agno Agent。"""
        return Agent(name=name, model=self.get_model(), **kwargs)
```

### 环境配置

在项目根目录创建 `.env` 文件：

```env
OPENAI_BASE_URL="https://openrouter.ai/api/v1"
OPENAI_API_KEY="your-api-key"
OPENAI_MODEL_ID="openrouter/your-model"
OPENAI_EMBEDDING_MODEL_ID="your-embedding-model"
OPENAI_EMBEDDING_DIMENSIONS="1536"
```

---

## 1.3 学习能力 ⭐⭐

**对应示例**：`examples/03_learning_basics.py`

### 学习目标

- 理解 Agno 的 Learning 机制
- 掌握用户画像和记忆的自动提取
- 学会使用数据库持久化学习结果

### 核心概念

**Learning** 是 Agno 的学习能力，开启后 Agent 会自动提取用户画像和记忆，并在后续会话中回忆。

### 代码解析

```python
from pathlib import Path
from agno.db.sqlite import SqliteDb
from models import OpenAIModel

def run_learning_basics_example() -> None:
    """演示官方文档中最基础的学习能力用法。"""
    # 学习能力需要数据库保存用户信息
    db_path = Path("tmp/agents.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()

    # learning=True 开启基础学习能力
    # Agent 会自动提取用户画像和用户记忆
    agent = model.create_agent(
        name="Agno Learning Agent",
        db=SqliteDb(db_file=str(db_path)),
        learning=True,
        markdown=True,
    )

    user_id = "student@example.com"

    print("\n--- 会话 1：告诉 Agent 你的偏好 ---")
    agent.print_response(
        "你好，我更喜欢带代码示例的解释，而且我正在学习 Agno。",
        user_id=user_id,
        session_id="session_1",
    )

    print("\n--- 会话 2：让 Agent 回忆它学到了什么 ---")
    agent.print_response(
        "你还记得我的学习偏好吗？",
        user_id=user_id,
        session_id="session_2",
    )
```

### 关键参数

| 参数 | 说明 |
|------|------|
| `db` | 数据库实例，用于持久化学习结果 |
| `learning` | 是否开启学习能力 |
| `user_id` | 用户标识，用于区分不同用户 |
| `session_id` | 会话标识，用于区分不同会话 |

---

## 1.4 工具基础 ⭐⭐

**对应示例**：`examples/04_tools_basics.py`

### 学习目标

- 理解 Agno 工具系统的架构
- 掌握函数工具的注册方法
- 学会使用工具扩展 Agent 能力

### 核心概念

**Tools** 是 Agent 可以调用的功能模块，扩展了 Agent 的能力边界。普通 Python 函数可以直接作为工具注册。

### 代码解析

```python
from models import OpenAIModel

def get_study_tip(topic: str) -> str:
    """根据主题返回一条固定的学习建议。"""
    tips = {
        "agent": "先理解 Agent 的输入、模型和输出，再继续学习工具和记忆。",
        "memory": "先区分 user_id 和 session_id，再观察 Agent 会记住什么。",
        "tools": "先从简单函数开始，把工具调用流程跑通，再接第三方服务。",
    }
    return tips.get(topic.lower(), f"先从最小示例开始学习 {topic}，逐步增加复杂度。")

def add_numbers(a: int, b: int) -> int:
    """演示最简单的计算工具。"""
    return a + b

def run_tools_basics_example() -> None:
    """演示如何给 Agno Agent 添加最基础的 Python 工具。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Tools Agent",
        tools=[get_study_tip, add_numbers],  # 直接注册函数作为工具
        instructions=[
            "你是 Agno 学习助手。",
            "当用户的问题适合调用工具时，优先调用工具。",
            "如果使用了工具，请结合工具结果给出简洁解释。",
        ],
        markdown=True,
        debug_mode=True,  # 显示工具调用过程
    )

    print("\n--- 示例 1：让 Agent 调用学习建议工具 ---")
    agent.print_response("我正在学习 Agno 的 tools，给我一条学习建议。")

    print("\n--- 示例 2：让 Agent 调用计算工具 ---")
    agent.print_response("请帮我计算 13 + 29，并顺便告诉我这展示了什么工具能力。")
```

### 工具注册要点

1. **函数签名**：参数名和类型注解会被 Agent 用来理解工具用途
2. **文档字符串**：`docstring` 会被用作工具描述
3. **返回值**：返回的字符串会作为工具执行结果传回 Agent

---

## 1.5 结构化输出 ⭐⭐

**对应示例**：`examples/05_structured_output.py`

### 学习目标

- 理解结构化输出的概念
- 掌握使用 Pydantic 定义输出格式
- 学会让 Agent 按固定结构返回结果

### 核心概念

**Structured Output** 让 Agent 按照预定义的 JSON Schema 返回结构化数据，便于后续处理。

### 代码解析

```python
from pydantic import BaseModel, Field
from models import OpenAIModel

class StudyTask(BaseModel):
    """定义单个学习任务的数据结构。"""
    title: str = Field(description="任务标题")
    duration_minutes: int = Field(description="预计学习时长，单位为分钟")
    goal: str = Field(description="这个任务的学习目标")

class DailyStudyPlan(BaseModel):
    """定义一天学习计划的结构化输出格式。"""
    topic: str = Field(description="今天学习的主题")
    level: str = Field(description="学习难度，例如入门、基础、进阶")
    tasks: list[StudyTask] = Field(description="今天的学习任务列表")
    summary: str = Field(description="对今天计划的简短总结")

def run_structured_output_example() -> None:
    """演示如何让 Agent 按固定结构返回结果。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Structured Output Agent",
        instructions=[
            "你是 Agno 学习规划助手。",
            "请根据用户需求生成结构化的学习计划。",
        ],
        response_model=DailyStudyPlan,  # 指定输出结构
        markdown=True,
    )

    agent.print_response("请帮我制定一个今天学习 Agno Tools 的计划，大约 60 分钟。")
```

---

## 1.6 内置工具 ⭐⭐

**对应示例**：`examples/06_builtin_tools_duckduckgo.py`

### 学习目标

- 了解 Agno 内置工具生态
- 掌握 DuckDuckGo 搜索工具的使用
- 学会安装和配置额外依赖

### 核心概念

**Builtin Tools** 是 Agno 官方提供的开箱即用工具，包括搜索、计算、文件操作等能力。

### 代码解析

```python
from models import OpenAIModel

def run_builtin_tools_example() -> None:
    """演示如何注册并使用 Agno 内置的 DuckDuckGo 工具。"""
    try:
        from agno.tools.duckduckgo import DuckDuckGoTools
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装 DuckDuckGo 依赖：`uv pip install -U ddgs`"
        ) from exc

    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Builtin Tools Agent",
        tools=[DuckDuckGoTools(enable_search=True, enable_news=False)],
        instructions=[
            "你是 Agno 学习助手。",
            "当问题需要联网搜索时，优先使用 DuckDuckGo 工具。",
            "请根据搜索结果给出简洁总结。",
        ],
        markdown=True,
        debug_mode=True,
    )

    agent.print_response("请搜索 Agno 官方文档里对 tools 的定义，并做一个简短总结。")
```

### 依赖安装

```bash
uv pip install -U ddgs
```

---

## 1.7 自定义 Toolkit ⭐⭐⭐

**对应示例**：`examples/07_custom_toolkit.py`

### 学习目标

- 理解 Toolkit 的概念和用途
- 掌握自定义 Toolkit 的创建方法
- 学会将多个相关工具组织成工具包

### 核心概念

**Toolkit** 是一组相关工具的集合，通过继承 `agno.tools.Toolkit` 类实现，便于组织和复用。

### 代码解析

```python
from agno.tools import Toolkit
from models import OpenAIModel

class StudyTools(Toolkit):
    """把多个学习相关工具打包成一个可复用的 Toolkit。"""

    def __init__(self) -> None:
        super().__init__(name="study_tools")

        # 在自定义 Toolkit 中，需要把方法显式注册成工具
        self.register(self.get_study_tip)
        self.register(self.make_daily_goal)
        self.register(self.add_numbers)

    def get_study_tip(self, topic: str) -> str:
        """根据主题返回一条学习建议。"""
        tips = {
            "agent": "先理解 Agent 的核心职责，再学习记忆和工具。",
            "memory": "重点观察同一个 user_id 在不同 session_id 下的表现。",
            "tools": "先从简单函数工具开始，再组合成 Toolkit。",
        }
        return tips.get(topic.lower(), f"学习 {topic} 时，建议先从最小可运行示例开始。")

    def make_daily_goal(self, topic: str, minutes: int) -> str:
        """根据主题和时长生成一个简单的今日目标。"""
        return f"今天用 {minutes} 分钟学习 {topic}，重点是跑通一个最小示例并理解输出。"

    def add_numbers(self, a: int, b: int) -> int:
        """返回两个整数的和。"""
        return a + b

def run_custom_toolkit_example() -> None:
    """演示如何把自定义 Toolkit 注册到 Agent。"""
    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno Custom Toolkit Agent",
        tools=[StudyTools()],  # 注册自定义 Toolkit
        instructions=[
            "你是 Agno 学习助手。",
            "遇到适合用工具完成的问题时，优先调用工具。",
            "回答时请顺带说明刚刚调用了什么工具。",
        ],
        markdown=True,
        debug_mode=True,
    )

    agent.print_response("我在学习 Agno 的 memory，请给我一条学习建议。")
```

### Toolkit 创建要点

1. 继承 `agno.tools.Toolkit` 类
2. 在 `__init__` 中使用 `self.register()` 注册方法
3. 方法的 `docstring` 会作为工具描述
4. 方法的类型注解会被用来定义参数格式

---

## 1.8 会话历史 ⭐⭐

**对应示例**：`examples/08_sessions_history.py`

### 学习目标

- 理解 Session 和 History 的概念
- 掌握多轮对话的实现方法
- 学会控制历史消息的数量

### 核心概念

- **Session**：会话，一次完整的对话过程
- **History**：历史消息，Agent 可以读取之前的对话内容

### 代码解析

```python
from pathlib import Path
from agno.db.sqlite import SqliteDb
from models import OpenAIModel

def run_sessions_history_example() -> None:
    """演示如何用 Session 和 History 实现多轮对话。"""
    db_path = Path("tmp/sessions.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)

    model = OpenAIModel.from_env()

    agent = model.create_agent(
        name="Agno History Agent",
        db=SqliteDb(db_file=str(db_path)),
        add_history_to_context=True,  # 开启后自动把历史消息加入上下文
        num_history_runs=3,  # 只取最近 3 轮
        instructions=[
            "你是 Agno 学习助手。",
            "请根据当前会话中的历史消息，保持回答前后一致。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"
    session_id = "history_demo_session"

    print("\n--- 第 1 轮：建立上下文 ---")
    agent.print_response(
        "我正在学习 Agno，我更喜欢先看最小可运行示例。",
        user_id=user_id,
        session_id=session_id,
    )

    print("\n--- 第 2 轮：继续同一个 Session ---")
    agent.print_response(
        "请基于我刚才的偏好，给我一个学习建议。",
        user_id=user_id,
        session_id=session_id,
    )

    print("\n--- 第 3 轮：验证 Agent 是否能读取会话历史 ---")
    agent.print_response(
        "你还记得我喜欢什么样的学习方式吗？",
        user_id=user_id,
        session_id=session_id,
    )
```

### 关键参数

| 参数 | 说明 |
|------|------|
| `add_history_to_context` | 是否将历史消息加入上下文 |
| `num_history_runs` | 加入上下文的历史轮数 |

---

## 1.9 学习记忆 ⭐⭐⭐

**对应示例**：`examples/09_learning_machine_memory.py`

### 学习目标

- 理解 LearningMachine 的精细配置
- 掌握 UserMemory 和 SessionContext 的区别
- 学会自定义学习策略

### 核心概念

- **UserMemory**：长期用户记忆，跨会话持久化
- **SessionContext**：当前会话上下文，会话内有效
- **LearningMode**：学习策略（ALWAYS、ON_DEMAND 等）

### 代码解析

```python
from pathlib import Path
from agno.db.sqlite import SqliteDb
from agno.learn import LearningMachine, LearningMode, SessionContextConfig, UserMemoryConfig
from models import OpenAIModel

def run_learning_machine_memory_example() -> None:
    """演示如何使用 LearningMachine 精细配置学习能力。"""
    db_path = Path("tmp/learning_machine.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db = SqliteDb(db_file=str(db_path))

    model = OpenAIModel.from_env()

    # 和 learning=True 不同，这里把学习能力拆开配置：
    # 1. user_memory：长期记住用户偏好
    # 2. session_context：学习当前会话中的上下文事实
    learning = LearningMachine(
        db=db,
        user_memory=UserMemoryConfig(mode=LearningMode.ALWAYS),
        session_context=SessionContextConfig(mode=LearningMode.ALWAYS),
        debug_mode=True,
    )

    agent = model.create_agent(
        name="Agno LearningMachine Agent",
        db=db,
        learning=learning,
        instructions=[
            "你是 Agno 学习助手。",
            "请根据长期用户记忆和当前会话上下文来回答问题。",
        ],
        markdown=True,
    )

    user_id = "student@example.com"

    print("\n--- 会话 1：建立长期用户记忆 ---")
    agent.print_response(
        "我学习 Agno 时更喜欢先看最小示例，再看原理解释。",
        user_id=user_id,
        session_id="learning_machine_session_1",
    )

    print("\n--- 会话 2：让 Agent 回忆长期偏好 ---")
    agent.print_response(
        "你记得我的学习偏好吗？",
        user_id=user_id,
        session_id="learning_machine_session_2",
    )

    print("\n--- 会话 3：写入当前会话上下文 ---")
    agent.print_response(
        "我今天正在学习 Agno 的 LearningMachine，目标是理解 user_memory 和 session_context 的区别。",
        user_id=user_id,
        session_id="learning_machine_session_3",
    )

    print("\n--- 会话 4：验证当前会话上下文是否可用 ---")
    agent.print_response(
        "我今天这节课的重点是什么？",
        user_id=user_id,
        session_id="learning_machine_session_3",
    )
```

---

# 第二阶段：Knowledge / RAG（10-18）

> 本阶段目标：掌握 Agno 的知识库和 RAG（检索增强生成）系统，包括文档处理、向量存储和检索优化。

---

## 2.1 RAG 基础 ⭐⭐⭐

**对应示例**：`examples/10_knowledge_rag_basics.py`

### 学习目标

- 理解 RAG（Retrieval-Augmented Generation）的核心概念
- 掌握 Knowledge 和 VectorDB 的基本用法
- 学会构建最小可运行的 RAG 系统

### 核心概念

- **RAG**：检索增强生成，先检索相关文档，再基于文档生成回答
- **Knowledge**：Agno 的知识库管理组件
- **VectorDB**：向量数据库，用于存储和检索文档嵌入

### 代码解析

```python
from pathlib import Path
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.search import SearchType
from models import OpenAICompatibleEmbedder, OpenAIModel

def run_knowledge_rag_basics_example() -> None:
    """演示如何使用本地文档构建最小可运行的 Agno Knowledge / RAG 示例。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    # 基于当前脚本位置反推项目根目录，避免受执行时工作目录影响。
    project_root = Path(__file__).resolve().parents[1]
    document_path = project_root / "knowledge_docs" / "agno_rag_basics.md"
    vector_db_dir = project_root / "tmp" / "chromadb"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    if not document_path.exists():
        raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    model = OpenAIModel.from_env()
    embedder = OpenAICompatibleEmbedder.from_env()

    # 这里使用本地持久化 Chroma，适合作为知识库入门示例。
    vector_db = ChromaDb(
        collection="agno_study_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.vector,
    )

    knowledge = Knowledge(
        name="agno_study_knowledge",
        vector_db=vector_db,
    )

    # 首次运行时把本地资料写入知识库。
    knowledge.insert(
        path=str(document_path),
        upsert=True,
    )

    agent = model.create_agent(
        name="Agno Knowledge Agent",
        knowledge=knowledge,
        # 让 Agent 在回答问题时自动搜索知识库。
        search_knowledge=True,
        instructions=[
            "你是 Agno 学习助手。",
            "请优先根据知识库中的内容回答问题。",
            "如果知识库中没有答案，再明确说明资料中未提到。",
        ],
        markdown=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：询问 Knowledge 的作用 ---")
    agent.print_response("Agno 里的 Knowledge 更关注什么？它和 Memory 有什么区别？")

    print("\n--- 示例 2：询问 RAG 的基本流程 ---")
    agent.print_response("请根据知识库内容总结 Agno 中 RAG 的基本流程。")
```

### RAG 流程

```
文档 → Reader 分块 → Embedder 向量化 → VectorDB 存储
                                              ↓
用户查询 → Agent → 检索相关文档 → 结合文档生成回答
```

### 依赖安装

```bash
uv pip install -U chromadb
```

---

## 2.2 读取器与过滤器 ⭐⭐⭐

**对应示例**：`examples/11_knowledge_readers_and_filters.py`

### 学习目标

- 了解不同类型的文档读取器
- 掌握过滤器的使用方法
- 学会优化检索结果

### 核心概念

- **Reader**：文档读取器，负责解析不同格式的文档（Markdown、PDF、网页等）
- **Filter**：过滤器，用于筛选检索结果（按相关性、时间、来源等）

---

## 2.3 RAG 调优 ⭐⭐⭐⭐

**对应示例**：`examples/12_rag_tuning_basics.py`

### 学习目标

- 理解 RAG 系统的调优维度
- 掌握分块大小、检索数量等参数的调整
- 学会评估 RAG 系统的效果

### 调优维度

| 维度 | 参数 | 说明 |
|------|------|------|
| 分块 | `chunk_size` | 文档分块大小，影响检索精度 |
| 分块 | `chunk_overlap` | 分块重叠，避免信息断裂 |
| 检索 | `num_results` | 返回结果数量 |
| 检索 | `search_type` | 检索类型（cosine、hybrid 等） |

---

## 2.4 多数据源 ⭐⭐⭐

**对应示例**：`examples/13_knowledge_multi_source_basics.py`

### 学习目标

- 掌握同时处理多个数据源的方法
- 学会组织和管理不同来源的文档

---

## 2.5 网页读取器 ⭐⭐⭐

**对应示例**：`examples/14_knowledge_website_reader.py`

### 学习目标

- 掌握网页内容的抓取和解析
- 学会将网页内容纳入知识库

### 依赖安装

```bash
uv pip install -U beautifulsoup4
```

---

## 2.6 PDF 读取器 ⭐⭐⭐

**对应示例**：`examples/15_knowledge_pdf_reader.py`

### 学习目标

- 掌握 PDF 文档的读取和解析
- 学会处理 PDF 中的文本内容

### 依赖安装

```bash
uv pip install -U pypdf reportlab
```

---

## 2.7 深度爬取 ⭐⭐⭐⭐

**对应示例**：`examples/17_knowledge_website_deep_crawl.py`

### 学习目标

- 掌握网站深度爬取技术
- 学会处理多层级网页结构
- 理解爬取深度和范围的控制

---

## 2.8 高级过滤 ⭐⭐⭐⭐

**对应示例**：`examples/18_rag_filtering_advanced.py`

### 学习目标

- 掌握高级过滤策略
- 学会组合多种过滤条件
- 理解过滤对检索质量的影响

---

# 第三阶段：Team / 多智能体（16-24）

> 本阶段目标：掌握 Agno 的多智能体协调系统，包括四种基本模式（Coordinate、Route、Broadcast、Tasks）及其组合应用。

---

## 3.1 Coordinate 模式 ⭐⭐⭐

**对应示例**：`examples/16_team_coordinate_basics.py`

### 学习目标

- 理解 Team 的基本概念
- 掌握 Coordinate 协调模式
- 学会组织多个 Agent 协作完成任务

### 核心概念

- **Team**：团队，由多个 Agent 组成的协作单元
- **TeamMode**：团队模式，决定 Agent 之间的协作方式
- **Coordinate**：协调模式，由团队领导者分配任务并整合结果

### 代码解析

```python
from agno.team import Team, TeamMode
from models import OpenAIModel

def run_team_coordinate_basics_example() -> None:
    """演示如何使用 Team 组织多个 Agent 协作完成任务。"""
    model = OpenAIModel.from_env()

    # 创建专家 Agent
    concept_agent = model.create_agent(
        name="概念讲解专家",
        role="负责解释 Agno 概念和模块分工",
        instructions=[
            "你擅长把 Agno 的概念解释清楚。",
            "请尽量用初学者容易理解的方式说明问题。",
        ],
        markdown=True,
    )

    planning_agent = model.create_agent(
        name="学习规划专家",
        role="负责把学习目标拆成可执行步骤",
        instructions=[
            "你擅长把学习目标拆成清晰的步骤。",
            "请优先输出适合初学者执行的小步计划。",
        ],
        markdown=True,
    )

    # 创建团队，使用 Coordinate 模式
    team = Team(
        name="Agno 学习协作团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[concept_agent, planning_agent],
        instructions=[
            "你是团队协调者。",
            "请先判断需要哪些成员参与，再综合成员结果给出最终回答。",
            "最终回答要同时包含概念说明和可执行建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "我刚学完 Knowledge 和 PDF Reader。请团队一起帮我解释 Team / Multi-Agent 的作用，并给我一个下一步学习建议。"
    )
```

### Coordinate 模式特点

```
用户请求 → 团队领导者
              ↓
         分配任务给成员 A → 成员 A 结果
         分配任务给成员 B → 成员 B 结果
              ↓
         整合结果 → 最终回答
```

---

## 3.2 Route 模式 ⭐⭐⭐

**对应示例**：`examples/19_team_route_basics.py`

### 学习目标

- 理解 Route 路由模式的工作原理
- 掌握根据条件选择最合适的成员
- 学会设计路由策略

### 核心概念

**Route**：路由模式，团队领导者根据请求内容选择最合适的单个成员处理，直接返回该成员的回答。

### 代码解析

```python
from agno.team import Team, TeamMode
from models import OpenAIModel

def run_team_route_basics_example() -> None:
    """演示如何使用 TeamMode.route 把问题路由给最合适的成员。"""
    model = OpenAIModel.from_env()

    beginner_agent = model.create_agent(
        name="初学者辅导专家",
        role="只负责回答适合 Agno 初学者的问题",
        instructions=[
            "你只回答适合初学者的问题。",
            "请优先给出简单、直接、低负担的建议。",
        ],
        markdown=True,
    )

    advanced_agent = model.create_agent(
        name="进阶实践专家",
        role="只负责回答 Agno 进阶实践和架构问题",
        instructions=[
            "你只回答进阶实践问题。",
            "请优先关注检索优化、架构设计和复杂协作。",
        ],
        markdown=True,
    )

    # Route 模式：只路由给一个最合适的成员
    team = Team(
        name="Agno 路由团队",
        mode=TeamMode.route,
        model=model.get_model(),
        members=[beginner_agent, advanced_agent],
        instructions=[
            "你是团队路由器。",
            "请根据用户问题，把请求交给最合适的一个成员处理。",
            "不要综合多个成员结果，直接返回最合适成员的回答。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    print("\n--- 示例 1：路由到初学者专家 ---")
    team.print_response("我是初学者，刚学完 Agent 和 Tools，下一步最适合先学什么？")

    print("\n--- 示例 2：路由到进阶专家 ---")
    team.print_response("我已经学完基础课程，下一步更适合先优化 RAG，还是先设计多 Agent 架构？")
```

### Route 模式特点

```
用户请求 → 团队路由器
              ↓
         判断最合适的成员
              ↓
         路由给成员 X → 成员 X 结果 → 直接返回
```

---

## 3.3 Broadcast 模式 ⭐⭐⭐

**对应示例**：`examples/20_team_broadcast_basics.py`

### 学习目标

- 理解 Broadcast 广播模式的工作原理
- 掌握并行任务分发的方法
- 学会整合多个成员的并行结果

### 核心概念

**Broadcast**：广播模式，将同一请求同时发送给所有成员，收集并整合所有成员的回答。

### 代码解析

```python
from agno.team import Team, TeamMode
from models import OpenAIModel

def run_team_broadcast_basics_example() -> None:
    """演示如何使用 TeamMode.broadcast 让多个成员同时评估同一个问题。"""
    model = OpenAIModel.from_env()

    opportunity_agent = model.create_agent(
        name="机会分析专家",
        role="负责评估问题中的机会和收益",
        instructions=[
            "你专注于分析机会、优势和潜在收益。",
            "请优先说明这件事值得做的原因。",
        ],
        markdown=True,
    )

    risk_agent = model.create_agent(
        name="风险分析专家",
        role="负责评估问题中的风险和潜在问题",
        instructions=[
            "你专注于分析风险、限制和潜在问题。",
            "请优先指出需要小心的地方。",
        ],
        markdown=True,
    )

    action_agent = model.create_agent(
        name="行动建议专家",
        role="负责给出可执行的下一步建议",
        instructions=[
            "你专注于把问题转化为可执行的建议。",
            "请优先给出清晰的小步行动方案。",
        ],
        markdown=True,
    )

    # broadcast 模式会把同一个问题同时交给所有成员，
    # 然后由 Team 统一汇总他们的观点。
    team = Team(
        name="Agno 广播协作团队",
        mode=TeamMode.broadcast,
        model=model.get_model(),
        members=[opportunity_agent, risk_agent, action_agent],
        instructions=[
            "你是团队协调者。",
            "请把同一个问题同时交给所有成员分析。",
            "最后把不同成员的观点汇总成一个清晰的结论。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "我已经学完 Team 的 coordinate 和 route。现在要不要马上进入 tasks 模式？请从机会、风险和行动建议三个角度一起分析。"
    )
```

### Broadcast 模式特点

```
用户请求 ──┬──→ 成员 A（机会分析）──┐
           ├──→ 成员 B（风险分析）──┼──→ 团队协调者整合 → 最终回答
           └──→ 成员 C（行动建议）──┘
```

### Broadcast vs Coordinate vs Route

| 模式 | 成员数量 | 结果处理 | 适用场景 |
|------|----------|----------|----------|
| Coordinate | 多个 | 整合所有结果 | 需要综合多方意见 |
| Route | 单个 | 直接返回 | 问题明确，只需一个专家 |
| Broadcast | 所有 | 汇总所有观点 | 需要多角度分析 |

---

## 3.4 Tasks 模式 ⭐⭐⭐⭐

**对应示例**：`examples/21_team_tasks_basics.py`

### 学习目标

- 理解 Tasks 任务管理模式
- 掌握跨 Agent 的任务分配和跟踪
- 学会管理复杂的多步骤任务

### 核心概念

**Tasks**：任务模式，支持将复杂任务拆分为子任务，分配给不同成员执行，并跟踪任务状态。

---

## 3.5 共享知识 ⭐⭐⭐⭐

**对应示例**：`examples/22_team_shared_knowledge.py`

### 学习目标

- 理解团队共享知识库的概念
- 掌握知识库在团队中的配置方法
- 学会让多个 Agent 共享同一知识源

### 核心概念

**Shared Knowledge**：团队成员共享同一知识库，确保信息一致性。

### 代码解析

```python
from pathlib import Path
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from models import OpenAICompatibleEmbedder, OpenAIModel

def build_team_knowledge() -> Knowledge:
    """构建供 Team 共享使用的知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_team_shared_knowledge"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_team_shared_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_team_shared_knowledge",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge

def run_team_shared_knowledge_example() -> None:
    """演示如何让 Team 共享同一个 Knowledge。"""
    model = OpenAIModel.from_env()
    knowledge = build_team_knowledge()

    concept_agent = model.create_agent(
        name="概念专家",
        role="负责解释概念和模块关系",
        instructions=[
            "你擅长解释 Agno 中不同模块的分工。",
            "请尽量把概念关系讲清楚。",
        ],
        markdown=True,
    )

    roadmap_agent = model.create_agent(
        name="路线规划专家",
        role="负责给出学习顺序和下一步行动建议",
        instructions=[
            "你擅长安排学习路线。",
            "请优先给出清晰的下一步学习安排。",
        ],
        markdown=True,
    )

    # Team 共享同一个 Knowledge，这样多个成员可以围绕同一份资料协作。
    team = Team(
        name="Agno 共享知识团队",
        mode=TeamMode.coordinate,
        model=model.get_model(),
        members=[concept_agent, roadmap_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是团队协调者。",
            "请基于共享知识库协调成员回答问题。",
            "最终答案要同时包含概念解释和下一步学习建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

    team.print_response(
        "请基于共享知识库，解释 Knowledge、Memory 和 Team 三者在 Agno 学习路径中的位置，并给我一个下一阶段学习建议。"
    )
```

### 共享知识 vs 独立知识

| 方式 | 说明 | 适用场景 |
|------|------|----------|
| 共享知识 | 所有成员访问同一知识库 | 需要信息一致性的协作 |
| 独立知识 | 每个成员有自己的知识库 | 不同领域的专业化分工 |

---

## 3.6 共享工具 ⭐⭐⭐⭐

**对应示例**：`examples/23_team_shared_tools.py`

### 学习目标

- 理解团队共享工具的概念
- 掌握工具在团队中的配置方法
- 学会让多个 Agent 共享工具能力

---

## 3.7 Tasks 与知识 ⭐⭐⭐⭐⭐

**对应示例**：`examples/24_team_tasks_with_knowledge.py`

### 学习目标

- 掌握 Tasks 与 Knowledge 的组合使用
- 学会构建知识驱动的任务系统
- 理解复杂协作场景的设计方法

---

# 第四阶段：集成与项目结构（25-26）

> 本阶段目标：学习如何将各种 Agno 组件整合到一个完整的应用中，并组织成可维护的项目结构。

---

## 4.1 应用骨架 ⭐⭐⭐⭐

**对应示例**：`examples/25_integrated_app_skeleton.py`

### 学习目标

- 理解 Agno 应用的整体架构
- 掌握组件整合的方法
- 学会构建可运行的应用骨架

### 核心概念

将前面学到的 Agent、Knowledge、Team 等组件整合到一个统一的应用中。

### 代码解析

```python
from pathlib import Path
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from models import OpenAICompatibleEmbedder, OpenAIModel

def estimate_topic_difficulty(topic: str) -> str:
    """根据主题给出一个简单的学习难度判断。"""
    difficulty_map = {
        "agent": "基础，适合作为入门主题。",
        "tools": "基础到中等，适合在掌握 Agent 后学习。",
        "knowledge": "中等，建议在 Tools 和基础 Agent 之后学习。",
        "team": "中等到进阶，建议在单 Agent 和 RAG 基础之后学习。",
        "rag": "中等到进阶，建议在 Knowledge 基础跑通后再做调优。",
    }
    return difficulty_map.get(
        topic.lower(),
        f"{topic} 建议先从最小可运行示例开始，再逐步扩展复杂度。",
    )

def suggest_next_module(current_stage: str) -> str:
    """根据当前阶段给出下一步建议。"""
    stage = current_stage.lower()
    if "team" in stage and "knowledge" in stage:
        return "下一步建议做真实项目骨架：把 Team、Knowledge、Tools 组合进一个稳定入口。"
    if "rag" in stage:
        return "下一步建议把 Knowledge 和 Team 结合起来，体验协作式 RAG。"
    return "下一步建议继续沿主线学习，并优先保持示例最小可运行。"

def build_shared_knowledge() -> Knowledge:
    """构建一个供综合示例使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`") from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_integrated_app"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档: {document_path}")

    embedder = OpenAICompatibleEmbedder.from_env()

    vector_db = ChromaDb(
        collection="agno_integrated_app_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=embedder.get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_integrated_app_knowledge",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge

def build_learning_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建一个共享知识库和工具的学习协作团队。"""
    research_agent = model_wrapper.create_agent(
        name="知识研究专家",
        role="负责从知识库中提取关键信息",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你擅长从知识库中提取与问题最相关的信息。",
            "请尽量基于资料内容总结，不要脱离资料随意扩展。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="学习规划专家",
        role="负责结合工具和知识库安排下一步学习路线",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_topic_difficulty, suggest_next_module],
        instructions=[
            "你擅长制定学习计划。",
            "当问题涉及难度或下一步安排时，请优先调用工具。",
        ],
        markdown=True,
    )

    return Team(
        name="Agno 综合学习团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[research_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,
        instructions=[
            "你是一个综合型学习团队协调者。",
            "请先根据共享知识库理解问题，再协调合适成员完成分析。",
            "最终答案需要同时包含知识解释、难度判断和下一步建议。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

def run_integrated_app_skeleton_example() -> None:
    """运行综合项目骨架示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_shared_knowledge()
    team = build_learning_team(model_wrapper, knowledge)

    team.print_response(
        "我已经学完 Agent、Tools、Knowledge 和 Team 的基础模式。"
        "请基于共享知识库和工具，帮我判断我现在学习 Team + Knowledge + Tools 组合课的难度，"
        "并给我一个下一步的学习建议。"
    )
```

### 应用架构

```
┌─────────────────────────────────────────┐
│              应用入口 (app.py)            │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ Team    │  │Knowledge│  │ Tools   │ │
│  │ 协调层  │←→│ 知识层  │←→│ 工具层  │ │
│  └────┬────┘  └─────────┘  └─────────┘ │
│       ↓                                 │
│  ┌─────────┐  ┌─────────┐              │
│  │ Agent A │  │ Agent B │  ...         │
│  └─────────┘  └─────────┘              │
│                                         │
└─────────────────────────────────────────┘
```

---

## 4.2 项目结构 ⭐⭐⭐⭐

**对应示例**：`examples/26_real_project_structure_basics.py`

### 学习目标

- 理解真实项目的目录结构
- 掌握模块化组织的方法
- 学会将应用拆分为可维护的模块

### 项目结构

```
study_assistant_app/
├── __init__.py          # 导出公共接口
├── app.py               # 应用入口
├── knowledge.py         # 知识库构建
├── team.py              # 团队配置
├── agents.py            # Agent 定义
└── settings.py          # 配置管理
```

### 模块化设计

```python
# study_assistant_app/__init__.py
"""学习助手项目骨架示例。"""
from .app import run_study_assistant_app
__all__ = ["run_study_assistant_app"]

# study_assistant_app/app.py
from models import OpenAIModel
from .knowledge import build_study_knowledge
from .team import build_study_team

def run_study_assistant_app() -> None:
    """运行模块化后的学习助手小应用。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_study_knowledge()
    team = build_study_team(model_wrapper, knowledge)

    team.print_response(
        "我已经学完了 Agent、Tools、Knowledge、Team 以及整合课。"
        "请结合共享知识库，帮我总结我现在处于什么阶段，"
        "这个阶段的学习难度如何，以及下一课最适合学什么。"
    )
```

---

# 第五阶段：Workflow（27-32）

> 本阶段目标：掌握 Agno 的 Workflow 系统，包括顺序、分组、条件、并行、循环等模式及其组合应用。

---

## 5.1 基础工作流 ⭐⭐⭐

**对应示例**：`examples/27_workflow_basics.py`

### 学习目标

- 理解 Workflow 的基本概念
- 掌握顺序步骤的执行流程
- 学会使用 Step 和 StepOutput

### 核心概念

- **Workflow**：工作流，由多个步骤组成的执行流程
- **Step**：步骤，工作流的基本执行单元
- **StepOutput**：步骤输出，表示一个步骤的执行结果
- **executor**：执行器，可以是 Agent 或函数

### 代码解析

```python
from agno.workflow import Step, StepOutput, Workflow
from models import OpenAIModel

def extract_stage_summary(step_input) -> StepOutput:
    """从前一个步骤输出里整理出更适合继续规划的阶段摘要。"""
    previous_content = step_input.previous_step_content or ""

    summary = (
        "当前学习阶段摘要：\n"
        f"{previous_content}\n\n"
        "请在后续步骤里基于这份摘要继续给出更清晰的学习建议。"
    )
    return StepOutput(content=summary, success=True)

def run_workflow_basics_example() -> None:
    """运行最基础的顺序型 Workflow 示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责判断用户当前处于什么学习阶段。",
        instructions=[
            "请根据用户提供的学习进度，判断当前所处阶段。",
            "输出时请给出阶段名称、已经掌握的重点、当前最需要巩固的能力。",
        ],
        markdown=True,
    )

    lesson_planner = model_wrapper.create_agent(
        name="课程规划员",
        role="负责基于前面步骤的结果安排下一课。",
        instructions=[
            "你会收到前一个步骤整理好的学习阶段摘要。",
            "请基于摘要给出下一课建议，并说明为什么这样安排。",
            "回答尽量清晰、具体，适合继续按课程节奏学习。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Workflow 基础课",
        description="用顺序步骤把学习阶段分析和下一课规划串起来。",
        steps=[
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前进度处于哪一个学习阶段。",
            ),
            Step(
                name="摘要整理",
                executor=extract_stage_summary,
                description="把上一步结果整理成更适合继续规划的摘要。",
            ),
            Step(
                name="下一课规划",
                agent=lesson_planner,
                description="基于前面步骤输出安排下一课。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team，"
            "并且完成了整合课和真实项目骨架深化课。"
            "请帮我判断我现在处于什么阶段，并安排下一课。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Workflow 执行流程

```
输入 → Step 1 (Agent) → Step 2 (函数) → Step 3 (Agent) → 输出
         ↓                  ↓                  ↓
      阶段分析            摘要整理            下一课规划
```

### Step 类型

| 类型 | 说明 |
|------|------|
| Agent Step | 使用 Agent 执行，配置 `agent` 参数 |
| 函数 Step | 使用函数执行，配置 `executor` 参数 |

---

## 5.2 分组步骤 ⭐⭐⭐

**对应示例**：`examples/28_workflow_grouped_steps.py`

### 学习目标

- 理解 Steps 分组的概念
- 掌握可复用流程的封装方法
- 学会组织复杂的多步骤工作流

### 核心概念

**Steps**：步骤组，将多个相关步骤封装为一个可复用的单元，可以在不同的 Workflow 中复用。

### 代码解析

```python
from agno.workflow import Step, StepOutput, Steps, Workflow
from models import OpenAIModel

def build_stage_brief(step_input) -> StepOutput:
    """把阶段分析结果整理成更适合继续规划的简报。"""
    stage_analysis = step_input.get_step_content("阶段分析") or step_input.previous_step_content or ""
    brief = (
        "学习阶段简报：\n"
        f"{stage_analysis}\n\n"
        "下面请继续基于这份简报，拆出下一课规划所需的关键点。"
    )
    return StepOutput(content=brief, success=True)

def extract_planning_focus(step_input) -> StepOutput:
    """从阶段简报里提炼下一课规划重点。"""
    brief = step_input.get_step_content("简报") or step_input.previous_step_content or ""
    focus = (
        "下一课规划重点：\n"
        f"{brief}\n\n"
        "请优先安排一个既能承接当前阶段、又能自然扩展后续能力的主题。"
    )
    return StepOutput(content=focus, success=True)

def run_workflow_grouped_steps_example() -> None:
    """运行 Grouped Steps 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责判断用户当前处于哪个学习阶段。",
        instructions=[
            "请根据用户已经学过的内容判断当前学习阶段。",
            "输出时请说明当前阶段、已经掌握的重点、下一阶段最值得切入的方向。",
        ],
        markdown=True,
    )

    lesson_planner = model_wrapper.create_agent(
        name="课程规划员",
        role="负责根据步骤组整理出的重点安排下一课。",
        instructions=[
            "你会收到一个由步骤组整理好的规划重点。",
            "请基于这些重点给出下一课建议，并说明为什么这样安排。",
            "输出尽量清晰，适合作为继续学习的课程安排。",
        ],
        markdown=True,
    )

    # 将多个相关步骤封装成一个可复用的 Steps 组
    planning_steps = Steps(
        name="下一课规划步骤组",
        description="把阶段分析结果整理成更适合生成课程建议的中间信息。",
        steps=[
            Step(
                name="阶段简报",
                executor=build_stage_brief,
                description="先把阶段分析整理成一份简报。",
            ),
            Step(
                name="规划重点提炼",
                executor=extract_planning_focus,
                description="再从简报里提炼下一课规划重点。",
            ),
        ],
    )

    workflow = Workflow(
        name="Agno Grouped Steps 基础课",
        description="学习如何把多个顺序步骤封装成一个可复用的步骤组。",
        steps=[
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前学习进度所处阶段。",
            ),
            planning_steps,
            Step(
                name="下一课规划",
                agent=lesson_planner,
                description="基于步骤组整理出的重点安排下一课。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经完成了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及最基础的 Workflow 顺序课。"
            "请帮我判断我现在的学习阶段，并安排下一课。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Steps vs Step

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| Step | 单个步骤 | 简单的顺序执行 |
| Steps | 步骤组 | 将多个步骤封装为可复用单元 |

### 执行流程

```
输入 → Step（阶段分析）→ Steps（下一课规划步骤组）→ Step（下一课规划）→ 输出
                              ├─ Step（阶段简报）
                              └─ Step（规划重点提炼）
```

---

## 5.3 条件分支 ⭐⭐⭐⭐

**对应示例**：`examples/29_workflow_condition_basics.py`

### 学习目标

- 理解条件分支的工作原理
- 掌握评估函数的编写方法
- 学会设计动态执行路径

### 核心概念

**Condition**：条件步骤，根据评估函数的结果决定执行哪个分支。

### 代码解析

```python
from agno.workflow import Condition, Step, StepOutput, Workflow
from models import OpenAIModel

def should_take_advanced_branch(step_input) -> bool:
    """根据前一步的阶段分析结果判断是否进入进阶分支。"""
    stage_analysis = str(step_input.get_step_content("阶段分析") or "")
    advanced_keywords = ["workflow", "团队", "team", "进阶", "骨架", "整合"]
    return any(keyword in stage_analysis.lower() for keyword in advanced_keywords)

def prepare_beginner_path(step_input) -> StepOutput:
    """整理更适合巩固型学习的下一课建议。"""
    stage_analysis = step_input.get_step_content("阶段分析") or ""
    content = (
        "当前更适合走巩固分支。\n"
        f"阶段分析参考：\n{stage_analysis}\n\n"
        "建议先补强当前阶段的基础理解，再进入更复杂的 Workflow 模式。"
    )
    return StepOutput(content=content, success=True)

def prepare_advanced_path(step_input) -> StepOutput:
    """整理更适合进阶型学习的下一课建议。"""
    stage_analysis = step_input.get_step_content("阶段分析") or ""
    content = (
        "当前更适合走进阶分支。\n"
        f"阶段分析参考：\n{stage_analysis}\n\n"
        "建议继续学习带条件分支、并行和循环的 Workflow，逐步进入更复杂的流程编排。"
    )
    return StepOutput(content=content, success=True)

def run_workflow_condition_basics_example() -> None:
    """运行 Condition 条件分支 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责判断当前学习阶段，并给出阶段特征。",
        instructions=[
            "请根据用户已经完成的课程判断当前学习阶段。",
            "回答时请说明当前阶段、已掌握重点，以及接下来更适合巩固还是继续进阶。",
        ],
        markdown=True,
    )

    final_planner = model_wrapper.create_agent(
        name="分支总结规划员",
        role="负责结合分支结果给出最终下一课建议。",
        instructions=[
            "你会收到前面步骤生成的分支建议。",
            "请基于分支结果给出最终下一课安排，并说明为什么这样安排。",
            "输出要清晰，适合作为继续学习的课程建议。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Condition Workflow 基础课",
        description="学习如何根据条件判断执行不同分支。",
        steps=[
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前学习阶段。",
            ),
            Condition(
                name="学习路径分支",
                description="根据阶段分析结果判断走巩固分支还是进阶分支。",
                evaluator=should_take_advanced_branch,
                steps=[
                    Step(
                        name="进阶路径建议",
                        executor=prepare_advanced_path,
                        description="当阶段已经进入进阶区间时，生成进阶路径建议。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径建议",
                        executor=prepare_beginner_path,
                        description="当阶段仍需要巩固时，生成巩固路径建议。",
                    )
                ],
            ),
            Step(
                name="最终下一课规划",
                agent=final_planner,
                description="综合分支结果，给出最终下一课安排。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及 Workflow 的基础课和 Steps 课程。"
            "请判断我现在应该走巩固分支还是进阶分支，并安排下一课。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Condition 执行流程

```
输入 → 阶段分析 → Condition 评估
                    ├─ True  → 进阶路径建议 ─┐
                    └─ False → 巩固路径建议 ─┤
                                              ↓
                                    最终下一课规划 → 输出
```

### Condition 关键参数

| 参数 | 说明 |
|------|------|
| `evaluator` | 评估函数，返回 `bool` 决定走哪个分支 |
| `steps` | 条件为 `True` 时执行的步骤 |
| `else_steps` | 条件为 `False` 时执行的步骤 |

---

## 5.4 并行执行 ⭐⭐⭐⭐

**对应示例**：`examples/30_workflow_parallel_basics.py`

### 学习目标

- 理解并行执行的工作原理
- 掌握 Parallel 步骤的配置方法
- 学会整合并行执行的结果

### 核心概念

**Parallel**：并行步骤，让多个独立步骤同时执行，提高效率。

### 代码解析

```python
from agno.workflow import Parallel, Step, Workflow
from models import OpenAIModel

def run_workflow_parallel_basics_example() -> None:
    """运行 Parallel 并行 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    capability_analyst = model_wrapper.create_agent(
        name="能力盘点分析员",
        role="负责分析当前已经掌握的能力。",
        instructions=[
            "请根据用户已经完成的学习内容，梳理当前已经掌握的核心能力。",
            "输出时尽量按要点整理，帮助后续步骤快速使用。",
        ],
        markdown=True,
    )

    next_stage_analyst = model_wrapper.create_agent(
        name="下一阶段分析员",
        role="负责分析当前最值得继续推进的方向。",
        instructions=[
            "请根据用户当前进度，判断下一阶段最值得继续推进的主题。",
            "输出时请说明为什么这个方向最适合现在继续学习。",
        ],
        markdown=True,
    )

    final_planner = model_wrapper.create_agent(
        name="并行结果汇总员",
        role="负责整合多个并行分支的结果，给出最终学习建议。",
        instructions=[
            "你会收到多个并行步骤的分析结果。",
            "请整合这些结果，给出一份清晰的下一课建议。",
            "最终回答要同时包含：当前能力总结、下一阶段重点、下一课安排。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Parallel Workflow 基础课",
        description="学习如何让多个独立步骤并行执行，再统一汇总结果。",
        steps=[
            Parallel(
                Step(
                    name="能力盘点",
                    agent=capability_analyst,
                    description="并行分析当前已经掌握的能力。",
                ),
                Step(
                    name="下一阶段重点分析",
                    agent=next_stage_analyst,
                    description="并行分析下一阶段最值得推进的方向。",
                ),
                name="并行分析阶段",
                description="让多个独立分析步骤同时执行。",
            ),
            Step(
                name="最终并行汇总",
                agent=final_planner,
                description="整合并行阶段结果，生成最终下一课建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及 Workflow 的基础课、Steps 和 Condition。"
            "请并行分析我当前已经掌握的能力和下一阶段最适合继续推进的方向，"
            "然后给我一个最终的下一课建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Parallel 执行流程

```
输入 ─┬─→ 能力盘点 ──┐
      │              ├─→ 最终并行汇总 → 输出
      └─→ 下一阶段 ──┘
          重点分析
```

---

## 5.5 循环执行 ⭐⭐⭐⭐

**对应示例**：`examples/31_workflow_loop_basics.py`

### 学习目标

- 理解循环执行的工作原理
- 掌握 Loop 步骤的配置方法
- 学会设置终止条件和最大迭代次数

### 核心概念

**Loop**：循环步骤，重复执行同一组步骤，直到满足终止条件或达到最大迭代次数。

### 代码解析

```python
from agno.workflow import Loop, Step, StepOutput, Workflow
from models import OpenAIModel

def expand_study_plan(step_input) -> StepOutput:
    """模拟按轮次逐步细化学习计划。"""
    previous_content = str(step_input.previous_step_content or "")

    if "第1轮迭代完成" not in previous_content:
        content = (
            "第1轮迭代完成。\n"
            "当前先给出一个基础学习计划：\n"
            "1. 回顾 Workflow 的顺序、分组、条件、并行四种模式。\n"
            "2. 明确下一步要学习循环执行模式。\n"
            "3. 先建立 Loop 的使用直觉，再继续复杂组合。\n"
        )
    else:
        content = (
            "第2轮迭代完成。\n"
            "在上一轮基础上进一步细化学习计划：\n"
            "1. 先理解 Loop 会重复执行同一组步骤。\n"
            "2. 再理解 max_iterations 和 end_condition 的关系。\n"
            "3. 最后观察 forward_iteration_output 如何把上一轮结果传给下一轮。\n"
            "4. 学完后继续进入更复杂的 Workflow 组合模式。\n"
        )

    return StepOutput(content=content, success=True)

def is_loop_good_enough(outputs: list[StepOutput]) -> bool:
    """当迭代计划已经进入第二轮细化时结束循环。"""
    for output in outputs:
        if output.content and "第2轮迭代完成" in str(output.content):
            return True
    return False

def run_workflow_loop_basics_example() -> None:
    """运行 Loop 循环 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    final_planner = model_wrapper.create_agent(
        name="循环结果汇总员",
        role="负责整合多轮迭代结果，给出最终学习建议。",
        instructions=[
            "你会收到 Loop 多轮迭代后的结果。",
            "请基于最终迭代内容，输出一份清晰的下一课学习建议。",
            "回答需要说明：本轮学习重点、为什么这样安排、下一步继续学什么。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Loop Workflow 基础课",
        description="学习如何通过循环步骤逐轮细化同一个任务。",
        steps=[
            Loop(
                name="学习计划细化循环",
                description="重复执行同一步骤，逐轮把学习计划变得更具体。",
                steps=[
                    Step(
                        name="学习计划迭代器",
                        executor=expand_study_plan,
                        description="每一轮都把学习计划再细化一点。",
                    )
                ],
                max_iterations=3,
                end_condition=is_loop_good_enough,
                forward_iteration_output=True,
            ),
            Step(
                name="最终循环汇总",
                agent=final_planner,
                description="整合循环后的最终结果，给出下一课建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition 和 Parallel。"
            "请用循环方式逐轮细化我的下一阶段学习计划，"
            "然后给我一个最终的下一课建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Loop 执行流程

```
输入 → Loop 开始
         ↓
       迭代 1 → 检查终止条件 → 未满足
         ↓
       迭代 2 → 检查终止条件 → 满足 → 退出循环
         ↓
       最终循环汇总 → 输出
```

### Loop 关键参数

| 参数 | 说明 |
|------|------|
| `steps` | 循环执行的步骤列表 |
| `max_iterations` | 最大迭代次数 |
| `end_condition` | 终止条件函数，返回 `True` 时停止循环 |
| `forward_iteration_output` | 是否将上一轮输出传递给下一轮 |

---

## 5.6 多模式组合 ⭐⭐⭐⭐⭐

**对应示例**：`examples/32_workflow_multi_pattern_basics.py`

### 学习目标

- 理解复杂工作流的组合模式
- 掌握 Condition + Parallel + Loop 的嵌套使用
- 学会设计企业级工作流系统

### 核心概念

多模式组合是将 Condition、Parallel、Loop 等模式嵌套使用，构建复杂的执行流程。

### 代码解析

```python
from agno.workflow import Condition, Loop, Parallel, Step, StepOutput, Workflow
from models import OpenAIModel

def should_use_advanced_path(step_input) -> bool:
    """根据输入判断是否进入进阶学习路径。"""
    user_input = (step_input.input or "").lower()
    advanced_keywords = ["workflow", "parallel", "condition", "loop", "team", "knowledge"]
    return any(keyword in user_input for keyword in advanced_keywords)

def build_beginner_direction(step_input) -> StepOutput:
    """生成更适合巩固阶段的方向说明。"""
    content = (
        "当前进入巩固路径。\n"
        "建议优先回顾已经学过的基础模式，确保对顺序、条件、并行、循环的差别足够清楚。"
    )
    return StepOutput(content=content, success=True)

def build_advanced_direction(step_input) -> StepOutput:
    """生成更适合进阶阶段的方向说明。"""
    content = (
        "当前进入进阶路径。\n"
        "建议开始学习如何把多种 Workflow 模式组合在同一个真实流程里。"
    )
    return StepOutput(content=content, success=True)

def refine_combined_plan(step_input) -> StepOutput:
    """把前面汇总的计划再细化一轮。"""
    previous_content = str(step_input.previous_step_content or "")

    if "第1轮细化完成" not in previous_content:
        content = (
            "第1轮细化完成。\n"
            "建议下一步先做一节多模式组合课，重点观察 Condition、Parallel、Loop 如何串联。\n"
            "再继续尝试把 Workflow 和 Team、Knowledge 组合起来。"
        )
    else:
        content = (
            "第2轮细化完成。\n"
            "最终学习建议：\n"
            "1. 先掌握多模式组合 Workflow。\n"
            "2. 再进入 Workflow + Team。\n"
            "3. 最后进入 Workflow + Knowledge，做更接近真实项目的编排。"
        )

    return StepOutput(content=content, success=True)

def run_workflow_multi_pattern_basics_example() -> None:
    """运行多模式组合 Workflow 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    stage_analyst = model_wrapper.create_agent(
        name="学习阶段分析员",
        role="负责分析当前学习阶段。",
        instructions=[
            "请根据用户已经完成的课程，判断当前学习阶段。",
            "输出时请说明当前阶段、已掌握重点，以及当前最适合继续推进的方向。",
        ],
        markdown=True,
    )

    final_planner = model_wrapper.create_agent(
        name="多模式结果汇总员",
        role="负责整合多模式组合结果，给出最终学习建议。",
        instructions=[
            "你会收到多模式 Workflow 的执行结果。",
            "请基于所有分析结果，输出一份清晰的最终学习建议。",
            "回答需要说明：当前阶段总结、推荐的学习路径、下一课安排。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno 多模式组合 Workflow 基础课",
        description="学习如何把 Condition、Parallel、Loop 组合到同一个 Workflow 里。",
        steps=[
            # 第一步：阶段分析
            Step(
                name="阶段分析",
                agent=stage_analyst,
                description="先分析当前学习阶段。",
            ),

            # 第二步：条件分支判断学习路径
            Condition(
                name="学习路径判断",
                description="根据输入判断走巩固路径还是进阶路径。",
                evaluator=should_use_advanced_path,
                steps=[
                    Step(
                        name="进阶路径方向",
                        executor=build_advanced_direction,
                        description="当输入包含进阶关键词时，生成进阶方向说明。",
                    )
                ],
                else_steps=[
                    Step(
                        name="巩固路径方向",
                        executor=build_beginner_direction,
                        description="当输入更适合巩固时，生成巩固方向说明。",
                    )
                ],
            ),

            # 第三步：并行分析多个维度
            Parallel(
                Step(
                    name="并行能力盘点",
                    agent=stage_analyst,
                    description="并行分析当前已掌握的能力。",
                ),
                Step(
                    name="并行方向分析",
                    agent=stage_analyst,
                    description="并行分析最适合继续推进的方向。",
                ),
                name="并行分析阶段",
                description="同时分析多个维度。",
            ),

            # 第四步：循环细化学习计划
            Loop(
                name="学习计划细化循环",
                description="通过循环逐步细化学习计划。",
                steps=[
                    Step(
                        name="计划细化器",
                        executor=refine_combined_plan,
                        description="每一轮都把学习计划再细化一点。",
                    )
                ],
                max_iterations=3,
                end_condition=lambda outputs: any(
                    "第2轮细化完成" in str(o.content) for o in outputs
                ),
                forward_iteration_output=True,
            ),

            # 第五步：最终汇总
            Step(
                name="最终多模式汇总",
                agent=final_planner,
                description="整合多模式组合结果，生成最终学习建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Agent、Tools、Knowledge、Team、整合课、"
            "真实项目骨架深化课，以及 Workflow 的基础课、Steps、Condition、Parallel 和 Loop。"
            "请用多模式组合的方式帮我分析当前阶段，并给出最终学习建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### 多模式组合执行流程

```
输入 → 阶段分析 → Condition 判断
                    ├─ 进阶路径 ─┐
                    └─ 巩固路径 ─┤
                                 ↓
                       Parallel 并行分析
                         ├─ 能力盘点
                         └─ 方向分析
                                 ↓
                       Loop 循环细化
                         ├─ 迭代 1
                         └─ 迭代 2
                                 ↓
                       最终汇总 → 输出
```

---

## 5.7 Workflow + Team ⭐⭐⭐⭐⭐

**对应示例**：`examples/33_workflow_team_basics.py`

### 学习目标

- 理解 Workflow 和 Team 的集成方式
- 掌握在 Workflow 中使用 Team 作为步骤
- 学会构建复杂的协作式工作流

### 核心概念

**Workflow + Team**：将 Team 作为 Workflow 的一个步骤，实现复杂的协作式工作流。Workflow 负责控制整体流程节奏，Team 负责完成其中一个协作分析阶段。

### 代码解析

```python
from agno.team import Team, TeamMode
from agno.workflow import Step, Workflow
from models import OpenAIModel

def build_study_team(model_wrapper: OpenAIModel) -> Team:
    """构建一个专门用于学习规划的协作团队。"""
    concept_agent = model_wrapper.create_agent(
        name="概念讲解成员",
        role="负责解释当前阶段最重要的概念重点。",
        instructions=[
            "请根据用户当前进度，解释当前阶段最需要理解的核心概念。",
            "输出要清晰、简洁，方便后续步骤继续使用。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="课程规划成员",
        role="负责给出下一阶段学习安排。",
        instructions=[
            "请根据用户当前进度，给出下一阶段最值得优先学习的课程安排。",
            "输出要说明为什么这样安排。",
        ],
        markdown=True,
    )

    return Team(
        name="Workflow 学习协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, planning_agent],
        instructions=[
            "你是一个学习协作团队。",
            "请协调不同成员，从概念理解和课程安排两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

def run_workflow_team_basics_example() -> None:
    """运行 Workflow + Team 入门示例。"""
    model_wrapper = OpenAIModel.from_env()

    kickoff_agent = model_wrapper.create_agent(
        name="流程启动员",
        role="负责识别当前学习请求的背景。",
        instructions=[
            "请先简要识别用户当前已经学到什么位置，以及这次请求的目标。",
            "输出尽量简洁，作为后续团队协作的上下文。",
        ],
        markdown=True,
    )

    summary_agent = model_wrapper.create_agent(
        name="流程总结员",
        role="负责整合 Team 的结果，给出最终学习建议。",
        instructions=[
            "你会收到前面 Workflow 和 Team 阶段的结果。",
            "请整合这些信息，给出最终下一课建议，并说明后续主线安排。",
        ],
        markdown=True,
    )

    study_team = build_study_team(model_wrapper)

    workflow = Workflow(
        name="Agno Workflow + Team 基础课",
        description="学习如何在 Workflow 中把某个阶段交给 Team 协作完成。",
        steps=[
            Step(
                name="流程启动分析",
                agent=kickoff_agent,
                description="先识别当前学习背景和本次请求目标。",
            ),
            Step(
                name="团队协作分析",
                team=study_team,
                description="把核心分析阶段交给 Team 协作完成。",
            ),
            Step(
                name="最终流程总结",
                agent=summary_agent,
                description="整合 Workflow 和 Team 阶段结果，生成最终建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop，"
            "以及多模式组合课。请用 Workflow + Team 的方式帮我安排下一阶段学习。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Workflow + Team 执行流程

```
输入 → 流程启动分析 → 团队协作分析 → 最终流程总结 → 输出
                          │
                          ├─ 概念讲解成员
                          └─ 课程规划成员
```

### 关键参数

| 参数 | 说明 |
|------|------|
| `team` | 在 Step 中使用 `team` 参数指定 Team 实例 |
| `agent` | 在 Step 中使用 `agent` 参数指定单个 Agent |
| `executor` | 在 Step 中使用 `executor` 参数指定函数执行器 |

### Step 类型总结

| 类型 | 参数 | 说明 |
|------|------|------|
| Agent Step | `agent` | 单个 Agent 执行 |
| Team Step | `team` | Team 协作执行 |
| 函数 Step | `executor` | 函数执行 |

---

## 5.8 Workflow + Knowledge ⭐⭐⭐⭐⭐

**对应示例**：`examples/34_workflow_knowledge_basics.py`

### 学习目标

- 理解 Workflow 和 Knowledge 的集成方式
- 掌握在 Workflow 步骤中使用知识库检索
- 学会构建 "编排 + 资料供给" 的工作流模式

### 核心概念

**Workflow + Knowledge**：在 Workflow 的某个阶段显式接入知识库检索，先检索再继续规划。Workflow 负责编排，Knowledge 负责供给资料。

### 代码解析

```python
from pathlib import Path
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.search import SearchType
from agno.workflow import Step, Workflow
from models import OpenAICompatibleEmbedder, OpenAIModel

def build_workflow_knowledge() -> Knowledge:
    """构建供 Workflow 示例使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_workflow_knowledge"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档：{document_path}")

    vector_db = ChromaDb(
        collection="agno_workflow_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_workflow_knowledge",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge

def run_workflow_knowledge_basics_example() -> None:
    """运行 Workflow + Knowledge 入门示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_workflow_knowledge()

    retrieval_agent = model_wrapper.create_agent(
        name="资料检索员",
        role="负责先从知识库中找到和问题最相关的资料。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请先根据用户问题检索知识库。",
            "输出时优先总结和当前问题最相关的知识点。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="知识规划员",
        role="负责基于检索结果给出下一阶段学习建议。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你会收到前面步骤检索出的关键知识点。",
            "请基于这些内容给出下一阶段学习建议。",
            "回答里要同时说明：当前最该理解什么，以及下一课适合学什么。",
        ],
        markdown=True,
    )

    workflow = Workflow(
        name="Agno Workflow + Knowledge 基础课",
        description="学习如何让 Workflow 在某个阶段显式使用共享知识库。",
        steps=[
            Step(
                name="知识检索阶段",
                agent=retrieval_agent,
                description="先从知识库中检索和当前问题最相关的资料。",
            ),
            Step(
                name="知识规划阶段",
                agent=planning_agent,
                description="再基于检索结果生成下一阶段学习建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop、"
            "多模式组合课，以及 Workflow + Team。"
            "请基于知识库先检索当前最相关的学习重点，再给我下一阶段学习建议。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Workflow + Knowledge 执行流程

```
输入 → 知识检索阶段（Agent + Knowledge）→ 知识规划阶段（Agent + Knowledge）→ 输出
                        │                            │
                        └─ 检索知识库                 └─ 基于检索结果规划
```

### 关键参数

| 参数 | 说明 |
|------|------|
| `knowledge` | 在 Agent 中使用 `knowledge` 参数指定知识库 |
| `search_knowledge` | 是否开启知识库自动检索 |
| `add_knowledge_to_context` | 是否将检索结果加入上下文 |

### Workflow 集成模式总结

| 模式 | 说明 | 示例 |
|------|------|------|
| Workflow + Team | 在 Workflow 中使用 Team 完成协作阶段 | 示例 33 |
| Workflow + Knowledge | 在 Workflow 中使用 Knowledge 完成资料检索 | 示例 34 |
| Workflow + Team + Knowledge | 三者结合，构建完整的协作式知识驱动工作流 | 示例 35 |

---

## 5.9 Workflow + Team + Knowledge ⭐⭐⭐⭐⭐

**对应示例**：`examples/35_workflow_team_knowledge_basics.py`

### 学习目标

- 掌握 Workflow、Team、Knowledge 三者的组合使用
- 理解 "编排 + 协作 + 知识供给" 的完整工作流模式
- 学会构建更接近真实项目的最小工作流

### 核心概念

**Workflow + Team + Knowledge**：Workflow 负责整体编排，Team 负责协作分析，Knowledge 负责提供共享资料。三者一起构成更接近真实项目的最小工作流。

### 代码解析

```python
from pathlib import Path
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from agno.workflow import Step, Workflow
from models import OpenAICompatibleEmbedder, OpenAIModel

def build_team_workflow_knowledge() -> Knowledge:
    """构建供 Workflow + Team + Knowledge 示例使用的共享知识库。"""
    try:
        from agno.vectordb.chroma import ChromaDb
    except ImportError as exc:
        raise ImportError(
            "运行这个示例前，请先安装知识库依赖：`uv pip install -U chromadb`"
        ) from exc

    project_root = Path(__file__).resolve().parents[1]
    knowledge_dir = project_root / "knowledge_docs"
    vector_db_dir = project_root / "tmp" / "chromadb_workflow_team_knowledge"
    vector_db_dir.mkdir(parents=True, exist_ok=True)

    documents = [
        knowledge_dir / "agno_rag_basics.md",
        knowledge_dir / "agno_tools_notes.md",
        knowledge_dir / "agno_memory_notes.md",
        knowledge_dir / "agno_beginner_track.md",
        knowledge_dir / "agno_advanced_track.md",
    ]

    for document_path in documents:
        if not document_path.exists():
            raise FileNotFoundError(f"没有找到知识库文档：{document_path}")

    vector_db = ChromaDb(
        collection="agno_workflow_team_knowledge",
        path=str(vector_db_dir),
        persistent_client=True,
        embedder=OpenAICompatibleEmbedder.from_env().get_embedder(),
        search_type=SearchType.hybrid,
    )

    knowledge = Knowledge(
        name="agno_workflow_team_knowledge",
        vector_db=vector_db,
    )

    reader = MarkdownReader(chunk_size=1200)
    for document_path in documents:
        knowledge.insert(
            path=str(document_path),
            reader=reader,
            upsert=True,
        )

    return knowledge

def build_knowledge_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建围绕共享知识库协作分析的团队。"""
    concept_agent = model_wrapper.create_agent(
        name="知识概念成员",
        role="负责解释当前问题里最重要的概念关系。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请先基于共享知识库解释当前最关键的概念。",
            "回答时优先使用知识库里能支撑当前问题的内容。",
        ],
        markdown=True,
    )

    roadmap_agent = model_wrapper.create_agent(
        name="学习路线成员",
        role="负责基于共享知识库安排下一阶段学习路线。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请根据共享知识库里的资料，给出下一阶段最适合的学习安排。",
            "回答时说明为什么这样安排。",
        ],
        markdown=True,
    )

    return Team(
        name="Workflow 知识协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, roadmap_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "你是一个围绕共享知识库协作的学习团队。",
            "请协调不同成员，从概念理解和路线规划两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

def run_workflow_team_knowledge_basics_example() -> None:
    """运行 Workflow + Team + Knowledge 入门示例。"""
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_team_workflow_knowledge()

    kickoff_agent = model_wrapper.create_agent(
        name="流程背景整理员",
        role="负责识别当前学习背景和本次目标。",
        instructions=[
            "请先识别用户当前已经学到了哪里，以及这次请求想解决什么问题。",
            "输出尽量简洁，作为后续知识协作阶段的上下文。",
        ],
        markdown=True,
    )

    summary_agent = model_wrapper.create_agent(
        name="最终建议汇总员",
        role="负责整合 Workflow、Team 和 Knowledge 阶段结果。",
        instructions=[
            "你会收到前面流程的背景整理结果，以及团队基于知识库的协作结果。",
            "请整合这些信息，给出最终的下一阶段学习建议。",
        ],
        markdown=True,
    )

    knowledge_team = build_knowledge_team(model_wrapper, knowledge)

    workflow = Workflow(
        name="Agno Workflow + Team + Knowledge 基础课",
        description="学习如何把 Workflow、Team、Knowledge 三者组合在同一个工作流里。",
        steps=[
            Step(
                name="流程背景整理",
                agent=kickoff_agent,
                description="先识别当前学习背景和本次目标。",
            ),
            Step(
                name="知识协作分析阶段",
                team=knowledge_team,
                description="让 Team 基于共享知识库协作完成核心分析。",
            ),
            Step(
                name="最终综合建议",
                agent=summary_agent,
                description="整合流程背景和知识协作结果，给出最终建议。",
            ),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop、"
            "多模式组合课，以及 Workflow + Team 和 Workflow + Knowledge。"
            "请用 Workflow + Team + Knowledge 的方式，帮我安排下一阶段学习。"
        ),
        markdown=True,
        stream=True,
        show_step_details=True,
    )
```

### Workflow + Team + Knowledge 执行流程

```
输入 → 流程背景整理（Agent）→ 知识协作分析阶段（Team + Knowledge）→ 最终综合建议（Agent）→ 输出
                                      │
                                      ├─ 知识概念成员
                                      └─ 学习路线成员
                                      （均共享 Knowledge）
```

### 三者职责分工

| 组件 | 职责 | 关键参数 |
|------|------|----------|
| Workflow | 整体编排，控制流程节奏 | `steps=[]` |
| Team | 协作分析，多成员协调 | `team=knowledge_team` |
| Knowledge | 资料供给，知识库检索 | `knowledge=knowledge`, `search_knowledge=True` |

### 架构层级

```
┌─────────────────────────────────────────────────┐
│              Workflow（整体编排）                  │
├─────────────────────────────────────────────────┤
│  Step 1      │  Step 2              │  Step 3   │
│  Agent       │  Team + Knowledge    │  Agent    │
│  （背景整理） │  （协作分析）         │  （汇总） │
│              │  ├─ 成员 A           │           │
│              │  └─ 成员 B           │           │
│              │     └─ 共享 Knowledge │           │
└─────────────────────────────────────────────────┘
```

---

## 5.10 真实项目小型工作流 ⭐⭐⭐⭐⭐

**对应示例**：`examples/36_learning_assistant_mini_workflow.py`

### 学习目标

- 掌握将 Condition、函数 Step、Team、Knowledge 组合为一个完整工作流
- 学会使用 `evaluator` 函数做运行时路径判断
- 学会使用 `executor` 函数做函数式 Step
- 体验更接近真实项目的多阶段工作流设计

### 核心概念

**真实项目小型工作流**：将前面学到的所有模式（Condition、函数 Step、Team + Knowledge、Custom Tools）组合到一个工作流中，模拟真实项目中的多阶段、多模式编排需求。

### 代码解析

```python
from pathlib import Path
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.team import Team, TeamMode
from agno.vectordb.search import SearchType
from agno.workflow import Condition, Step, StepOutput, Workflow
from models import OpenAICompatibleEmbedder, OpenAIModel

# ── 1. 自定义工具函数 ─────────────────────────────────

def estimate_weekly_effort(stage_name: str) -> str:
    """根据阶段给出建议的每周投入。"""
    stage = stage_name.lower()
    if "advanced" in stage or "workflow" in stage:
        return "建议每周投入 4 到 6 小时，保持连续练习。"
    if "beginner" in stage:
        return "建议每周投入 2 到 4 小时，先保证基础跑通。"
    return "建议每周投入 3 到 5 小时，根据理解速度动态调整。"

def suggest_output_style(goal: str) -> str:
    """根据目标给出更合适的学习产出形式。"""
    lowered_goal = goal.lower()
    if "workflow" in lowered_goal:
        return "更适合的产出是一个最小可运行工作流示例。"
    if "knowledge" in lowered_goal:
        return "更适合的产出是一个带知识库检索的可运行示例。"
    return "更适合的产出是一个能跑通的最小示例加一份阶段总结。"

# ── 2. Condition evaluator 和 executor ────────────────

def needs_advanced_path(step_input) -> bool:
    """根据当前输入判断是否进入进阶学习路径。"""
    user_input = (step_input.input or "").lower()
    advanced_keywords = ["workflow", "team", "knowledge", "parallel", "loop", "condition"]
    return any(keyword in user_input for keyword in advanced_keywords)

def build_beginner_path_note(step_input) -> StepOutput:
    """生成巩固路径说明。"""
    return StepOutput(
        content=(
            "当前进入巩固路径。\n"
            "建议先回顾已学模式的边界和职责，再逐步进入更完整的小型工作流。"
        ),
        success=True,
    )

def build_advanced_path_note(step_input) -> StepOutput:
    """生成进阶路径说明。"""
    return StepOutput(
        content=(
            "当前进入进阶路径。\n"
            "建议开始围绕一个真实学习助手目标，组织完整工作流并产出可执行计划。"
        ),
        success=True,
    )

# ── 3. Team 构建（带自定义工具） ──────────────────────

def build_learning_team(model_wrapper: OpenAIModel, knowledge: Knowledge) -> Team:
    """构建围绕学习规划协作的知识团队。"""
    concept_agent = model_wrapper.create_agent(
        name="学习概念成员",
        role="负责解释当前阶段最该理解的关键概念。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        instructions=[
            "请先基于共享知识库解释当前阶段最重要的概念重点。",
            "回答时尽量围绕当前阶段最需要理解的内容展开。",
        ],
        markdown=True,
    )

    planning_agent = model_wrapper.create_agent(
        name="学习规划成员",
        role="负责制定下一阶段学习安排。",
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        tools=[estimate_weekly_effort, suggest_output_style],  # 自定义工具
        instructions=[
            "请基于共享知识库制定下一阶段学习安排。",
            "当问题涉及学习投入或产出形式时，请优先调用工具。",
        ],
        markdown=True,
    )

    return Team(
        name="学习助手协作团队",
        mode=TeamMode.coordinate,
        model=model_wrapper.get_model(),
        members=[concept_agent, planning_agent],
        knowledge=knowledge,
        search_knowledge=True,
        add_knowledge_to_context=True,
        add_member_tools_to_context=True,  # 让 Team 看到成员的工具
        instructions=[
            "你是一个围绕共享知识库协作的学习助手团队。",
            "请从概念理解和学习规划两个角度共同完成分析。",
        ],
        markdown=True,
        show_members_responses=True,
        debug_mode=True,
    )

# ── 4. 主函数（Workflow 编排） ────────────────────────

def run_learning_assistant_mini_workflow_example() -> None:
    model_wrapper = OpenAIModel.from_env()
    knowledge = build_mini_workflow_knowledge()

    intake_agent = model_wrapper.create_agent(
        name="需求识别员",
        role="负责识别用户当前进度、目标和问题。",
        instructions=[...],
        markdown=True,
    )
    summary_agent = model_wrapper.create_agent(
        name="最终计划汇总员",
        role="负责把前面各阶段结果整理成一份可执行计划。",
        instructions=[
            "你会收到前面多个阶段的结果。",
            "请整合这些内容，给出一份可执行的下一阶段学习计划。",
            "最终回答要包含：当前阶段判断、学习重点、每周投入建议、下一课安排、建议产出形式。",
        ],
        markdown=True,
    )
    study_team = build_learning_team(model_wrapper, knowledge)

    workflow = Workflow(
        name="Agno 学习助手小型工作流",
        description="一个更接近真实项目的学习助手最小工作流。",
        steps=[
            Step(name="需求识别阶段", agent=intake_agent),
            Condition(
                name="学习路径判断",
                evaluator=needs_advanced_path,
                steps=[Step(name="进阶路径说明", executor=build_advanced_path_note)],
                else_steps=[Step(name="巩固路径说明", executor=build_beginner_path_note)],
            ),
            Step(name="知识协作规划阶段", team=study_team),
            Step(name="最终学习计划", agent=summary_agent),
        ],
        debug_mode=True,
    )

    workflow.print_response(
        input=(
            "我已经学完了 Workflow 的基础课、Steps、Condition、Parallel、Loop、"
            "多模式组合课，以及 Workflow + Team、Workflow + Knowledge、Workflow + Team + Knowledge。"
            "现在我想进入更接近真实项目的小型工作流阶段，请帮我安排下一阶段学习计划。"
        ),
        markdown=True, stream=True, show_step_details=True,
    )
```

### 执行流程

```
输入 → 需求识别（Agent）→ 路径判断（Condition）→ 知识协作规划（Team + Knowledge）→ 最终计划（Agent）→ 输出
                                │                           │
                           ┌────┴────┐                       ├─ 学习概念成员
                           │         │                       └─ 学习规划成员（带工具）
                       进阶路径    巩固路径                         └─ 共享 Knowledge
                      （函数Step）（函数Step）
```

### 新模式总结

| 模式 | 说明 | 本示例应用 |
|------|------|------------|
| `evaluator` | Condition 的判断函数 | `needs_advanced_path()` 判断是否进入进阶路径 |
| `executor` | Step 的函数执行器 | `build_advanced_path_note()` / `build_beginner_path_note()` |
| `tools` | Agent 的自定义工具 | `estimate_weekly_effort()` / `suggest_output_style()` |
| `add_member_tools_to_context` | 让 Team 看到成员工具 | `True`，便于 Team 协调时知道成员能力 |

### 架构层级

```
┌───────────────────────────────────────────────────────┐
│              Workflow（整体编排）                        │
├───────────────────────────────────────────────────────┤
│  Step 1    │  Condition       │  Step 3         │  Step 4  │
│  Agent     │  （路径判断）      │  Team + Know.   │  Agent   │
│  需求识别  │  ┌─ 进阶路径     │  协作规划        │  最终计划│
│            │  └─ 巩固路径     │  ├─ 概念成员     │          │
│            │  （函数 Step）   │  └─ 规划成员     │          │
│            │                  │     └─ 共享 Know. │          │
└───────────────────────────────────────────────────────┘
```

---

## 5.11 应用骨架工作流 ⭐⭐⭐⭐⭐

**对应示例**：`examples/37_study_assistant_workflow_app.py` + `study_assistant_app/workflow_app.py`

### 学习目标

- 掌握把 Workflow 能力接回模块化应用骨架
- 理解 Workflow 如何与已有项目结构集成
- 学会从应用骨架内部构建和运行 Workflow

### 核心概念

**应用骨架工作流**：不再写独立的示例文件，而是把 Workflow 能力接入 `study_assistant_app` 的模块化结构中。`workflow_app.py` 是新增的应用模块，负责构建完整的工作流并对外暴露 `run_study_assistant_workflow_app()` 函数。

### 项目结构变化

```
study_assistant_app/
├── __init__.py            # 新增导出 run_study_assistant_workflow_app
├── app.py                 # Team + Knowledge 应用
├── knowledge.py           # 知识库构建
├── team.py                # Team 构建
├── tools.py               # 自定义工具（estimate_stage_difficulty, suggest_next_lesson）
└── workflow_app.py        # 【新增】Workflow 应用模块
```

### `examples/37_study_assistant_workflow_app.py`

```python
from study_assistant_app import run_study_assistant_workflow_app

def run_study_assistant_workflow_app_example() -> None:
    """运行接回应用骨架后的学习助手工作流示例。"""
    run_study_assistant_workflow_app()

if __name__ == "__main__":
    run_study_assistant_workflow_app_example()
```

### `study_assistant_app/workflow_app.py` 核心代码

```python
from agno.workflow import Condition, Step, Workflow
from models import OpenAIModel
from .knowledge import build_study_knowledge
from .tools import estimate_stage_difficulty, suggest_next_lesson

def build_study_assistant_workflow_app(model_wrapper=None) -> Workflow:
    """构建接入应用骨架的学习助手工作流。"""
    wrapper = model_wrapper or OpenAIModel.from_env()
    knowledge = build_study_knowledge()
    study_team = build_workflow_learning_team(wrapper, knowledge)

    intake_agent = wrapper.create_agent(name="应用需求识别员", ...)
    summary_agent = wrapper.create_agent(name="应用计划汇总员", ...)

    return Workflow(
        name="Agno 学习助手应用骨架工作流",
        steps=[
            Step(name="应用需求识别", agent=intake_agent),
            Condition(
                name="应用路径判断",
                evaluator=_needs_advanced_path,
                steps=[Step(name="进阶路径提示", executor=_build_advanced_note)],
                else_steps=[Step(name="巩固路径提示", executor=_build_beginner_note)],
            ),
            Step(name="应用骨架协作规划", team=study_team),
            Step(name="应用最终建议", agent=summary_agent),
        ],
        debug_mode=True,
    )

def run_study_assistant_workflow_app() -> None:
    """运行接入应用骨架后的学习助手工作流。"""
    workflow = build_study_assistant_workflow_app()
    workflow.print_response(input="...", markdown=True, stream=True, show_step_details=True)
```

### 执行流程

```
输入 → 应用需求识别（Agent）→ 路径判断（Condition）→ 应用骨架协作规划（Team + Knowledge）→ 应用最终建议（Agent）→ 输出
                                   │                           │
                              ┌────┴────┐                       ├─ 应用概念成员
                              │         │                       └─ 应用规划成员（带工具）
                          进阶路径    巩固路径                         └─ 共享 Knowledge
                         （函数Step）（函数Step）
```

### 关键设计

| 设计点 | 说明 |
|--------|------|
| 模块化 | Workflow 逻辑封装在 `workflow_app.py` 中，与 `app.py`（Team 应用）并行 |
| 复用 | 知识库通过 `build_study_knowledge()` 复用，自定义工具通过 `tools.py` 复用 |
| 对外接口 | `__init__.py` 同时导出 `run_study_assistant_app` 和 `run_study_assistant_workflow_app` |
| 轻量入口 | `examples/37_*.py` 只做调用，不包含业务逻辑 |

---

## 5.12 Router 路由编排 ⭐⭐⭐⭐⭐

**对应示例**：`examples/38_workflow_router_orchestration.py`

### 学习目标

- 掌握 `Router` 的使用，按目标把请求分流到不同子流程
- 学会用 `Steps` 封装子流程，并通过 `choices` 注册到 Router
- 理解 "背景识别 → 路由分流 → 子流程执行 → 统一汇总" 的完整编排模式

### 核心概念

**Router 路由编排**：`Router` 是 Workflow 中的分流组件。它通过 `selector` 函数分析用户输入，返回子流程名称，然后把请求分发到对应的 `Steps` 子流程中执行。最终由后续步骤统一汇总结果。

### 代码解析

```python
from agno.workflow import Router, Step, Steps, Workflow

# ── 1. selector 函数（路由判断） ─────────────────────

def select_learning_route(step_input) -> str:
    """根据用户目标选择最合适的子流程。"""
    user_input = (step_input.input or "").lower()
    if "knowledge" in user_input or "rag" in user_input or "检索" in user_input:
        return "knowledge_route"
    if "team" in user_input or "协作" in user_input:
        return "team_route"
    return "workflow_route"

# ── 2. 子流程定义（Steps） ───────────────────────────

workflow_route = Steps(
    name="workflow_route",
    description="偏 Workflow 实现路线的子流程。",
    steps=[
        Step(name="工作流路线分析", agent=workflow_focus_agent),
    ],
)

knowledge_route = Steps(
    name="knowledge_route",
    description="偏 Knowledge / RAG 路线的子流程。",
    steps=[
        Step(name="知识路线分析", agent=knowledge_focus_agent),
    ],
)

team_route = Steps(
    name="team_route",
    description="偏 Team 协作路线的子流程。",
    steps=[
        Step(name="团队路线分析", team=learning_team),
    ],
)

# ── 3. Workflow 组装（Router + choices） ──────────────

workflow = Workflow(
    name="Agno Router 编排进阶课",
    steps=[
        Step(name="路由背景识别", agent=intake_agent),
        Router(
            name="学习路线分流器",
            selector=select_learning_route,
            choices=[workflow_route, knowledge_route, team_route],
        ),
        Step(name="最终路由汇总", agent=summary_agent),
    ],
    debug_mode=True,
)
```

### 执行流程

```
输入 → 路由背景识别（Agent）→ Router 分流器 → 子流程执行（Steps）→ 最终路由汇总（Agent）→ 输出
                                    │
                           ┌────────┼────────┐
                           │        │        │
                       workflow  knowledge  team
                       _route    _route    _route
                       （Agent）（Agent）（Team）
```

### Router 参数说明

| 参数 | 说明 |
|------|------|
| `selector` | 路由判断函数，接收 `step_input`，返回子流程 `name` |
| `choices` | 可选子流程列表，每个元素是一个 `Steps` 实例 |

### Condition vs Router 对比

| 特性 | Condition | Router |
|------|-----------|--------|
| 分支数 | 2 个（if / else） | N 个（多个 choices） |
| 判断方式 | `evaluator` 返回 bool | `selector` 返回 string |
| 子流程 | `steps` / `else_steps` | `choices` 列表 |
| 适用场景 | 二元判断（进阶/巩固） | 多路分流（多种路线） |

---

# 附录

## A. 模型层封装

### OpenAIModel

```python
# models/openai_model.py
class OpenAIModel:
    """封装兼容 OpenAI 的模型，方便在不同的 Agno 示例中复用。"""

    def __init__(self, model_id=None, api_key=None, base_url=None, **model_kwargs):
        self.model_id = model_id or os.getenv("OPENAI_MODEL_ID")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")

    def get_model(self) -> OpenAILike:
        """构建 Agno 的 OpenAILike 模型实例。"""
        return OpenAILike(id=self.model_id, api_key=self.api_key, base_url=self.base_url, **self.model_kwargs)

    def create_agent(self, name="Agno Agent", **kwargs) -> Agent:
        """创建一个使用当前模型的 Agno Agent。"""
        return Agent(name=name, model=self.get_model(), **kwargs)

    @classmethod
    def from_env(cls, **model_kwargs) -> "OpenAIModel":
        """从环境变量创建默认的模型封装实例。"""
        return cls(**model_kwargs)
```

### OpenAICompatibleEmbedder

```python
# models/openai_embedder.py
class OpenAICompatibleEmbedder:
    """封装兼容 OpenAI 的嵌入模型，方便在 Knowledge 示例中复用。"""

    def __init__(self, model_id=None, api_key=None, base_url=None, dimensions=None):
        self.model_id = model_id or os.getenv("OPENAI_EMBEDDING_MODEL_ID")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        self.dimensions = dimensions or self._read_dimensions()

    def get_embedder(self) -> OpenAILikeEmbedder:
        """根据当前配置创建 OpenAI 兼容嵌入器。"""
        return OpenAILikeEmbedder(id=self.model_id, api_key=self.api_key, base_url=self.base_url, dimensions=self.dimensions)

    @classmethod
    def from_env(cls) -> "OpenAICompatibleEmbedder":
        """从环境变量创建默认嵌入器配置。"""
        return cls()
```

---

## B. 依赖列表

来自 `pyproject.toml` 的完整依赖：

| 依赖 | 版本 | 用途 |
|------|------|------|
| `agno` | >=1.0.0 | Agno 框架（当前本地版本 2.5.17） |
| `openai` | >=2.30.0 | OpenAI SDK |
| `pydantic` | >=2.0.0 | 数据验证和结构化输出 |
| `sqlalchemy` | >=2.0.49 | 数据库 ORM |
| `fastapi` | >=0.136.0 | Web 框架 |
| `python-dotenv` | >=1.0.0 | 环境变量管理 |
| `beautifulsoup4` | >=4.12.0 | HTML 解析 |
| `chromadb` | >=0.5.0 | 向量数据库 |
| `ddgs` | >=9.13.1 | DuckDuckGo 搜索 |
| `pypdf` | >=5.0.0 | PDF 读取 |
| `reportlab` | >=4.0.0 | PDF 生成 |

### 依赖安装

```bash
# 使用 uv（推荐）
uv sync

# 使用 pip
pip install -e .

# 按需安装额外功能
uv pip install -U ddgs chromadb beautifulsoup4 pypdf reportlab
```

---

## C. 版本说明

- 当前本地版本为 `agno 2.5.17`
- `Agent.__init__()` 不支持 `show_tool_calls`，使用 `debug_mode=True` 替代
- Knowledge 示例使用基于脚本位置的路径解析

---

## D. 当前学习进度与下一步建议

### 已完成课程

| 阶段 | 课程 | 状态 |
|------|------|------|
| 第一阶段 | 01-09 Agent 基础 | ✅ 已完成 |
| 第二阶段 | 10-18 Knowledge / RAG | ✅ 已完成 |
| 第三阶段 | 16-24 Team / 多智能体 | ✅ 已完成 |
| 第四阶段 | 25-26 集成与项目结构 | ✅ 已完成 |
| 第五阶段 | 27-38 Workflow | ✅ 已完成 |

### 下一步学习建议

完成本手册的所有课程后，建议继续学习：

1. **更长链路的真实项目实践**：基于已有模式，构建更完整的长链路项目工作流
2. **更完整的应用骨架**：将 Router 编排等高级模式接入应用骨架
3. **工程化整理**：回顾所有模式，整理出可复用的工作流模板

### 推荐学习顺序

1. 更长链路的真实项目实践
2. 继续把应用骨架升级成更完整的小项目
3. 回头做更复杂的工程化整理

### 参考文档

- [Agno Workflows Overview](https://docs.agno.com/basics/workflows/overview)
- [Agno Workflow Patterns](https://docs.agno.com/workflows/workflow-patterns/overview)
- [Agno Conditional Workflow](https://docs.agno.com/workflows/workflow-patterns/conditional-workflow)
- [Agno Parallel Workflow](https://docs.agno.com/workflows/workflow-patterns/parallel-workflow)
- [Agno Loop Workflow](https://docs.agno.com/workflows/workflow-patterns/loop-workflow)

---

> **祝你学习愉快！** 🚀
