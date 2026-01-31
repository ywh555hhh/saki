---
name: {{tool}}-operator
description: Automation skill for {{tool}}, focusing on safe execution and state management.
version: 1.0.0
category: DevOps
---

# {{tool}} Operator

## 🧠 Context
Optimized for **{{role}}** to handle **{{tool}}** operations.

## 🛠️ Triggers
*   User asks to "deploy", "build", "audit".
*   File changes in `{{config_file}}`.

## ⚡ Actions

### 1. Pre-Flight Check
*   [ ] **Dry Run**: Always simulate the command first if possible (e.g., `terraform plan`, `kubectl diff`).
*   [ ] **State Backup**: Confirm current state is saved.

### 2. Execution Strategy
*   **Command**: `{{command_template}}`
*   **Safety Flag**: {{safety_flag}} (e.g., `--auto-approve` or interactive).

### 3. Verification
*   After execution, run: `{{verify_command}}`.
