import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel

# Initialize Rich console for enhanced text output (colors, styles, etc.)
console = Console()


def clear_screen():
    """Clear the terminal screen for a cleaner look."""
    os.system("cls" if os.name == "nt" else "clear")  # Use 'cls' for Windows, 'clear' for Unix-based systems


def show_menu():
    """Display the main menu with styled text and options."""
    console.print(Panel.fit("[bold magenta]📝 To-Do List Manager[/bold magenta]", style="bold cyan"))  # Title panel
    console.print("\n[bold]What would you like to do?[/bold]")  # Menu header
    console.print("1. 👀 View To-Do List", style="bold yellow")  # Option 1
    console.print("2. ➕ Add a Task", style="bold yellow")  # Option 2
    console.print("3. ✅ Mark a Task as Completed", style="bold yellow")  # Option 3
    console.print("4. ❌ Remove a Task", style="bold yellow")  # Option 4
    console.print("5. 👋 Exit", style="bold yellow")  # Option 5


def should_cancel(user_input):
    """
    Check if the user wants to go back to the main menu.
    Returns True if they want to cancel, False if they want to continue.
    """
    if not user_input:  # If the user just pressed Enter
        return True
    return user_input.lower().strip() in ["exit", "back"]  # Check if the input is "exit" or "back"


def ask_user(question, allow_empty=False):
    """
    Ask the user a question and handle the response.
    Returns None if they want to cancel, otherwise returns their answer.
    """
    answer = Prompt.ask(f"[bold yellow]{question}[/bold yellow] (press Enter to go back)").strip()  # Prompt the user

    if should_cancel(answer) and not allow_empty:  # Check if the user wants to cancel
        console.print(Panel.fit("↩️ Going back to main menu!", border_style="bold yellow"))  # Notify cancellation
        return None

    return answer  # Return the user's answer


def view_tasks(todo_list):
    """Display all tasks in a Rich table with their status."""
    if not todo_list:  # Check if the to-do list is empty
        console.print(Panel.fit("❌ No tasks found. Add one first!", border_style="bold red"))  # Notify if no tasks
        return

    # Create a Rich table to display tasks
    table = Table(title="[bold]Your To-Do List[/bold]", show_header=True, header_style="bold blue")
    table.add_column("#", justify="center", style="cyan", no_wrap=True)  # Task number column
    table.add_column("Task", style="green")  # Task name column
    table.add_column("Status", justify="center", style="bold yellow")  # Task status column

    # Populate the table with tasks
    for index, task in enumerate(todo_list, start=1):
        status = "[bold green]✓ Done[/bold green]" if task["completed"] else "[bold red]✗ Not Done[/bold red]"  # Set status
        table.add_row(str(index), task["name"], status)  # Add task row to the table

    console.print(table)  # Display the table


def add_task(todo_list):
    """Add a new task to the to-do list."""
    task_name = ask_user("Enter the task name")  # Ask the user for the task name
    if task_name is None:  # If the user cancels, return to the main menu
        return

    # Add the task to the list
    todo_list.append({"name": task_name, "completed": False})
    console.print(Panel.fit(f"[bold green]✓ Task '{task_name}' added to the to-do list![/bold green]", border_style="bold green"))


def mark_task_completed(todo_list):
    """Mark a task as completed."""
    if not todo_list:  # Check if the to-do list is empty
        console.print(Panel.fit("❌ No tasks found. Add one first!", border_style="bold red"))
        return

    view_tasks(todo_list)  # Display the current tasks
    while True:
        task_number = ask_user("Enter the task number to mark as completed")  # Ask for the task number
        if task_number is None:  # If the user cancels, return to the main menu
            return

        try:
            task_number = int(task_number)  # Convert input to integer
            if 1 <= task_number <= len(todo_list):  # Validate the task number
                break
            console.print("❌ Please enter a valid task number!", style="bold red")  # Notify invalid input
        except ValueError:
            console.print("❌ Please enter a number!", style="bold red")  # Notify invalid input

    # Mark the task as completed
    todo_list[task_number - 1]["completed"] = True
    console.print(Panel.fit(f"[bold green]✓ Task '{todo_list[task_number - 1]['name']}' marked as completed![/bold green]", border_style="bold green"))


def remove_task(todo_list):
    """Remove a task from the to-do list."""
    if not todo_list:  # Check if the to-do list is empty
        console.print(Panel.fit("❌ No tasks found. Add one first!", border_style="bold red"))
        return

    view_tasks(todo_list)  # Display the current tasks
    while True:
        task_number = ask_user("Enter the task number to remove")  # Ask for the task number
        if task_number is None:  # If the user cancels, return to the main menu
            return

        try:
            task_number = int(task_number)  # Convert input to integer
            if 1 <= task_number <= len(todo_list):  # Validate the task number
                break
            console.print("❌ Please enter a valid task number!", style="bold red")  # Notify invalid input
        except ValueError:
            console.print("❌ Please enter a number!", style="bold red")  # Notify invalid input

    # Remove the task from the list
    removed_task = todo_list.pop(task_number - 1)
    console.print(Panel.fit(f"[bold green]✓ Task '{removed_task['name']}' removed from the to-do list![/bold green]", border_style="bold green"))


def main():
    """Run the To-Do List Manager."""
    todo_list = []  # Initialize an empty to-do list

    while True:
        clear_screen()  # Clear the screen for a clean UI
        show_menu()  # Display the main menu

        # Ask the user for their choice
        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4", "5"], default="5")

        clear_screen()  # Clear the screen before showing the next screen

        match choice:  # Handle the user's choice
            case "1":
                view_tasks(todo_list)  # View all tasks
            case "2":
                add_task(todo_list)  # Add a new task
            case "3":
                mark_task_completed(todo_list)  # Mark a task as completed
            case "4":
                remove_task(todo_list)  # Remove a task
            case "5":
                console.print(Panel.fit("👋 Thanks for using To-Do List Manager. Goodbye!", style="bold green"))  # Exit the program
                return
            case _:
                console.print("❌ Please enter a number between 1 and 5!", style="bold red")  # Handle invalid input

        if choice != "5":  # If the user didn't choose to exit, wait for them to continue
            Prompt.ask("\nPress Enter to continue...")


if __name__ == "__main__":
    main()  # Run the program