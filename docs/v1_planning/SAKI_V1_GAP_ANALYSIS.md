# 🌸 Saki V1.0 Gap Analysis: Vision vs. Reality

> **Status**: Analysis Complete
> **Date**: 2026-01-31
> **Reviewer**: Antigravity

This document analyzes the gap between the **Saki V1.0 Product Design Spec** (The Vision) and the current **Codebase Implementation** (The Reality).

---

## 1. Executive Summary

The vision describes a **"Living" AI Partner** with a strong emphasis on **UX Rituals** (Persona, Magic Moment) and **Intelligence** (Deep Context Awareness).
The current implementation is a **Functional Skeleton**. It has the mechanisms (CLI, Scripts) but lacks the *Soul* (Interactive Rituals) and the *Brain* (Real Scanner Integration).

**Gap Severity**: 🔴 High. The core "Magic Moment" is currently mocked/simulated.

---

## 2. Detailed Component Analysis

### A. The Ritual (CLI Experience)

| Feature | Design Spec (The Dream) | Current Implementation (The Code) | Gap |
| :--- | :--- | :--- | :--- |
| **Entry Point** | `npx saki-forge init` (Zero Install) | `python saki.py` (Manual) | **Missing**. Needs a streamlined entry point. |
| **Onboarding** | "Scan -> Detect -> Persona -> Install" | `interactive_mode` (Menu based: Inject/Diff/Manage) | **Missing**. The "First Run Experience" flow is absent. |
| **Persona** | Select: "Senior Architect" vs "Hacky Prototyper" | Not implemented. | **CRITICAL MISSING**. No logic to handle persona-based skill generation. |
| **Vibe** | "Saki is online. 🌸" (Character) | Standard CLI output. | **Low**. Needs more personality in strings. |

### B. The Brain (Context & Bootstrap)

| Feature | Design Spec (The Dream) | Current Implementation (The Code) | Gap |
| :--- | :--- | :--- | :--- |
| **Context Scanner** | Detects Next.js, Bun, Tailwind, etc. | `scripts/context_scanner.py` exists but is **Mocked** in `bootstrap.py`. | **CRITICAL**. `bootstrap.py` hardcodes `["git"]`. |
| **Logic** | Protocol: "If `bun.lockb` -> Use Bun". | No logic. Just copies static folders. | **High**. Needs logic to dynamically modify templates based on scanner. |
| **Library** | "Central + Symlink" Model (`.saki/`) | Copies files directly to Target. | **Medium**. Symlink model not implemented. |

### C. The Artifacts (Files)

| Feature | Design Spec (The Dream) | Current Implementation (The Code) | Gap |
| :--- | :--- | :--- | :--- |
| **`saki-skill.md`** | Defines 3 Protocols (Boundary, Bootstrap, Singleforge). | Exists (`skills/saki/SKILL.md`) and is mostly aligned. | **Aligned**. Just needs minor updates. |
| **Structure** | `.saki/core`, `.saki/library` | `.agent/skills/saki` | **Minor**. Directory structure needs alignment. |

---

## 3. The Roadmap to V1.0

To bridge this gap, we need to focus on **"The Magic Moment"**.

### Phase 1: Activate the Brain (Backend)
1.  **Wire up the Scanner**: Make `bootstrap.py` *actually* call `context_scanner.py`.
2.  **Implement Logic**: Add template modification logic (e.g., replace `npm` with `bun` dynamically).

### Phase 2: Create the Ritual (Frontend)
1.  **Implement `init` Command**: A dedicated setup flow in the CLI.
2.  **Add Persona Selection**: Store user preference in `saki-profile.json` or similar.
3.  **Polish Output**: Add emojis and character voice.

### Phase 3: Centralize (Architecture) (Optional for V1)
1.  Move to `.saki/` central repo structure.
2.  Implement Symlink logic for cleaner Agent folders.

---

## 4. Conclusion

The design is vastly superior to the current code. We are currently "Faking it" (Mocked scanner). To reach V1.0, we must stop faking and start **Forging**.
