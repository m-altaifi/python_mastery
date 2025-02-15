from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()


def display_menu():
    console.print(Panel("[bold cyan]Habit Tracker Menu[/bold cyan]", expand=False))
    console.print("1. Add a Habit")
    console.print("2. Log a Habit Completion")
    console.print("3. View Habit Progress")
    console.print("4. Exit")


def add_habit(habits):
    habit_name = Prompt.ask("[green]Enter the name of the habit[/green]")
    goal = int(Prompt.ask("[green]Enter your goal (times per week)[/green]"))

    habits.append({"name": habit_name, "goal": goal, "completions": []})
    console.print(f"[bold green]Habit '{habit_name}' added with a goal of {goal} times per week![/bold green]")


def log_habit_completion(habits):
    if not habits:
        console.print("[red]No habits found. Add a habit first![/red]")
        return

    table = Table(title="Select a Habit", header_style="bold magenta")
    table.add_column("#", justify="right")
    table.add_column("Habit Name", justify="left")
    for index, habit in enumerate(habits, start=1):
        table.add_row(str(index), habit["name"])
    console.print(table)

    try:
        habit_index = int(Prompt.ask("[blue]Enter the habit number to log completion[/blue]")) - 1
        if 0 <= habit_index < len(habits):
            habits[habit_index]["completions"].append(datetime.now())
            console.print(f"[bold green]Completion logged for '{habits[habit_index]['name']}'![/bold green]")
        else:
            console.print("[red]Invalid habit number![/red]")
    except ValueError:
        console.print("[red]Please enter a valid number![/red]")


def view_habit_progress(habits):
    if not habits:
        console.print("[red]No habits found. Add a habit first![/red]")
        return

    table = Table(title="Habit Progress", show_header=True, header_style="bold cyan")
    table.add_column("Habit Name", justify="left")
    table.add_column("Progress (This Week)", justify="right")

    for habit in habits:
        completions_this_week = sum(1 for date in habit["completions"] if datetime.now() - date < timedelta(days=7))
        table.add_row(habit["name"], f"{completions_this_week}/{habit['goal']}")

    console.print(table)


def main():
    habits = []
    while True:
        display_menu()
        choice = Prompt.ask("[bold yellow]Enter your choice (1-4)[/bold yellow]")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            log_habit_completion(habits)
        elif choice == "3":
            view_habit_progress(habits)
        elif choice == "4":
            console.print("[bold red]\nExiting the Habit Tracker. Goodbye![/bold red]")
            break
        else:
            console.print("[red]Invalid choice! Please enter a number between 1 and 4.[/red]")


if __name__ == "__main__":
    main()
