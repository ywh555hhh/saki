---
name: {{stack}}-expert
description: Specialized coding assistant for {{stack}} projects, focusing on syntax, patterns, and architectural rules.
version: 1.0.0
category: Frameworks
---

# {{stack}} Expert

## 🧠 Context
This skill is designed for a **{{role}}** persona working on a **{{stack}}** project.

## 🛠️ Triggers
*   Editing `{{file_extension}}` files.
*   User asks for "refactor", "debug", or "explain" related to {{stack}}.

## ⚡ Actions

### 1. Code Analysis (Pre-Computation)
Before writing code, ALWAYS:
*   [ ] Check for project-specific linting rules (ESLint, Flake8).
*   [ ] Verify version compatibility (Next.js 13 vs 14, Python 3.x).
*   [ ] Search for existing patterns to maintain consistency.

### 2. Implementation Rules
*   **Style**: {{style_preference}} (e.g., Functional vs OOP).
*   **Safety**: {{safety_level}} (Strict Types vs Loose).
*   **Comments**: {{comment_density}} (Verbose vs Minimal).

## 📚 Stack-Specific Knowledge
*   (Agent should fill this with best practices found in `library/frameworks/{{stack}}`)
