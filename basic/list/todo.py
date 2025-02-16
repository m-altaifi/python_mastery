import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel

# Initialize Rich console
console = Console()


def clear_screen():
    """Clear the terminal screen for a cleaner look."""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    """Show the main menu with nice colors."""
    console.print(Panel.fit("[bold magenta]📝 To-Do List Manager[/bold magenta]", style="bold cyan"))
    console.print("\n[bold]What would you like to do?[/bold]")
    console.print("1. 👀 View To-Do List", style="bold yellow")
    console.print("2. ➕ Add a Task", style="bold yellow")
    console.print("3. ✅ Mark a Task as Completed", style="bold yellow")
    console.print("4. ❌ Remove a Task", style="bold yellow")
    console.print("5. 👋 Exit", style="bold yellow")


def should_cancel(user_input):
    """
    Check if the user wants to go back to the main menu.
    Returns True if they want to cancel, False if they want to continue.
    """
    if not user_input:  # They just pressed Enter
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


def view_tasks(todo_list):
    """Display all tasks in a Rich table."""
    if not todo_list:
        console.print(Panel.fit("❌ No tasks found. Add one first!", border_style="bold red"))
        return

    table = Table(title="[bold]Your To-Do List[/bold]", show_header=True, header_style="bold blue")
    table.add_column("#", justify="center", style="cyan", no_wrap=True)
    table.add_column("Task", style="green")
    table.add_column("Status", justify="center", style="bold yellow")

    for index, task in enumerate(todo_list, start=1):
        status = "[bold green]✓ Done[/bold green]" if task["completed"] else "[bold red]✗ Not Done[/bold red]"
        table.add_row(str(index), task["name"], status)

    console.print(table)


def add_task(todo_list):
    """Add a new task."""
    task_name = ask_user("Enter the task name")
    if task_name is None:
        return

    todo_list.append({"name": task_name, "completed": False})
    console.print(Panel.fit(f"[bold green]✓ Task '{task_name}' added to the to-do list![/bold green]", border_style="bold green"))


def mark_task_completed(todo_list):
    """Mark a task as completed."""
    if not todo_list:
        console.print(Panel.fit("❌ No tasks found. Add one first!", border_style="bold red"))
        return

    view_tasks(todo_list)
    while True:
        task_number = ask_user("Enter the task number to mark as completed")
        if task_number is None:
            return

        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(todo_list):
                break
            console.print("❌ Please enter a valid task number!", style="bold red")
        except ValueError:
            console.print("❌ Please enter a number!", style="bold red")

    todo_list[task_number - 1]["completed"] = True
    console.print(Panel.fit(f"[bold green]✓ Task '{todo_list[task_number - 1]['name']}' marked as completed![/bold green]", border_style="bold green"))


def remove_task(todo_list):
    """Remove a task."""
    if not todo_list:
        console.print(Panel.fit("❌ No tasks found. Add one first!", border_style="bold red"))
        return

    view_tasks(todo_list)
    while True:
        task_number = ask_user("Enter the task number to remove")
        if task_number is None:
            return

        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(todo_list):
                break
            console.print("❌ Please enter a valid task number!", style="bold red")
        except ValueError:
            console.print("❌ Please enter a number!", style="bold red")

    removed_task = todo_list.pop(task_number - 1)
    console.print(Panel.fit(f"[bold green]✓ Task '{removed_task['name']}' removed from the to-do list![/bold green]", border_style="bold green"))


def main():
    """Run the To-Do List Manager."""
    todo_list = []

    while True:
        clear_screen()
        show_menu()

        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4", "5"], default="5")

        clear_screen()

        match choice:
            case "1":
                view_tasks(todo_list)
            case "2":
                add_task(todo_list)
            case "3":
                mark_task_completed(todo_list)
            case "4":
                remove_task(todo_list)
            case "5":
                console.print(Panel.fit("👋 Thanks for using To-Do List Manager. Goodbye!", style="bold green"))
                return
            case _:
                console.print("❌ Please enter a number between 1 and 5!", style="bold red")

        if choice != "5":
            Prompt.ask("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
