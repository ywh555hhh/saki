# Skill Templates (技能模板)

[English](#english) | [中文](#chinese)

---

## English

This directory contains the **Pattern Templates** used by the Meta-Engine to generate new skills.
Each file represents a specific domain expertise (e.g., `coding.md` for writing code, `ops.md` for infrastructure).

### How to Customize
You can modify these templates to enforce organization-wide standards.

**Placeholders**:
The engine uses Handlebars-style placeholders:
*   `{{stack}}`: The detected technology (e.g., "React").
*   `{{role}}`: The detected user persona (e.g., "Learner").

**Example**:
If you want ALL comments to be in Chinese, edit `coding.md` to include:
> `## Rules`: All comments must be in Simplified Chinese.

### Adding a New Category
1.  Create `mytemplate.md`.
2.  Update the main `SKILL.md` to route requests to your new template.

---

## Chinese (中文)

此目录包含 Meta-Engine 用来生成新技能的 **核心模板**。
每个文件代表一个特定的领域专长（例如 `coding.md` 用于代码编写，`ops.md` 用于运维）。

### 如何自定义
你可以修改这些模板，以在整个组织或项目中强制执行特定标准。

**占位符 (Placeholders)**:
引擎使用 Handlebars 风格的占位符：
*   `{{stack}}`: 检测到的技术栈（例如 "React"）。
*   `{{role}}`: 检测到的用户角色（例如 "Learner"）。

**示例**:
如果你希望 Agent 生成的所有代码注释都必须是中文，请编辑 `coding.md` 并加入：
> `## Rules`: 所有代码注释必须使用简体中文。

### 添加新分类
1.  创建一个新文件 `mytemplate.md`。
2.  更新主 `SKILL.md` 文件，将相关请求路由到你的新模板。
