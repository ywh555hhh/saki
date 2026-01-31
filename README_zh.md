<div align="center">

# 🌸 Saki | 咲

**AI Agent 的智能技能锻造师 (Intelligent Skill Forge)**

[English](README.md) | [简体中文](README_zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Saki Version](https://img.shields.io/badge/Version-1.1.0-magenta.svg)]()
[![Agent Compatible](https://img.shields.io/badge/Agent-Ready-green.svg)]()

> **"有了 Saki，技能变简单。"**

</div>

---

## 😫 痛点： "我只想安心写代码" ("I just want it to work")

**场景 (The Scenario)**:
1.  **你有任务**: "我要部署这个服务"，"我要重构那个模块"。
2.  **你有代码**: 它有自己的历史包袱、怪癖，和独特的 Tech Stack。
3.  **你有偏好**: 你讨厌写重复的配置，你也讨厌复制粘贴网上的通用 Skill 然后再痛苦地修改。

**问题 (The Problem)**:
手动编写 `SKILL.md` 既繁琐又耗时。而直接复制的 Skill 往往"水土不服"，需要大量因地制宜的 Modify。

## 🌸 解药：Saki (The Cure)

**把繁文缛节交给 Saki (Delegate the bureaucracy to Saki).**

Saki 是一个 **Meta-Agent** (Saki CLI + Saki Skill)。
它潜伏在你的项目中，读取你的 **Task**，扫描你的 **Repo**，尊重你的 **Preferences**，然后为你 **Forge** 出完美的 Skill。

它不靠猜；它 **Scan**，**Retrieve**，然后 **Synthesize**。

**Saki 让你的 AI 瞬间从"实习生"进化为"Senior Engineer"。**

---

## 🚀 极速上手 (30秒)

### 第一步：The Ritual (安装)
将 Saki **Meta-Skill** 注入到你的 Agent 中。

```bash
# Windows / Mac / Linux
python saki.py init
```
*(CLI 已全面支持中文显示，自动适配你的系统语言)*

### 第二步：The Awakening (觉醒)
打开你的 AI 助手，在对话框输入：

> **@Saki bootstrap**

### 第三步：The Magic (见证奇迹)
Saki 会：
1.  🕵️ **Scan** 你的代码库 (精准识别 Rust/Node, Tailwind, Docker 等)。
2.  🧠 **Analyze** 最佳实践 (根据 Context 动态生成)。
3.  ✨ **Result**: 现在，你的 AI 完全理解这个项目该怎么写代码了。

---

## 📂 架构 (Architecture)

```mermaid
graph LR
    CLI[终端: saki init] -->|安装| Agent[Agent: SKILL.md]
    Agent -->|调用| Scanner[扫描脚本]
    Scanner -->|返回 Context JSON| Agent
    Agent -->|锻造 (Forges)| Skills[专属技能 Skills]
    style CLI fill:#f9f,stroke:#333,stroke-width:2px
    style Agent fill:#bbf,stroke:#333,stroke-width:4px
    style Scanner fill:#bfb,stroke:#333,stroke-width:2px
```

*Forged with 🌸 by Antigravity*
