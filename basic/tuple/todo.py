import os
from typing import List, Tuple
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

# Initialize Rich console
console = Console()


def show_menu():
    """Show the main menu with nice colors."""
    console.print(Panel.fit("[bold magenta]📚 Student Grade Tracker[/bold magenta]", style="bold cyan"))
    console.print("\n[bold]What would you like to do?[/bold]")
    console.print("1. ➕ Add Student", style="bold yellow")
    console.print("2. 👀 View Students", style="bold yellow")
    console.print("3. 📊 Calculate Average Grade", style="bold yellow")
    console.print("4. 👋 Exit", style="bold yellow")


def should_cancel(user_input):
    """
    Check if the user wants to go back to the main menu.
    Returns True if they want to cancel, False if they want to continue.
    """
    if not user_input:  # User just pressed Enter
        return True
    return user_input.lower().strip() in ["exit", "back"]


def ask_user(question, allow_empty=False):
    """
    Ask the user a question and handle the response nicely.
    Returns None if they want to cancel, otherwise returns their answer.
    """
    answer = Prompt.ask(f"[bold yellow]{question}[/bold yellow] (press Enter to go back)").strip()

    if should_cancel(answer) and not allow_empty:
        console.print(Panel.fit("↩️ Going back to main menu!", border_style="bold yellow"))
        return None

    return answer


def add_student(students: List[Tuple[str, float]]):
    """Add a student's name and grade."""
    name = ask_user("Enter student's name")
    if name is None:
        return

    while True:
        grade = ask_user("Enter student's grade")
        if grade is None:
            return

        try:
            grade = float(grade)
            if 0 <= grade <= 100:  # Assuming grades are between 0 and 100
                break
            console.print("❌ Please enter a grade between 0 and 100!", style="bold red")
        except ValueError:
            console.print("❌ Please enter a valid number!", style="bold red")

    students.append((name, grade))
    console.print(Panel.fit(f"[bold green]✓ Added student: {name} with grade {grade}[/bold green]", border_style="bold green"))


def view_students(students: List[Tuple[str, float]]):
    """Display all students and their grades in a Rich table."""
    if not students:
        console.print(Panel.fit("❌ No students found. Add one first!", border_style="bold red"))
        return

    table = Table(title="[bold]Students and Grades[/bold]", show_header=True, header_style="bold blue")
    table.add_column("Index", style="cyan", justify="right")
    table.add_column("Name", style="green")
    table.add_column("Grade", style="yellow")

    for idx, (name, grade) in enumerate(students, 1):
        table.add_row(str(idx), name, str(grade))

    console.print(table)


def calculate_average_grade(students: List[Tuple[str, float]]):
    """Calculate the average grade of all students."""
    if not students:
        console.print(Panel.fit("❌ No students found. Add one first!", border_style="bold red"))
        return

    # Simulate a loading effect with a progress bar
    console.print("[bold]Calculating average grade...[/bold]")
    total_grades = 0

    average = total_grades / len(students)
    console.print(
        Panel.fit(
            f"[bold cyan]Total Students:[/bold cyan] {len(students)}\n" f"[bold cyan]Average Grade:[/bold cyan] [bold green]{average:.2f}[/bold green]",
            title="[bold]Average Grade Results[/bold]",
            border_style="bold magenta",
        )
    )


def main():
    """Run the Student Grade Tracker."""
    students: List[Tuple[str, float]] = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_menu()

        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4"], default="4")

        os.system("cls" if os.name == "nt" else "clear")

        match choice:
            case "1":
                add_student(students)
            case "2":
                view_students(students)
            case "3":
                calculate_average_grade(students)
            case "4":
                console.print(Panel.fit("👋 Thanks for using Student Grade Tracker. Goodbye!", style="bold green"))
                return
            case _:
                console.print("❌ Please enter a number between 1 and 4!", style="bold red")

        if choice != "4":
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
