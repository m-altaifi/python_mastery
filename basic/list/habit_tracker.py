import os
from datetime import datetime, timedelta

# Rich is a library that makes pretty terminal output
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

# Create our pretty console - this helps make nice colored output
console = Console()


def clear_screen():
    """Clear the terminal screen for a cleaner look."""
    # 'cls' for Windows, 'clear' for Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    """Show the main menu with nice colors."""
    # Display a pretty title
    console.print(Panel.fit("[bold magenta]👋 Welcome to Your Habit Tracker![/bold magenta]", style="bold cyan"))

    # Show menu options
    console.print("\n[bold]What would you like to do?[/bold]")
    console.print("1. ✨ Create a New Habit", style="bold yellow")
    console.print("2. ✅ Mark a Habit as Complete", style="bold yellow")
    console.print("3. 📊 See Your Progress", style="bold yellow")
    console.print("4. 👋 Exit", style="bold yellow")


def should_cancel(user_input):
    """
    Check if the user wants to go back to the main menu.
    Returns True if they want to cancel, False if they want to continue.
    """
    # User can press Enter, type 'exit', or type 'back' to cancel
    if not user_input:  # They just pressed Enter
        return True
    return user_input.lower().strip() in ["exit", "back"]


def ask_user(question, allow_empty=False):
    """
    Ask the user a question and handle the response nicely.
    Returns None if they want to cancel, otherwise returns their answer.
    """
    # Get user's answer
    answer = Prompt.ask(f"[bold yellow]{question}[/bold yellow] (press Enter to go back)").strip()

    # Check if they want to cancel
    if should_cancel(answer) and not allow_empty:
        console.print(Panel.fit("↩️ Going back to main menu!", border_style="bold yellow"))
        return None

    return answer


def create_habit(habits):
    """Create a new habit and add it to the list."""
    # Ask for the habit name
    habit_name = ask_user("What habit would you like to track?")
    if habit_name is None:
        return

    # Ask for weekly goal
    while True:
        goal = ask_user("How many times per week do you want to do this?")
        if goal is None:
            return

        try:
            goal = int(goal)
            if goal > 0:
                break
            console.print("❌ Please enter a positive number!", style="bold red")
        except ValueError:
            console.print("❌ Please enter a number!", style="bold red")

    # Add the new habit to our list
    habits.append({"name": habit_name, "goal": goal, "completions": []})  # This will store the dates when the habit was completed

    # Show success message
    console.print(Panel.fit(f"[bold green]✨ Great! Added '{habit_name}' with a goal of {goal} times per week![/bold green]", border_style="bold green"))


def mark_complete(habits):
    """Mark a habit as complete for today."""
    if not habits:
        console.print(Panel.fit("❌ No habits found. Create one first!", border_style="bold red"))
        return

    # Show all habits in a pretty table
    table = Table(title="[bold]Your Habits[/bold]", show_header=True, header_style="bold blue")
    table.add_column("Number", style="cyan")
    table.add_column("Habit", style="green")

    # Add each habit to the table
    for num, habit in enumerate(habits, 1):
        table.add_row(str(num), habit["name"])

    console.print(table)

    # Ask which habit they completed
    while True:
        choice = ask_user("Enter the number of the habit you completed:")
        if choice is None:
            return

        try:
            choice = int(choice)
            if 1 <= choice <= len(habits):
                break
            console.print("❌ Please enter a valid habit number!", style="bold red")
        except ValueError:
            console.print("❌ Please enter a number!", style="bold red")

    # Record the completion
    habit = habits[choice - 1]
    habit["completions"].append(datetime.now())

    console.print(Panel.fit(f"[bold green]🎉 Nice work! Marked '{habit['name']}' as complete![/bold green]", border_style="bold green"))


def show_progress(habits):
    """Show how well you're doing with your habits."""
    if not habits:
        console.print(Panel.fit("❌ No habits found. Create one first!", border_style="bold red"))
        return

    # Create a pretty table for progress
    table = Table(title="[bold]📊 Your Progress This Week[/bold]", show_header=True, header_style="bold magenta")
    table.add_column("Habit", style="cyan")
    table.add_column("Progress", justify="center", style="green")

    # For each habit, count completions in the last 7 days
    for habit in habits:
        week_ago = datetime.now() - timedelta(days=7)
        completed = sum(1 for date in habit["completions"] if date > week_ago)
        progress = f"[bold green]{completed}[/bold green]/[bold yellow]{habit['goal']}[/bold yellow]"
        table.add_row(habit["name"], progress)

    console.print(table)


def main():
    """Run our habit tracker."""
    # This will store all our habits
    habits = []

    while True:
        clear_screen()
        show_menu()

        # Get user's choice
        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4"], default="4")

        clear_screen()

        # Handle their choice
        match choice:
            case "1":
                create_habit(habits)
            case "2":
                mark_complete(habits)
            case "3":
                show_progress(habits)
            case "4":
                console.print(Panel.fit("👋 Thanks for using Habit Tracker. See you next time!", style="bold green"))
                return
            case _:
                console.print("❌ Please enter a number between 1 and 4!", style="bold red")

        # Wait for user before showing menu again
        if choice != "4":
            Prompt.ask("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
