
import typer
import sys
import subprocess
from pathlib import Path
from .ui.console import console
from .utils.i18n import t
from .utils.i18n import t
from .core.install import resolve_path, injector
from .config import SKILL_SOURCE_DIR
from .core.config_manager import config_manager
from .commands import skill, repo

# Create the main Typer app
app = typer.Typer(
    name="saki",
    help="Saki - The Agent Skill Injector",
    add_completion=False,
    no_args_is_help=False  # Handled manually for interactive mode
)

# Register subcommands
app.add_typer(skill.app, name="skill", help="Manage and inject agent skills")
app.add_typer(repo.app, name="repo", help="Manage skill repositories")

# Alias for 'saki inject' (Direct injection)
# We wrap the underlying function to register it directly on the main app
@app.command("inject", help="Alias for skill inject (Direct injection)")
def inject_alias(
    ctx: typer.Context,
    skill_name: str = typer.Argument("saki", help="Name of the skill to inject"),
    target: str = typer.Option("cursor", "--target", "-t", help="Target IDE/Agent"),
    global_scope: bool = typer.Option(True, "--global/--local", help="Inject to global scope or local project"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing skill without prompting")
):
    """
    Alias for `saki skill inject`.
    """
    # Forward to the implementation
    skill.inject_skill(skill_name, target, global_scope, force)

@app.command("init", help="Install Saki Meta-Skill to your Agent (The Ritual)")
def init(
    target: str = typer.Option(".agent/skills", "--target", "-t", help="Target directory (e.g., .cursor/skills)"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing installation")
):
    """
    Installs the Saki Meta-Skill to your project.
    Once installed, open your Agent and type '@Saki bootstrap'.
    """
    source_path = SKILL_SOURCE_DIR
    dest_path = Path(target).resolve()
    
    console.print_header()
    console.info(t('init_header'))
    console.info(t('init_target', dest_path))
    
    # 1. Inject the Meta-Skill
    success = injector.inject(source_path, dest_path, force=force)
    
    if success:
        console.success(t('init_online'))
        console.print(t('init_steps'))
        console.print(t('init_step1'))
        console.print(t('init_step2'))
        console.print(t('init_step3'))
    else:
        raise typer.Exit(code=1)

import questionary
from rich.console import Console

def interactive_mode():
    """
    Main interactive loop for the CLI (TUI Mode).
    """
    console.print_header()
    
    while True:
        # Main Menu
        action = questionary.select(
            "Choose an action:",
            choices=[
                "Inject Skill", 
                "Drift Detection (Diff)", 
                "Manage Repositories", 
                "Quit"
            ],
            use_shortcuts=True # Allows 1, 2, 3 selection, typing also filters
        ).ask()
        
        if not action or action == "Quit":
            console.info("Bye 🌸")
            sys.exit(0)
            
        elif action == "Inject Skill":
            tools = config_manager.get_all_tools()
            tool_keys = list(tools.keys())
            
            # Format choices for Questionary
            # We want to show "Name" but return "key"
            tool_choices = [
                questionary.Choice(title=f"{tools[key]['name']}", value=key) 
                for key in tool_keys
            ]
            
            selected_key = questionary.select(
                "Select Target Tool:",
                choices=tool_choices,
                use_shortcuts=True
            ).ask()
            
            if not selected_key: continue
            
            tool_data = tools[selected_key]
            console.rule(f"📦 {tool_data['name']}")
            
            loc_choice = questionary.select(
                "Select Location:",
                choices=["Global", "Local"],
                default="Global",
                use_shortcuts=True
            ).ask()
            
            if not loc_choice: continue
            
            is_global = (loc_choice == "Global")
            target_path_str = tool_data.get('global') if is_global else tool_data.get('local')
            
            if not target_path_str:
                console.error(f"No path configured for {loc_choice} scope.")
                questionary.press_any_key_to_continue().ask()
                continue

            dest_path = resolve_path(target_path_str, is_global=is_global)
            source_path = SKILL_SOURCE_DIR
            
            if questionary.confirm(f"Inject Saki to {dest_path}?").ask():
                injector.inject(source_path, dest_path, force=True)
                questionary.press_any_key_to_continue().ask()

        elif action == "Drift Detection (Diff)":
            console.info("Feature available via CLI command: `saki diff`")
            questionary.press_any_key_to_continue().ask()

        elif action == "Manage Repositories":
             repo.list_repos()
             questionary.press_any_key_to_continue().ask()

@app.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context):
    """
    Saki CLI Entry Point.
    """
    if ctx.invoked_subcommand is None:
        interactive_mode()

def main():
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n\nBye 🌸")
    except Exception as e:
        console.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
