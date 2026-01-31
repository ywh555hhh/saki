
import typer
from typing import Optional
from ..core.config_manager import config_manager
from ..ui.console import console

app = typer.Typer(help="Manage skill repositories (Global, Team, Personal sources).")

@app.command("list")
def list_repos():
    """
    List all configured skill repositories.
    """
    repos = config_manager.get_repositories()
    if not repos:
        console.warning("No repositories configured.")
        return

    table = console.create_table("Skill Repositories", ["Name", "URL", "Type"])
    for repo in repos:
        table.add_row(repo["name"], repo["url"], repo["type"])
    
    console.print_table(table)

@app.command("add")
def add_repo(
    name: str = typer.Argument(..., help="Name of the repository"),
    url: str = typer.Argument(..., help="URL of the repository (Git or Local Path)"),
    type: str = typer.Option("git", "--type", "-t", help="Type of repository (git or local)")
):
    """
    Add or update a skill repository.
    """
    try:
        config_manager.add_repository(name, url, type)
        console.success(f"Repository '{name}' added successfully.")
    except Exception as e:
        console.error(f"Failed to add repository: {e}")

@app.command("remove")
def remove_repo(name: str):
    """
    Remove a configured repository.
    """
    try:
        config_manager.remove_repository(name)
        console.success(f"Repository '{name}' removed.")
    except Exception as e:
        console.error(f"Failed to remove repository: {e}")

@app.command("update")
def update_repos():
    """
    Update local cache for all repositories (Coming Soon).
    """
    # TODO: Implement git pull logic for repositories
    console.info("Repository update feature coming soon...")
