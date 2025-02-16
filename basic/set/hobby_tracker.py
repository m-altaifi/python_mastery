import sys
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

# Initialize Rich console
console = Console()

# Set to store unique hobbies
hobbies = set()


def clear_screen():
    """Clear the terminal screen for a cleaner look."""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    """Show the main menu with nice colors."""
    console.print(Panel.fit("[bold magenta]🌟 Unique Hobby Tracker[/bold magenta]", style="bold cyan"))
    console.print("\n[bold]What would you like to do?[/bold]")
    console.print("1. 👀 View Hobbies", style="bold yellow")
    console.print("2. 🔍 Check if a Hobby Exists", style="bold yellow")
    console.print("3. ➕ Add a Hobby", style="bold yellow")
    console.print("4. 🗑️ Remove a Hobby", style="bold yellow")
    console.print("5. 🧹 Clear All Hobbies", style="bold yellow")
    console.print("6. 👋 Exit", style="bold yellow")


def ask_user(question, allow_empty=False):
    """
    Ask the user a question and handle the response nicely.
    Returns None if they want to cancel, otherwise returns their answer.
    """
    answer = Prompt.ask(f"[bold yellow]{question}[/bold yellow] (press Enter to go back)").strip()

    if not answer and not allow_empty:
        console.print(Panel.fit("↩️ Going back to main menu!", border_style="bold yellow"))
        return None

    return answer


def show_hobbies():
    """Display all hobbies in a Rich table."""
    if not hobbies:
        console.print(Panel.fit("❌ No hobbies found. Add one first!", border_style="bold red"))
        return

    table = Table(title="[bold]Your Hobbies[/bold]", show_header=True, header_style="bold blue")
    table.add_column("Hobby", style="cyan", justify="left")

    for hobby in hobbies:
        table.add_row(hobby)

    console.print(table)


def check_hobby():
    """Check if a hobby exists in the set."""
    hobby = ask_user("Enter the hobby to check")
    if hobby is None:
        return

    if hobby in hobbies:
        console.print(
            Panel.fit(
                f"[bold green]✓ Found:[/bold green] [bold cyan]{hobby}[/bold cyan]",
                title="[bold]Hobby Check[/bold]",
                border_style="bold magenta",
            )
        )
    else:
        console.print(Panel.fit(f"[bold red]✗ Hobby not found![/bold red]", border_style="bold red"))


def add_hobby():
    """Add a new hobby to the set."""
    hobby = ask_user("Enter the new hobby")
    if hobby is None:
        return

    if hobby in hobbies:
        console.print(Panel.fit(f"[bold red]✗ Hobby already exists![/bold red]", border_style="bold red"))
    else:
        hobbies.add(hobby)
        console.print(
            Panel.fit(
                f"[bold green]✓ Hobby added:[/bold green] [bold cyan]{hobby}[/bold cyan]",
                title="[bold]Add Hobby[/bold]",
                border_style="bold green",
            )
        )


def remove_hobby():
    """Remove an existing hobby from the set."""
    hobby = ask_user("Enter the hobby to remove")
    if hobby is None:
        return

    if hobby in hobbies:
        hobbies.remove(hobby)
        console.print(
            Panel.fit(
                f"[bold green]✓ Hobby removed:[/bold green] [bold cyan]{hobby}[/bold cyan]",
                title="[bold]Remove Hobby[/bold]",
                border_style="bold green",
            )
        )
    else:
        console.print(Panel.fit(f"[bold red]✗ Hobby not found![/bold red]", border_style="bold red"))


def clear_hobbies():
    """Clear all hobbies from the set."""
    global hobbies
    if not hobbies:
        console.print(Panel.fit("❌ No hobbies to clear!", border_style="bold red"))
        return

    hobbies.clear()
    console.print(Panel.fit("[bold green]✓ All hobbies cleared![/bold green]", border_style="bold green"))


def main():
    """Run the Unique Hobby Tracker."""
    while True:
        clear_screen()
        show_menu()

        choice = Prompt.ask(
            "[bold cyan]Enter your choice[/bold cyan]",
            choices=["1", "2", "3", "4", "5", "6"],
            default="6",
        )

        clear_screen()

        match choice:
            case "1":
                show_hobbies()
            case "2":
                check_hobby()
            case "3":
                add_hobby()
            case "4":
                remove_hobby()
            case "5":
                clear_hobbies()
            case "6":
                console.print(Panel.fit("👋 Thanks for using Unique Hobby Tracker. Goodbye!", style="bold green"))
                sys.exit()
            case _:
                console.print("❌ Please enter a number between 1 and 6!", style="bold red")

        if choice != "6":
            Prompt.ask("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
