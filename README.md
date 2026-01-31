# ⚒️ Agent Skill Forge

<div align="center">

![Agent Skill Forge](https://img.shields.io/badge/Status-Beta-blue?style=for-the-badge)
![Agent-Native](https://img.shields.io/badge/Agent--Native-100%25-ff69b4?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **"Don't just use skills. Forge them."**

[**🇨🇳 中文文档 (Chinese)**](./README_CN.md) | [**Contributing**](./CONTRIBUTING.md)

</div>

---

**Agent Skill Forge** is not a script. It is a **Meta-Skill** that teaches your AI (Claude, Cursor, Antigravity) how to build *new* skills for you.

We crawled **600+ high-quality Agent Skills** to distill the "DNA" of a perfect tool. We packaged this intelligence into a `SKILL.md` that acts as a "Skill Architect" inside your IDE.

## 🚀 Key Features

*   **🧠 Deep Intelligence**: It knows the patterns of 600+ production skills.
*   **🎭 Persona-Aware**: Reads your `user_profile.md` to know if you are a **Learner**, **Hacker**, or **Enterprise Architect**.
*   **⚡ Native Integration**: No Python scripts to run. Just chat with your Agent.

## ⚡ Quick Start

### 1. Installation
Copy the `skills/skill-forge` directory into your agent's skill folder:

```bash
# Example for Cursor/Antigravity
cp -r skills/skill-forge .cursor/skills/
```

### 2. Usage (The Magic)
Open your IDE and just ask:

> **User**: "@skill-forge Analyze this project and recommend some skills."

> **User**: "@skill-forge I am building a Next.js app. Create a routing expert skill for me."

### 3. Personalization (Optional)
Want the agent to write code *your* way?
Copy one of our templates from `skills/skill-forge/profiles/` to `.agent/user_profile.md`.

*   `learner.md`: "Explain everything."
*   `hacker.md`: "Speed first. MVP focus."
*   `enterprise.md`: "Strict types and documentation."

## 📂 Project Structure

*   `skills/skill-forge/SKILL.md`: **The Brain**. The Meta-Prompt that powers the engine.
*   `skills/skill-forge/templates/`: **The Specialist Tools**.
    *   `coding.md`: For writing code (React, Go, Python).
    *   `ops.md`: For DevOps safe execution (Docker, K8s).
    *   `architecture.md`: For System Design & ADRs.
    *   `testing.md`: For QA & Coverage.
    *   `dependency.md`: For Package Management.
    *   `security.md`: For Audits & Auth.
    *   `writing.md`: For Tech Docs & Changelogs.
    *   `data.md`: For Analysis & ETL.
    *   `product.md`: For UX & User Stories.
*   `skills/skill-forge/profiles/`: Persona templates.
*   `raw_data/`: The original corpus (local cache).

## 🤝 Contributing

We believe in **Meta-Skills**—tools that build tools.
PRs are welcome! Help us improve the prompt engineering or add new skill sources.

---

<div align="center">
Made with ❤️ by the Open Source Community
</div>
