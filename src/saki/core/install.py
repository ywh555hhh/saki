
import shutil
import os
from pathlib import Path
from ..config import SKILL_SOURCE_DIR, SKILL_DEST_NAME
from ..utils.i18n import t
from ..utils.fs import safe_rmtree, copy_tree

def resolve_path(path_str, is_global=False):
    """
    Resolves path string to absolute Path object.
    Handles ~ expansion for global paths.
    """
    if is_global:
        return Path(os.path.expanduser(f"~/{path_str}"))
    return Path.cwd() / path_str

def install_skill(dest_path: Path):
    """
    Installs the Saki skill to the destination directory.
    """
    target = dest_path / SKILL_DEST_NAME
    
    print(f"\n⚡ {target}")
    
    # Validation
    if not SKILL_SOURCE_DIR.exists():
        print(t('source_missing', SKILL_SOURCE_DIR))
        return False

    # Conflict Resolution
    if target.exists():
        print(t('dest_exists', target))
        choice = input(t('overwrite_prompt')).strip().lower()
        if choice != 'y':
            print(t('install_cancelled'))
            return False
        
        # Safe Removal
        try:
            safe_rmtree(target)
        except Exception as e:
            print(t('remove_fail', e))
            return False

    # Installation
    try:
        dest_path.mkdir(parents=True, exist_ok=True)
        copy_tree(SKILL_SOURCE_DIR, target)
        print(t('install_success'))
        return True
    except Exception as e:
        print(t('install_fail', e))
        return False
