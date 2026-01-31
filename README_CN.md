# ⚒️ Agent Skill Forge (智能技能工厂)

<div align="center">

![Agent Skill Forge](https://img.shields.io/badge/Status-Beta-blue?style=for-the-badge)
![Agent-Native](https://img.shields.io/badge/Agent--Native-100%25-ff69b4?style=for-the-badge)

> **"不要只是使用 Skill，去铸造它们。"**

[**English Document**](./README.md)

</div>

---

**Agent Skill Forge** 不是一个 Python 脚本，而是一个 **Meta-Skill (元技能)**。
它教会你的 AI (Claude, Cursor, Antigravity) 如何为你“铸造”出全新的、完美的工具。

我们深度分析了 **600+ 个顶级 Agent Skills**，提炼出优秀工具的“DNA”，并将其封装进一个 `SKILL.md`。从此，你的 IDE 里面就住着一位“技能架构师”。

## 🚀 核心亮点

*   **🧠 原生智能**: 内置 600+ 生产级 Skill 的设计模式。
*   **🎭 千人千面**: 能够读取 `user_profile.md`，识别你是 **Learner (学习者)**、**Hacker (极客)** 还是 **Architect (架构师)**。
*   **⚡ 无缝集成**: 无需运行外部脚本，直接在聊天窗口与 Agent 交互。

## ⚡ 快速开始

### 1. 安装 (Installation)
将 `skills/skill-forge` 文件夹复制到你的 Agent 技能目录：

```bash
# Cursor / Antigravity 示例
cp -r skills/skill-forge .cursor/skills/
```

### 2. 使用 (Usage)
在 IDE 中直接呼唤它：

> **User**: "@skill-forge 帮我分析这个项目，推荐我应该配置什么 Skill。"

> **User**: "@skill-forge 我正在写一个 Next.js 后台，帮我生成一个处理 API 路由的 Skill。"

### 3. 个性化 (Personalization)
希望 Agent 懂你的代码风格？
从 `skills/skill-forge/profiles/` 复制一个模板到 `.agent/user_profile.md`。

*   `learner.md`: "我是来学习的，请详细解释每一行代码。"
*   `hacker.md`: "别废话，我要速度。MVP 优先。"
*   `enterprise.md`: "严格模式。必须有类型检查和文档注释。"

## 📂 项目结构

*   `skills/skill-forge/SKILL.md`: **大脑 (The Brain)**. 驱动引擎的元提示词。
*   `skills/skill-forge/templates/`: **专家工具箱**.
    *   `coding.md`: 代码专家 (Coding).
    *   `ops.md`: 运维专家 (DevOps).
    *   `architecture.md`: 架构师 (System Design).
    *   `testing.md`: 测试专家 (QA).
    *   `dependency.md`: 依赖管理 (Packages).
    *   `security.md`: 安全专家 (Security).
    *   `writing.md`: 技术写作 (Documentation).
    *   `data.md`: 数据科学家 (Analysis).
    *   `product.md`: 产品经理 (Product/UX).
*   `skills/skill-forge/profiles/`: 用户画像模板。
*   `raw_data/`: 原始数据集（本地缓存）。

## 🤝 参与贡献

我们相信 **Meta-Skills**（构建工具的工具）是未来的方向。
欢迎提交 PR！帮助我们优化 Prompt Engineering，或添加更多优质的 Skill 源。

---

<div align="center">
Made with ❤️ by the Open Source Community
</div>
