
import shutil
import os
from pathlib import Path
from typing import Optional, List
from ..config import SKILL_SOURCE_DIR, SKILL_DEST_NAME
from ..utils.i18n import t
from ..utils.fs import safe_rmtree, copy_tree
from ..ui.console import console
import filecmp

def resolve_path(path_str, is_global=False):
    """
    Resolves path string to absolute Path object.
    Handles ~ expansion for global paths.
    """
    if is_global:
        return Path(os.path.expanduser(f"~/{path_str}"))
    return Path.cwd() / path_str

class SkillInjector:
    def __init__(self):
        pass

    def inject(self, source_path: Path, dest_parent: Path, force: bool = False) -> bool:
        """
        Injects a skill from source to destination.
        """
        target = dest_parent / SKILL_DEST_NAME
        
        console.info(f"Injecting to: {target}")
        
        # Validation
        if not source_path.exists():
            console.error(f"Source skill not found at: {source_path}")
            return False

        # Conflict Resolution
        if target.exists():
            if not force:
                console.warning(f"Destination exists: {target}")
                # We should technically use Typer's confirm here if interactive, 
                # but for core logic we might want to pass 'force' arg.
                # If called from CLI, force should be handled there.
                console.error("Destination exists. Use --force to overwrite.")
                return False
            
            # Safe Removal
            try:
                safe_rmtree(target)
            except Exception as e:
                console.error(f"Failed to remove existing skill: {e}")
                return False

        # Installation
        try:
            dest_parent.mkdir(parents=True, exist_ok=True)
            copy_tree(source_path, target)
            console.success("Skill injected successfully!")
            return True
        except Exception as e:
            console.error(f"Injection failed: {e}")
            return False

    def diff(self, path_a: Path, path_b: Path) -> bool:
        """
        Compare two directories. Returns True if different.
        Simple file comparison for now.
        """
        if not path_a.exists() or not path_b.exists():
            console.error(f"One of the paths does not exist: {path_a} vs {path_b}")
            return True # Treat as different

        dcmp = filecmp.dircmp(path_a, path_b)
        
        has_diff = False
        if dcmp.diff_files or dcmp.left_only or dcmp.right_only:
            has_diff = True
            console.rule("Drift Detection")
            if dcmp.diff_files:
                console.warning(f"Modified files: {dcmp.diff_files}")
            if dcmp.left_only:
                console.info(f"Only in {path_a.name}: {dcmp.left_only}")
            if dcmp.right_only:
                console.info(f"Only in {path_b.name}: {dcmp.right_only}")
                
        return has_diff

injector = SkillInjector()

# Legacy Wrapper for compatibility
def install_skill(dest_path: Path):
    return injector.inject(SKILL_SOURCE_DIR, dest_path, force=True) # Legacy always forces/prompts in wrapper
