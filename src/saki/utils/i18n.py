import locale
import sys
import os

def get_language():
    """
    Detects system language with better Windows support.
    """
    lang = 'en'
    try:
        # 1. Windows specific detection via ctypes (Most robust)
        if sys.platform == 'win32':
            import ctypes
            windll = ctypes.windll.kernel32
            # GetUserDefaultUILanguage returns a locale ID (e.g., 2052 for zh-CN)
            lang_id = windll.GetUserDefaultUILanguage()
            # 2052 is zh-CN, 3076 is zh-HK, 5124 is zh-MO, 4100 is zh-SG, 1028 is zh-TW
            if lang_id in [2052, 3076, 5124, 4100, 1028]:
                return 'zh'

        # 2. Standard locale module (Fallback)
        loc = locale.getlocale()[0]
        if not loc:
             loc = locale.getdefaultlocale()[0]
             
        if loc and 'zh' in loc.lower():
            return 'zh'
            
    except Exception:
        pass
        
    return 'en'

LANG = get_language()

STRINGS = {
    'en': {
        'header': """
    🌸 Saki (v1.0.2)
    =================
    > "With Saki, Skills are Easy."
        """,
        'source_missing': "[Error] 'skills/saki' directory not found at: {}",
        'dest_exists': "[Warning] Saki is already injected at: {}",
        'overwrite_prompt': "Overwrite? (y/n): ",
        'install_cancelled': "[Info] Injection cancelled.",
        'remove_fail': "[Error] Failed to clean up old injection: {}",
        'install_success': "\n✨ [Success] Saki Skill injected successfully!\n👉 Now open your AI Agent and type: @Saki verify",
        'install_fail': "[Error] Injection failed: {}",
        'select_tool': "Select your AI Editor / Agent:",
        'select_loc': "Where to inject Saki Skill?",
        'loc_global': "Global (Recommended for all projects)",
        'loc_local': "Current Project (This workspace only)",
        'invalid_choice': "Invalid choice.",
        'quit': "Quit",
        'init_header': "🌸 Initializing Saki Protocol...",
        'init_target': "📂 Target: {}",
        'init_online': "\n✨ Saki is Online.",
        'init_steps': "\n[bold green]Next Steps:[/bold green]",
        'init_step1': "1. Open your AI Assistant (Cursor/Windsurf/Claude)",
        'init_step2': "2. Type: [bold cyan]@Saki bootstrap[/bold cyan]",
        'init_step3': "3. Watch the magic happen. 🌸\n"
    },
    'zh': {
        'header': """
    🌸 Saki (v1.0.2)
    =================
    > "有了 Saki，技能变简单。"
        """,
        'source_missing': "[错误] 未找到 'skills/saki' 目录，路径: {}",
        'dest_exists': "[警告] Saki Skill 已存在于: {}",
        'overwrite_prompt': "是否覆盖? (y/n): ",
        'install_cancelled': "[信息] 注入已取消。",
        'remove_fail': "[错误] 清理旧文件失败: {}",
        'install_success': "\n✨ [成功] Saki Skill 已注入成功！\n👉 现在打开你的 AI 编辑器并输入: @Saki verify",
        'install_fail': "[错误] 注入失败: {}",
        'select_tool': "选择你的 AI编辑器 / Agent:",
        'select_loc': "将 Saki Skill 注入到哪里?",
        'loc_global': "全局 (推荐，适用于所有项目)",
        'loc_local': "当前项目 (仅当前工作区)",
        'invalid_choice': "无效选项。",
        'quit': "退出",
        'init_header': "🌸 正在初始化 Saki 协议...",
        'init_target': "📂 目标路径: {}",
        'init_online': "\n✨ Saki 已上线。",
        'init_steps': "\n[bold green]下一步:[/bold green]",
        'init_step1': "1. 打开你的 AI 助手 (Cursor/Windsurf/Claude)",
        'init_step2': "2. 输入: [bold cyan]@Saki bootstrap[/bold cyan]",
        'init_step3': "3. 见证奇迹时刻。 🌸\n"
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
