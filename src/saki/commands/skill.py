
import typer
from pathlib import Path
from ..core.config_manager import config_manager
from ..core.install import injector, resolve_path
from ..config import SKILL_SOURCE_DIR
from ..ui.console import console

app = typer.Typer(help="Manage and inject agent skills.")

@app.command("list")
def list_skills():
    """
    List available skills in the local repository.
    """
    # Currently only supports the bundled Saki skill
    table = console.create_table("Available Skills", ["Name", "Source", "Description"])
    table.add_row("saki", "Bundled", "The Intelligent Skill Forge")
    console.print_table(table)

@app.command("inject")
def inject_skill(
    skill_name: str = typer.Argument("saki", help="Name of the skill to inject"),
    target: str = typer.Option("cursor", "--target", "-t", help="Target IDE/Agent (cursor, windsurf, etc.)"),
    global_scope: bool = typer.Option(True, "--global/--local", help="Inject to global scope or local project"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing skill without prompting")
):
    """
    Inject a skill into an Agent's context.
    """
    tool_config = config_manager.get_tool_config(target)
    if not tool_config:
        console.error(f"Unknown target: {target}. Available: {list(config_manager.get_all_tools().keys())}")
        return

    path_key = "global" if global_scope else "local"
    dest_path_str = tool_config.get(path_key)
    
    if not dest_path_str:
        console.error(f"Configuration for {target} {path_key} path is missing.")
        return

    dest_path = resolve_path(dest_path_str, is_global=global_scope)
    
    # Source resolution (currently hardcoded to bundled saki, but extensbile)
    source_path = SKILL_SOURCE_DIR 
    
    if not force:
        # Check existence before proceeding
        full_dest = dest_path / "saki" # assumption
        if full_dest.exists():
            if not typer.confirm(f"Skill already exists at {full_dest}. Overwrite?"):
                console.info("Injection cancelled.")
                return
            force = True

    injector.inject(source_path, dest_path, force=force)

@app.command("diff")
def diff_skill(
    skill_name: str = typer.Argument("saki", help="Name of the skill to check"),
    target_a: str = typer.Argument(..., help="First target (e.g., cursor:global)"),
    target_b: str = typer.Argument("bundled", help="Second target (default: bundled source)")
):
    """
    Compare a deployed skill against the source or another deployment.
    Format: tool:scope (e.g. cursor:global)
    """
    def resolve_target_path(target_str):
        if target_str == "bundled":
            return SKILL_SOURCE_DIR
        
        parts = target_str.split(":")
        if len(parts) != 2:
            console.error(f"Invalid target format '{target_str}'. Use tool:scope (e.g. cursor:global)")
            return None
            
        tool, scope = parts
        tool_config = config_manager.get_tool_config(tool)
        if not tool_config:
            console.error(f"Unknown tool: {tool}")
            return None
            
        is_global = (scope == "global")
        path_str = tool_config.get(scope)
        if not path_str:
            console.error(f"No path for {tool}:{scope}")
            return None
            
        return resolve_path(path_str, is_global=is_global) / skill_name

    path_a = resolve_target_path(target_a)
    path_b = resolve_target_path(target_b)

    if path_a and path_b:
        console.info(f"Comparing {target_a} <-> {target_b}")
        if not injector.diff(path_a, path_b):
            console.success("Skills are identical.")
        else:
            console.warning("Drift detected!")

@app.command("sync")
def sync_skills(
    source: str = typer.Argument(..., help="Source (e.g. cursor:global)"),
    dest: str = typer.Argument(..., help="Destination (e.g. windsurf:global)"),
    force: bool = typer.Option(False, "--force", "-f", help="Force overwrite")
):
    """
    Sync skills between two environments.
    """
    # Reuse diff resolution logic? Ideally refactor, but for now duplicate slightly for speed
    # Or better, just implement basic sync: Copy Source -> Dest
    
    # 1. Resolve Source Path
    # 2. Resolve Dest Path
    # 3. Inject(Source, Dest.parent)
    
    console.info(f"Syncing {source} -> {dest}...")
    # (Implementation simplified for prototype)
    console.warning("Sync logic uses standard injection flow.")
    
    # Mocking self-call via subprocess or direct logic reuse is best.
    # calling inject logic directly:
    
    # THIS IS A PLACEHOLDER FOR FULL SYNC LOGIC
    # Ideally we parse 'source' and 'dest' exactly like diff does, then copy.
    console.info("To implemented: verify paths and copy tree.")
