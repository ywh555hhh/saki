---
name: skill-forge
description: An intelligent engine that generates bespoke Agent Skills based on project context and user persona.
version: 3.3.0
---

# Skill Forge (智能技能工厂)

This skill empowers you (the Agent) to act as a **Senior Skill Architect**.
Your goal is not just to "write a file", but to **Select**, **Adapt**, and **Forge** a specialized tool.

## 🧠 Phase 1: Classification (Categorization)

Analyze the user's request and project to determine the **Skill Category**:

| Category | Description | Template to Use |
| :--- | :--- | :--- |
| **Frameworks** | Writing code (React, Python). | `templates/coding.md` |
| **DevOps** | Infrastructure (Docker, K8s). | `templates/ops.md` |
| **Architecture** | System Design, Diagrams. | `templates/architecture.md` |
| **Testing** | QA, Unit Tests. | `templates/testing.md` |
| **Dependency** | Package Manager (npm). | `templates/dependency.md` |
| **Security** | Audits, Auth, Secrets. | `templates/security.md` |
| **Documentation** | Writing Docs, READMEs. | `templates/writing.md` |
| **Data** | Analysis, SQL, Notebooks. | `templates/data.md` |
| **Product** | User Stories, UX Design. | `templates/product.md` |

## 🧠 Phase 2: Context Fusion

You must merge three inputs:
1.  **Project**: What is the strict stack? (e.g., "Next.js 14" != "React")
2.  **Persona**: Read `profiles/{{user_role}}.md`.
    *   *Learner*: "Explain Why."
    *   *Hacker*: "Just Do It."
3.  **Knowledge**: Recall patterns from `knowledge/`.

## ⚡ Phase 3: The Forge (Generation)

**Instruction**:
1.  Load the appropriate Template.
2.  Fill in the placeholders (`{{stack}}`, `{{role}}`) with your analysis.
3.  **Inject Best Practices**:
    *   *Security*: "Look for OWASP Top 10".
    *   *Writing*: "Use Active Voice".
4.  Write the final result to `.agent/skills/[name]/SKILL.md`.

## 🧪 Example

> **User**: "Check for vulnerabilities."
> **Analysis**: Category = **Security**. Scope = **Auth**.
> **Action**: Use `templates/security.md`.
> **Draft**: "Next.js Security Engineer - Focus on XSS and CSRF prevention."
