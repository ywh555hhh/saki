
import os
import stat
import shutil
from pathlib import Path

def remove_readonly(func, path, _):
    """
    Error handler for shutil.rmtree to fix [WinError 5] Access is denied.
    Clears the readonly bit and retries the removal.
    """
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception as e:
        print(f"⚠️ Failed to remove {path}: {e}")

def safe_rmtree(path: Path):
    """
    Safely removes a directory tree, handling readonly files on Windows.
    """
    if path.exists():
        shutil.rmtree(path, onerror=remove_readonly)

def copy_tree(src: Path, dest: Path):
    """
    Copies directory tree.
    """
    shutil.copytree(src, dest, dirs_exist_ok=True)
