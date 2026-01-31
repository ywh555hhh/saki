# Saki Scenario & Gap Analysis (User-Centric)

> **Based on User Definition**:
> 1. **Power**: Migration, Sync, Management. Knows the inputs/outputs.
> 2. **Casual**: Intelligence, Recommendation. "Magic Moment".
> 3. **Novice**: Guidance. "How do I start?"

---

## 1. The Power User (Deep) 🛠️
*Goal: "Efficiency & Control."*
*   **Needs**: `saki sync`, `saki diff`, `saki publish`. Wants to migrate existing prompts to Saki skills.
*   **Current Reality**:
    *   CLI has basic `inject` and `repo` list.
    *   ❌ No `sync` (Drift detection is manual).
    *   ❌ No `migrate` (Cannot turn a local md file into a sharable skill automatically).
    *   ❌ No `manager` (Hard to update/delete installed skills).
*   **The Gap**: **Management Tooling**. Saki lacks the "CRUD" for skills.

## 2. The Casual User (Shallow) ✨
*Goal: "Intelligence & Results."*
*   **Needs**: `@Saki bootstrap`. "Read my project, give me the best tools."
*   **Current Reality**:
    *   Scanner is disconnected.
    *   `bootstrap.py` is dummy code.
    *   ❌ Agent cannot "Analyze" -> "Recommend". It just "Copies".
*   **The Gap**: **Brain-Body Disconnect**. The sensors (scanner) aren't talking to the ACTUATOR (Agent).

## 3. The Novice (Newbie) 🌱
*Goal: "Guidance & Safety."*
*   **Needs**: Hand-holding. "What is a Skill? Why do I need Saki?"
*   **Current Reality**:
    *   CLI is silent. `python saki.py` shows help text.
    *   ❌ No interactive `init` to explain concepts.
    *   ❌ No "Welcome" message in the generated Skill to guide them.
*   **The Gap**: **Onboarding Friction**. The "First 5 Minutes" are confusing.

---

## Strategic Pivot

We cannot fix everything at once. We must prioritize based on the "Saki V1.0" vision.

1.  **Fix Casual User First (The Core Value)**:
    *   If Saki isn't smart (Casual User), Power Users won't respect it.
    *   **Action**: Connect Scanner to `SKILL.md`. Enable `@Saki bootstrap`.

2.  **Fix Novice User Second (The Growth)**:
    *   Simple interactive CLI `saki init`.

3.  **Fix Power User Third (The Retention)**:
    *   Add `sync` and `diff` features later. (V1.1)

**Conclusion**: The immediate priority remains **The Agentic Brain** (serving Casual/Novice), while ensuring the **CLI** (serving Power) behaves as a solid foundation.
