# Saki User Guide

> **Unlock the full potential of your Intelligent Skill Forge.**

This guide covers everything from installation to advanced "Hacking" of Saki's brain.

---

## 🚀 1. Installation

### Prerequisites
*   Python 3.8+
*   Git

### Steps
1.  Clone the repository:
    ```bash
    git clone https://github.com/YourRepo/saki.git
    ```
2.  Run the installer:
    ```bash
    cd saki
    python saki.py
    ```
3.  **Select Target**:
    *   **Global**: Installs to your home directory (e.g., `~/.gemini/antigravity/skills`). Recommended if you want Saki available in *every* project.
    *   **Local**: Installs to the current project (e.g., `./.agent/skills`).

---

## 💡 2. Core Workflows

### A. The "Bootstrap" (Project Initialization)
*Best for: New projects or when you want to set up an environment quickly.*

1.  Open your IDE (Cursor, Antigravity, Claude).
2.  In the chat, type:
    > **@Saki bootstrap**
3.  **What happens?**
    *   Saki scans your files (`package.json`, `README.md`, etc.).
    *   It identifies your stack (e.g., "React + Vite + Tailwind").
    *   It automatically generates 5-10 essential skills for you, such as:
        *   `react-best-practices`
        *   `tailwind-styling`
        *   `vite-config`
        *   `git-workflow`

### B. The "Singleforge" (Specific Task)
*Best for: Adding a specific capability on demand.*

1.  Type:
    > **@Saki create a skill for [Topic]**
2.  Examples:
    *   `@Saki create a skill for Docker optimization`
    *   `@Saki create a skill for Python testing with Pytest`
3.  **What happens?**
    *   Saki searches its 3,500+ skill library.
    *   It finds the best matching reference.
    *   It customizes that reference to your project and installs it.

---

## ⚙️ 3. Configuration (Personalization)

Saki isn't one-size-fits-all. You can shape its personality.

### The `USER_PROFILE.md`
Located at `skills/saki/USER_PROFILE.md` (inside the installed directory).

**Default Content**:
```markdown
# User Profile
- **Role**: Architect
- **Language**: Chinese (Simplified)
- **Tone**: Professional, concise
```

**How to Customize**:
1.  Open the file.
2.  Change **Language** to `English` if you prefer English output.
3.  Change **Role** to `Hacker` if you want more aggressive, experimental code.
4.  Change **Role** to `Learner` if you want Saki to explain *why* it chose certain patterns.

---

## 🛠️ 4. Advanced: Extending Saki

### Adding Custom Templates
Saki uses templates in `skills/saki/templates/` as the "skeleton" for new skills.
*   **coding.md**: For general programming languages.
*   **ops.md**: For DevOps/Infrastructure.
*   **product.md**: For planning and design docs.

**To add a custom template**:
1.  Create `skills/saki/templates/my-template.md`.
2.  Tell Saki: "@Saki create a skill using my-template for X".

### Contributing to the Library
The `library/` folder contains the "Raw Wisdom".
If you find Saki doesn't know about a specific tool (e.g., "Svelte 5"), you can physically add a folder:
`skills/saki/library/frameworks/svelte-5/SKILL.md`
Then run `python skills/saki/scripts/build_index.py` to update Saki's brain.

---

## ❓ FAQ

**Q: Saki didn't detect my framework.**
A: Ensure you have a standard config file (`package.json`, `go.mod`). If not, mention it in your `README.md` (e.g., "This project uses Svelte"). Saki reads READMEs!

**Q: Can I use Saki in a monorepo?**
A: Yes. Saki scans the current working directory. If you are in a sub-package, it detects that package's stack.

**Q: Where are the skills installed?**
A:
*   Antigravity: `.agent/skills/`
*   Cursor: `.cursor/rules/`
*   Claude: `.claude/skills/`
