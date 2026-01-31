
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.table import Table
from typing import Optional

# Custom theme for Saki
theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "green",
    "header": "bold magenta",
})

class UIConsole:
    def __init__(self):
        self.console = Console(theme=theme)

    def print_header(self):
        """Prints the Saki header."""
        title = r"""
   _____       __    _ 
  / ___/____ _/ /__ (_)
  \__ \/ __ `/ //_// / 
 ___/ / /_/ / ,<  / /  
/____/\__,_/_/|_|/_/   
SKILL FORGE CLI
        """
        self.console.print(Panel(title, style="bold magenta", expand=False))

    def info(self, message: str):
        self.console.print(f"[info]ℹ️ {message}[/info]")

    def success(self, message: str):
        self.console.print(f"[success]✅ {message}[/success]")

    def warning(self, message: str):
        self.console.print(f"[warning]⚠️ {message}[/warning]")

    def error(self, message: str):
        self.console.print(f"[error]❌ {message}[/error]")

    def create_table(self, title: str, columns: list[str]) -> Table:
        table = Table(title=title, show_header=True, header_style="bold magenta")
        for col in columns:
            table.add_column(col)
        return table

    def print_table(self, table: Table):
        self.console.print(table)
    
    def rule(self, title: str = ""):
        self.console.rule(title)
        
    def print(self, *args, **kwargs):
        """Delegates to rich console print."""
        self.console.print(*args, **kwargs)

console = UIConsole()
