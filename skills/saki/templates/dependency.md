---
name: {{manager}}-guardian
description: Dependency manager using {{manager}}, focusing on security and version health.
version: 1.0.0
category: Dependency
---

# {{manager}} Guardian

## 🧠 Context
Manages packages using **{{manager}}** (npm, pip, go mod).

## 🛠️ Triggers
*   User asks to "install", "update", "audit" packages.
*   Changes to `package.json`, `requirements.txt`.

## ⚡ Actions

### 1. Installation Protocol
*   [ ] **Security Audit**: Run `{{audit_command}}` before installing.
*   [ ] **Version Lock**: Ensure lockfiles are committed.
*   [ ] **Bloat Check**: Is this package necessary?

### 2. Maintenance
*   Clean unused dependencies.
*   Check for major version updates.

## 📚 Knowledge
*   (Inject package ecosystem specifics here)
