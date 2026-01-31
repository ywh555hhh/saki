# Meta Skill Forge (元技能工厂)

<div align="center">

![Meta Skill Forge](https://img.shields.io/badge/Meta%20Skill-Forge-blueviolet?style=for-the-badge)
![Philosophy](https://img.shields.io/badge/Philosophy-Skills%20to%20make%20Skills-white?style=for-the-badge)

> **"Skills to make Skills. (用技能去铸造技能)"**

[**English Document**](./README.md)

</div>

---

## 🧬 这是什么？

**Meta Skill Forge** 是一个递归式的智能引擎。
它是一个用来“创造其他技能”的 AI Agent 技能。

它的诞生源于对 [awesome-agent-skills](https://github.com/jd-soloki/awesome-agent-skills) 仓库中 **644 种优秀模式** 的深度分析。我们提炼了顶级 Skill 的“基因”——结构化的提示词、清晰的触发器、安全的操作边界——并将这份智慧封装成了一个 **Meta-Skill (元技能)**。

## 🧠 设计哲学 (Design Thinking)

大多数用户并不知道如何编写高质量的 Agent 指令。
*   **过去**: 你手写一堆提示词，告诉 AI 要做什么。
*   **Forge**: 你只需要告诉 Meta-Skill 你的角色（"我是个极客"）和你的技术栈（"Next.js"）。它就会为你 **铸造 (Forge)** 一个完美适配当前上下文的专用 `SKILL.md`。

**它连接了“通用 AI”与“垂直领域专家”之间的鸿沟。**

## 🔄 使用流程

### 1. 安装 (Installation)
将核心智能植入你的 Agent 技能目录。Forge 支持多种平台：

| 平台 (Platform) | 路径 (Path) |
| :--- | :--- |
| **Antigravity** | `.agent/skills/` |
| **Cursor** | `.cursor/skills/` |
| **Claude Code** | `.claude/skills/` |
| **Windsurf** | `.windsurf/skills/` |

```bash
# Cursor 示例
cp -r skills/skill-forge .cursor/skills/
```

### 2. 个性化 (The Personalization)
告诉 Forge 你是谁。从 `skills/skill-forge/profiles/` 复制一个画像模板：
*   `learner.md`: 适合学习者，强调原理解释。
*   `hacker.md`: 适合极客，强调速度与 MVP。

### 3. 铸造 (The Fabrication)
在日常开发中，直接与 Agent 对话：

> **User**: "@meta-skill-forge 分析一下这个 Python 后端。我需要一个能安全处理数据库迁移的技能。"

**Forge 的思考过程**:
1.  **分析 (Analysis)**: 扫描项目，发现使用了 `alembic` 和 `sqlalchemy`。
2.  **选择 (Selection)**: 调取 `ops.md` 模板（因为涉及运维安全）。
3.  **注入 (Fusion)**: 注入你的 `learner.md` 画像（因此生成的技能会详细解释每一步）。
4.  **生成 (Generation)**: 产出 `.agent/skills/db-migrator.md`。

从此，你的 Agent 就从“通用助手”进化成了“数据库迁移专家”！

## 📂 项目结构

*   `skills/skill-forge/`: **核心引擎 (The Core)**.
    *   `SKILL.md`: 大脑 (Brain).
    *   `templates/`: 专家模具 (Coding, Ops, Architecture 等).
    *   `profiles/`: 用户画像 (Personas).
*   `library/`: **智慧源泉 (Source of Truth)**. 包含我们学习过的 600+ 个已分类的技能库。

---
*Learned from the community, built for the future.*
