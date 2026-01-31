# 🧠 Saki Concept: What is a "Skill"?

> **Core Philosophy**: "Skills are specialized, procedural knowledge modules loaded on demand."

本文档基于主流 Agent (Antigravity, Copilot, Claude) 的标准，定义了 **Skill** 的边界、应用场景以及 Saki 的独特定位。

---

## 1. 什么是 Skill？ (Definition)

在 Agent 生态中，Skill 不是简单的 "Prompt"。
**Skill = Context (Best Practices) + Process (How-to) + Tools (Scripts)**

它是一个**"专家模式"**。当 Agent 需要执行特定任务（如"调试 GitHub Actions"或"编写 SwiftUI"）时，它会加载这个 Skill，瞬间变身为该领域的专家。

### ✅ Skill 的边界 (Boundaries)

| 维度 | 是 Skill (✅) | 不是 Skill (❌) | 理由 |
| :--- | :--- | :--- | :--- |
| **通用性** | 针对特定任务 (Task-Specific) | 针对所有对话 (Global Context) | 全局规则应放在 `Custom Instructions` 中。 |
| **触发方式** | 按需加载 (On-Demand) | 永远激活 (Always On) | Skill 应像"应用"一样被调用，避免污染 Context Window。 |
| **内容深度** | 包含复杂的步骤、脚本、模板 | 仅有一两句提示词 | Saki 的 Skill 包含完整的工程化知识。 |
| **生命周期** | 可安装、卸载、更新 | 硬编码在 Prompt 中 | Skill 是独立的资产。 |

---

## 2. 通用场景 (Use Cases)

根据 Antigravity 和 Copilot 的定义，Skill 最适合以下场景：

1.  **复杂工作流 (Complex Workflows)**:
    *   *例*: "发布 npm 包" (检查版本 -> 运行测试 -> `npm publish` -> 打 git tag)。
    *   *Skill*: 包含每一步的检查清单和命令。

2.  **领域最佳实践 (Domain Expertise)**:
    *   *例*: "编写 Rust Async 代码"。
    *   *Skill*: 包含 Tokio 的使用规范、常见陷阱、错误处理模式。

3.  **工具增强 (Tool Augmentation)**:
    *   *例*: "分析 Log 文件"。
    *   *Skill*: 附带一个 Python 脚本来解析 Log，Agent 只需调用脚本而无需自己读文件。

---

## 3. Saki 的解法 (The Saki Solution)

用户面临的**痛点**：
*   写一个高质量的 `SKILL.md` 很难。
*   需要去查阅文档、寻找最佳实践、调试 Prompt。
*   **Context Explosion**: 每个项目都需要不同的配置。

Saki 的**无痛解法**：
**Saki = Saki CLI + Saki Meta-Skill**

1.  **Saki CLI (`saki.py`)**:
    *   负责**交付**。它是一个极其轻量的"加载器"，负责把 Saki 注入到你的 Agent 中。如果没有它，Agent 无法启动 Saki。

2.  **Saki Meta-Skill (`SKILL.md`)**:
    *   负责**生产**。它是"母体"。
    *   它**不仅是 Skill，更是 Skill Factory**。
    *   它利用 **RAG (Library Index)** 和 **Context Awareness (Scanner)**，瞬间为你生成上述的"专家模式"。

### 结论
*   **Skill** 是 Agent 的**"技能卡片"**。
*   **Saki** 是 Agent 的**"制卡师"**。

我们不生产代码，我们生产让 Agent 写出好代码的**"上下文环境" (Context Environment)**。
