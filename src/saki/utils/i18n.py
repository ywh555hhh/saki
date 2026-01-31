
import locale

def get_language():
    """
    Detects system language using modern Python 3 methods.
    """
    try:
        # getlocale is the preferred way, though even locale module is tricky across platforms.
        # Fallback to getdefaultlocale but catch warning if needed, 
        # or better: inspect environment variables directly for robustness.
        lang = locale.getlocale()[0]
        if not lang:
             # Fallback
             lang = locale.getdefaultlocale()[0]
             
        if lang and 'zh' in lang.lower():
            return 'zh'
    except:
        pass
    return 'en'

LANG = get_language()

STRINGS = {
    'en': {
        'header': """
    🌸 Saki (v1.0.2)
    =================
    > "Don't build a new agent. Upgrade the one you have."
        """,
        'source_missing': "[Error] 'skills/saki' directory not found at: {}",
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
    🌸 Saki (v1.0.2)
    =================
    > "无需重造 Agent，只需升级你手中的那个。"
        """,
        'source_missing': "[错误] 未找到 'skills/saki' 目录，路径: {}",
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
    """
    Translate string by key.
    """
    template = STRINGS[LANG].get(key, STRINGS['en'].get(key, key))
    if args:
        return template.format(*args)
    return template
