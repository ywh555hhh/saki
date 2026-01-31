
from pathlib import Path

# --- Constants ---
ROOT_DIR = Path(__file__).resolve().parent.parent.parent # src/saki/config.py -> src/saki -> src -> root
SKILL_SOURCE_DIR = ROOT_DIR / "skills" / "saki"
SKILL_DEST_NAME = "saki"

TOOLS_MAP = {
    "cursor": {
        "name": "Cursor",
        "local": ".cursor/rules", 
        "global": ".cursor/rules" # Cursor recent update favors rules
    },
    "windsurf": {
        "name": "Windsurf",
        "local": ".windsurf/skills",
        "global": ".codeium/windsurf/skills"
    },
    "claude": {
        "name": "Claude Code",
        "local": ".claude/skills",
        "global": ".claude/skills"
    },
    "antigravity": {
        "name": "Antigravity",
        "local": ".agent/skills",
        "global": ".gemini/antigravity/skills"
    },
    "copilot": {
        "name": "GitHub Copilot",
        "local": ".github/skills",
        "global": ".copilot/skills"
    },
    "vscode": {
        "name": "VS Code (Copilot)",
        "local": ".vscode/skills",
        "global": ".vscode/skills"
    }
}
