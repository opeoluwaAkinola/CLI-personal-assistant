from rich.console import Console
console = Console()

def success(message):
    console.print(f"✅ {message}", style="bold green")

def error(message):
    console.print(f"❌ {message}", style="bold red")

def info(message):
    console.print(f"ℹ️ {message}", style="bold blue")
