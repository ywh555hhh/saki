<div align="center">

# 🌸 Saki V1.0
### The Intelligent Skill Forge (Agent-on-Agent)

> **"Don't build a new agent. Upgrade the one you have."**

[中文介绍](README_CN.md)

</div>

---

## 😫 The Pain: "I just want it to work"

**The Scenario**:
1.  **You have tasks**: "I need to deploy this," "I need to refactor that."
2.  **You have a repo**: It has its own history, quirks, and tech stack.
3.  **You have preferences**: You hate manual boilerplate. You hate copying generic skills and rewriting them.

**The Problem**:
Writing a `SKILL.md` manually is tedious. Copying one from the internet requires too much modification to fit your project.

## 🌸 The Cure: Saki
**Delegate the bureaucracy to Saki.**

Saki is a **Meta-Agent** (Saki CLI + Saki Skill).
It sits inside your project, reads your **Tasks**, scans your **Repo**, respects your **Preferences**, and **forges** the perfect Skill for you.
It doesn't guess; it **Scans**, **Retrieves**, and **Synthesizes**.

### 🚀 Key Capabilities (V2.2)

1.  **Context Awareness** 🕵️
    *   Reads `package.json`, `Cargo.toml`, `go.mod`.
    *   Reads your `README.md` to understand the project soul.
    *   *Result*: Sees "Rust + Axum" -> Generates Async Rust skills.

2.  **Intelligent Bootstrap** ⚡
    *   **Command**: `@Saki bootstrap`
    *   **Magic**: Instantly generates 5-10 essential skills tailored to your stack.
    *   *Example*: A Next.js project gets: `next-router`, `tailwind-patterns`, `react-hooks`, `typescript-strict`.

3.  **The Awesome Library** 📚
    *   Built-in indexed corpus of **3,500+** best practices (from the *awesome-agent-skills* project).
    *   Saki retrieves the specific "Gold Standard" for your query (e.g., "FastAPI Testing") and injects it into your agent.

---

## 🏛️ Architecture & Design

Saki operates on a "Cognitive Loop" rather than simple string replacement.

```mermaid
graph TD
    subgraph Input [Phase 1: Awareness]
        P[Project Files] -->|Context Scanner| Context[Stack: Rust/React...]
        U[User Profile] -->|Persona| Role[Role: Hacker/Architect]
    end

    subgraph Memory [Phase 2: Retrieval]
        idx[Library Index] -->|Search Engine| Ref[Reference Wisdom]
        Ref -->|Example| Ex["Use tokio::select!"]
    end

    subgraph Core [Phase 3: The Forge]
        Context & Role & Ref --> Agent[Saki Intelligence]
        Agent -->|Synthesis| Skill[Bespoke SKILL.md]
    end

    User -->|@Saki bootstrap| Core
    Skill -->|Install| IDE[.agent/skills]
```

### Components
1.  **Saki.py**: The delivery vehicle. Injects the Meta-Skill into your IDE.
2.  **Logic Layer (`SKILL.md`)**: The brain. Defines the protocols for "Bootstrap" and "Singleforge".
3.  **Sensors (`scripts/`)**:
    *   `context_scanner.py`: Analyzes the file system.
    *   `search_index.py`: Vector-like retrieval from the knowledge base.

---

## 📦 Usage

### ⚡ Quick Start

1.  **Install**:
    ```bash
    python saki.py
    ```
2.  **Bootstrap**:
    Open your Agent (e.g., Cursor) and type:
    > **@Saki bootstrap**

    *Saki will scan your project and instantly generate 5-10 tailored skills.*

### 📖 Detailed Documentation
For advanced usage, configuration (like `USER_PROFILE.md`), and custom template creation, please read the **[User Guide](docs/USER_GUIDE.md)**.

---

## 🍵 Philosophy
We believe **Context is King**.
A generic "Expert Python Skill" is useless.
A "Python Skill for *this* Django 4.2 Legacy Project using Celery" is priceless.

**Saki makes the latter.**

Enjoy.
