
import os
import yaml
from pathlib import Path
from typing import Dict, Any, List

DEFAULT_CONFIG = {
    "repositories": [
        {
            "name": "official",
            "url": "https://github.com/ywh555hhh/saki-skills",
            "type": "git"
        }
    ],
    "tools": {
        "antigravity": {
            "name": "Antigravity",
            "local": ".agent/skills",
            "global": ".gemini/antigravity/skills"
        },
        "claude": {
            "name": "Claude Code",
            "local": ".claude/skills",
            "global": ".claude/skills"
        },
        "codex": {
            "name": "Codex",
            "local": ".codex/skills",
            "global": ".codex/skills"
        },
        "cursor": {
            "name": "Cursor",
            "local": ".cursor/skills", 
            "global": ".cursor/skills"
        },
        "gemini": {
            "name": "Gemini CLI",
            "local": ".gemini/skills", 
            "global": ".gemini/skills"
        },
        "copilot": {
            "name": "GitHub Copilot",
            "local": ".github/skills",
            "global": ".copilot/skills"
        },
        "opencode": {
            "name": "OpenCode",
            "local": ".opencode/skills", 
            "global": ".config/opencode/skills"
        },
        "windsurf": {
            "name": "Windsurf",
            "local": ".windsurf/skills",
            "global": ".codeium/windsurf/skills"
        },
        "vscode": {
            "name": "VS Code (Copilot)",
            "local": ".vscode/skills",
            "global": ".vscode/skills"
        }
    }
}

class ConfigManager:
    def __init__(self):
        self.config_dir = Path(os.path.expanduser("~/.saki"))
        self.config_file = self.config_dir / "config.yaml"
        self._config: Dict[str, Any] = {}
        self.load()

    def load(self):
        """Load configuration from file or create default if not exists."""
        if not self.config_file.exists():
            self._config = DEFAULT_CONFIG
            self.save()
        else:
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self._config = yaml.safe_load(f) or DEFAULT_CONFIG
                    # Merge with default to ensure new keys exist
                    self._merge_defaults(self._config, DEFAULT_CONFIG)
            except Exception as e:
                # Fallback to default in case of corruption
                # In a real app we might want to backup the corrupted file
                self._config = DEFAULT_CONFIG
                
    def save(self):
        """Save current configuration to file."""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        with open(self.config_file, 'w', encoding='utf-8') as f:
            yaml.dump(self._config, f, allow_unicode=True, default_flow_style=False)

    def _merge_defaults(self, config: Dict, defaults: Dict):
        """Recursive merge of defaults"""
        for key, value in defaults.items():
            if key not in config:
                config[key] = value
            elif isinstance(value, dict) and isinstance(config[key], dict):
                self._merge_defaults(config[key], value)

    def get_repositories(self) -> List[Dict[str, str]]:
        return self._config.get("repositories", [])

    def add_repository(self, name: str, url: str, type: str = "git"):
        repos = self.get_repositories()
        # Check if exists
        for repo in repos:
            if repo["name"] == name:
                repo["url"] = url
                repo["type"] = type
                self.save()
                return
        
        repos.append({
            "name": name,
            "url": url,
            "type": type
        })
        self._config["repositories"] = repos
        self.save()

    def remove_repository(self, name: str):
        repos = self.get_repositories()
        self._config["repositories"] = [r for r in repos if r["name"] != name]
        self.save()

    def get_tool_config(self, tool_name: str) -> Dict[str, str]:
        return self._config.get("tools", {}).get(tool_name, {})

    def get_all_tools(self) -> Dict[str, Any]:
        return self._config.get("tools", {})

# Global instance
config_manager = ConfigManager()
