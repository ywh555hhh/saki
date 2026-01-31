# System Architecture: The Intelligent Skill Forge

## 🧠 The "Meta-Forge" Workflow

This diagram explains how the **User Profile** and **Project Context** fuse together inside the **Meta-Skill** to generate a bespoke tool.

```mermaid
flowchart TD
    subgraph Inputs [Context Inputs]
        P[Project Codebase] -->|Scanner| Context[Context: Tech Stack & README]
        U[User Profile .md] -->|Persona| Role[Role: Learner/Hacker/Architect]
        L[Library Index] -->|Search| Patterns[Selected Pattern]
        T[Templates] -->|Fallback| Base[Base Structure]
    end

    subgraph Core [The Skill Forge 2.1]
        Context & Role & Patterns & Base --> Engine[Agent Synthesis Engine]
        Engine -->|Decision| Strategy{Strategy Selection}
        
        Strategy -->|Deep Mode| Deep[Synthesize Philosophy & Rules]
        Strategy -->|Express Mode| Fast[Apply Best Practices]
    end

    subgraph Output [The Forged Skill]
        Deep & Fast --> Result(New SKILL.md)
        
        Result -->|Contains| Triggers[Triggers: When to run]
        Result -->|Contains| Actions[Actions: Wraps Project Scripts]
        Result -->|Contains| Tone[Tone: Matches User Persona]
    end

    User((User)) -->|Commands: @skill-forge| Core
    Result -->|Installs into| Agent[.agent/skills/]
    Agent -->|Serves| User
```

## 📂 The "Library" (Awesome Skills Corpus)

We don't just generate from thin air. We hold a reference library of 600+ skills categorized structure:

```text
/library
  ├── mcp/               # Model Context Protocol skills
  ├── frameworks/        # React, Next.js, Django
  ├── devops/            # Docker, Kubernetes, Terraform
  ├── languages/         # Python, Go, Rust, TypeScript
  └── tools/             # Git, Linear, Jira
```
