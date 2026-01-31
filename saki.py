#!/usr/bin/env python3
"""
Saki - The Agent Skill Installer
================================

This script installs 'Saki' into your AI Coding Assistant's skill directory.
It supports Global installation (for all projects) and Local installation (for current project).

Supported Tools:
- Antigravity, Claude Code, Codex, Cursor
- Gemini CLI, GitHub Copilot, OpenCode, Windsurf

Usage:
    python saki.py           # Interactive Mode
    python saki.py --help    # Show help message
"""

import os
import sys
import shutil
import argparse
import locale
import json
from pathlib import Path

# --- Localization & Configuration ---
def get_language():
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and 'zh' in lang.lower():
            return 'zh'
    except:
        pass
    return 'en'

LANG = get_language()

STRINGS = {
    'en': {
        'header': """
    🌸 Saki (v1.0 Alpha)
    ====================
    > "Don't build a new agent. Upgrade the one you have."
        """,
        'source_missing': "[Error] 'skills/saki' directory not found. Please run this from the repo root.",
        'dest_exists': "[Warning] Saki is already installed at: {}",
        'overwrite_prompt': "Overwrite? (y/n): ",
        'install_cancelled': "[Info] Installation cancelled.",
        'remove_fail': "[Error] Failed to clean up old installation: {}",
        'install_success': "\n✨ [Success] Saki Skill installed successfully!\n👉 Now open your AI Agent and type: @Saki verify",
        'install_fail': "[Error] Installation failed: {}",
        'select_tool': "Select your AI Editor / Agent:",
        'select_loc': "Where to install Saki Skill?",
        'loc_global': "Global (Recommended for all projects)",
        'loc_local': "Current Project (This workspace only)",
        'invalid_choice': "Invalid choice.",
        'quit': "Quit"
    },
    'zh': {
        'header': """
    🌸 Saki (v1.0 Alpha)
    ====================
    > "无需重造 Agent，只需升级你手中的那个。"
        """,
        'source_missing': "[错误] 未找到 'skills/saki' 目录。请在仓库根目录运行此脚本。",
        'dest_exists': "[警告] Saki Skill 已存在于: {}",
        'overwrite_prompt': "是否覆盖? (y/n): ",
        'install_cancelled': "[信息] 安装已取消。",
        'remove_fail': "[错误] 清理旧文件失败: {}",
        'install_success': "\n✨ [成功] Saki Skill 已注入成功！\n👉 现在打开你的 AI 编辑器并输入: @Saki verify",
        'install_fail': "[错误] 安装失败: {}",
        'select_tool': "选择你的 AI编辑器 / Agent:",
        'select_loc': "安装 Saki Skill 到哪里?",
        'loc_global': "全局 (推荐，适用于所有项目)",
        'loc_local': "当前项目 (仅当前工作区)",
        'invalid_choice': "无效选项。",
        'quit': "退出"
    }
}

def t(key, *args):
    template = STRINGS[LANG].get(key, STRINGS['en'].get(key, key))
    if args:
        return template.format(*args)
    return template

# --- Constants ---
SKILL_SOURCE_DIR = Path("skills") / "saki"
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

def resolve_path(path_str, is_global=False):
    if is_global:
        return Path(os.path.expanduser(f"~/{path_str}"))
    return Path.cwd() / path_str

def install_skill(dest_path):
    target = dest_path / SKILL_DEST_NAME
    
    print(f"\n⚡ {target}")
    
    if not SKILL_SOURCE_DIR.exists():
        print(t('source_missing'))
        return False

    if target.exists():
        print(t('dest_exists', target))
        choice = input(t('overwrite_prompt')).strip().lower()
        if choice != 'y':
            print(t('install_cancelled'))
            return False
        try:
            shutil.rmtree(target)
        except Exception as e:
            print(t('remove_fail', e))
            return False

    try:
        dest_path.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_SOURCE_DIR, target)
        print(t('install_success'))
        return True
    except Exception as e:
        print(t('install_fail', e))
        return False

def interactive_mode():
    print(t('header'))
    print(t('select_tool'))
    
    keys = list(TOOLS_MAP.keys())
    for i, key in enumerate(keys):
        tool = TOOLS_MAP[key]
        print(f"  {i+1}) {tool['name']}")
    
    print(f"  q) {t('quit')}")

    choice = input("\n> ").strip()
    
    if choice.lower() == 'q':
        sys.exit(0)
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(keys):
            selected_key = keys[idx]
            tool_data = TOOLS_MAP[selected_key]
            
            print(f"\n📦 {tool_data['name']}")
            print(t('select_loc'))
            
            global_path = resolve_path(tool_data['global'], is_global=True)
            local_path = resolve_path(tool_data['local'], is_global=False)
            
            print(f"  1) {t('loc_global')}")
            print(f"  2) {t('loc_local')}")
            
            loc_choice = input("\n> ").strip()
            
            if loc_choice == '1':
                install_skill(global_path)
            elif loc_choice == '2':
                install_skill(local_path)
            else:
                print(t('invalid_choice'))
        else:
            print(t('invalid_choice'))
    except ValueError:
        print(t('invalid_choice'))

if __name__ == "__main__":
    try:
        interactive_mode()
    except KeyboardInterrupt:
        print("\n\nBye 🌸")
