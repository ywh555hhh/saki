# Meta Skill Forge

<div align="center">

![Meta Skill Forge](https://img.shields.io/badge/Meta%20Skill-Forge-blueviolet?style=for-the-badge)
![Philosophy](https://img.shields.io/badge/Philosophy-Skills%20to%20make%20Skills-white?style=for-the-badge)

> **"Skills to make Skills."**

[**🇨🇳 中文文档 (Chinese)**](./README_CN.md) | [**Contributing**](./CONTRIBUTING.md)

</div>

---

## 🧬 What is this?

**Meta Skill Forge** is a recursive intelligence engine.
It is an AI Agent Skill designed to... create *other* AI Agent Skills.

It was born from the analysis of **644 Patterns** found in the [awesome-agent-skills](https://github.com/jd-soloki/awesome-agent-skills) repository. We distilled the "DNA" of what makes a skill great—structured prompts, clear triggers, and safe actions—and packaged it into a **Meta-Skill**.

## 🧠 The Philosophy (Design Thinking)

Most users don't know how to prompt their Agent effectively.
*   **Old Way**: You manually write a prompt to tell the agent what to do.
*   **The Forge Way**: You tell the **Meta-Skill** about your role ("I am a Hacker") and your stack ("Next.js"). It then **Forges** a specialized `SKILL.md` that perfectly directs the agent for that specific context.

**It bridges the gap between "Generic AI" and "Specialized Expert".**

## 🔄 Usage Flow

### 1. Installation
Copy the core intelligence into your agent's skill directory. The Forge supports:

| Platform | Path |
| :--- | :--- |
| **Antigravity** | `.agent/skills/` |
| **Cursor** | `.cursor/skills/` |
| **Claude Code** | `.claude/skills/` |
| **Windsurf** | `.windsurf/skills/` |

```bash
# Example for Cursor
cp -r skills/skill-forge .cursor/skills/
```

### 2. The Personalization (One-Time)
Tell the Forge who you are. Copy a template from `skills/skill-forge/profiles/`:
*   `learner.md`: For deep understanding.
*   `hacker.md`: For rapid prototyping.

### 3. The Fabrication (Daily Usage)
Just chat with your Agent:

> **User**: "@meta-skill-forge Inspect this Python backend. I need a skill to handle database migrations safely."

**The Forge**:
1.  **Analyzes** the project (finds `alembic`, `sqlalchemy`).
2.  **Selects** the `ops.md` template (for safety).
3.  **Injects** your `learner.md` persona (explains the migration steps).
4.  **Generates** `.agent/skills/db-migrator.md`.

Now, your Agent has a permanent new capability!

## 📂 Project Structure

*   `skills/skill-forge/`: **The Core**.
    *   `SKILL.md`: The Brain.
    *   `templates/`: The Specialists (Coding, Ops, Architecture, etc.).
    *   `profiles/`: The Personas.
*   `library/`: The **Source of Truth**. containing the categorized corpus of 600+ skills we learned from.

---
*Learned from the community, built for the future.*
