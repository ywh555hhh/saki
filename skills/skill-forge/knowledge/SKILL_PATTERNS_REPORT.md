# Intelligent Skill Forge: Pattern Recognition Report

Based on the analysis of 300+ skills from `anthropics`, `vercel`, `cloudflare`, and community contributors, we have distilled the "DNA" of a high-quality Agent Skill.

## 🧬 Anatomy of an Awesome Skill

A high-performing `SKILL.md` typically follows this architectural pattern:

### 1. The Header (Metadata)
Use YAML frontmatter to give the agent quick context without reading the whole file.
```yaml
---
name: skill-name-kebab-case
description: Precise, action-oriented description of WHAT this does and WHEN to use it.
version: 1.0.0
---
```

### 2. The Trigger Definition (Context Awareness)
Explicitly tell the agent *when* to activate this skill.
> **Pattern**: "When to Use This Skill" / "Trigger Conditions"
> **Example**: "Use this skill when the user asks to debug a React Native app" or "Trigger when file path ends in .tf".

### 3. The Toolchain (Capabilities)
List the specific scripts or CLI commands the skill exposes.
> **Pattern**: A table or list of Scripts.
> **Key**: Don't just list commands; explain their *purpose* and *inputs*.

### 4. The Workflow (Procedural Knowledge)
The core "Algorithm" for the agent.
> **Best Practice**: Numbered steps (1. Analysis, 2. Execution, 3. Verification).
> **Insight**: The best skills don't just say "fix it"; they say "Analyze the error log first, then grep for the component..."

## 🏆 Identified Archetypes

We found three distinct types of skills:

| Type | Description | Example |
|------|-------------|---------|
| **The Specialist** | Deep knowledge about a specific framework or tool. | `react-native-best-practices`, `terraform-skill` |
| **The Orchestrator** | Manages a complex workflow involving multiple steps. | `doc-coauthoring`, `release-manager` |
| **The Connector** | Bridges the agent to an external API or CLI. | `mcp-builder`, `fal-audio` |

## 🧠 Meta-Engine Design Implications

To generate high-quality skills dynamically, our **Skill Forge** must:

1.  **Infer Triggers**: Look at the user's file extensions (`.tsx`, `.py`) to auto-populate "When to use".
2.  **Inject Best Practices**: If generating a React skill, inject "Hook Rules"; if Python, inject "Type Hinting".
3.  **Structure Enforcement**: Always enforce the Header -> Trigger -> Workflow structure.

## Next Steps
Use these patterns to construct the `skill_forge.py` logic, ensuring generated skills are indistinguishable from hand-crafted ones.
