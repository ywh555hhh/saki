
import sys
from .config import TOOLS_MAP
from .utils.i18n import t
from .core.install import resolve_path, install_skill

def interactive_mode():
    """
    Main interactive loop for the CLI.
    """
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

def main():
    try:
        interactive_mode()
    except KeyboardInterrupt:
        print("\n\nBye 🌸")
