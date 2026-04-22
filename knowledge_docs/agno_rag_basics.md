# Agno RAG 入门资料

## Agent

Agent 是 Agno 中最核心的运行单元。它负责接收用户输入、调用模型、决定是否使用工具，并输出结果。

## Tools

Tools 让 Agent 能够调用外部能力。最简单的工具可以是普通 Python 函数，更复杂的工具可以封装成 Toolkit。

## Memory

Memory 更关注“记住用户”或者“记住上下文”。

- `learning=True` 可以快速开启基础学习能力
- `LearningMachine` 适合做更细粒度的学习控制
- `session_id` 和 history 更适合当前会话上下文

## Knowledge / RAG

Knowledge 更关注“查资料”，而不是“记住用户”。

在 Agno 中，Knowledge 的常见流程是：

1. 准备文档
2. 把文档切分并写入向量数据库
3. 在 Agent 回答问题时检索相关文档
4. 基于检索到的内容生成答案

## Memory 和 Knowledge 的区别

- Memory：记住用户偏好、长期信息、当前会话上下文
- Knowledge：查询文档、笔记、资料库中的外部知识

## 适合学习的第一步

如果你刚开始学习 Agno 的 RAG，建议先从本地 Markdown 文档开始：

- 数据简单
- 容易观察插入和检索过程
- 不需要先处理复杂数据清洗
