from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()


def display_menu():
    console.print("\n[bold cyan]--- To-Do List Menu ---[/bold cyan]")
    console.print("[green]1.[/] View To-Do List")
    console.print("[green]2.[/] Add a Task")
    console.print("[green]3.[/] Mark a Task as Completed")
    console.print("[green]4.[/] Remove a Task")
    console.print("[green]5.[/] Exit")


def view_tasks(todo_list):
    if not todo_list:
        console.print("\n[bold red]Your to-do list is empty![/bold red]")
    else:
        table = Table(title="Your To-Do List", show_header=True, header_style="bold magenta")
        table.add_column("#", justify="center", style="cyan", no_wrap=True)
        table.add_column("Task", style="yellow")
        table.add_column("Status", justify="center", style="bold green")

        for index, task in enumerate(todo_list, start=1):
            status = "[bold green]✓ Done[/bold green]" if task["completed"] else "[bold red]✗ Not Done[/bold red]"
            table.add_row(str(index), task["name"], status)

        console.print(table)


def add_task(todo_list):
    task_name = Prompt.ask("\n[bold yellow]Enter the task[/bold yellow]")
    todo_list.append({"name": task_name, "completed": False})
    console.print(f"[bold green]Task '{task_name}' added to the to-do list![/bold green]")


def mark_task_completed(todo_list):
    if not todo_list:
        console.print("\n[bold red]No tasks to complete![/bold red]")
        return

    view_tasks(todo_list)
    task_number = IntPrompt.ask("\n[bold yellow]Enter the task number to mark as completed[/bold yellow]", default=1)

    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        console.print(f"[bold green]Task '{todo_list[task_number - 1]['name']}' marked as completed![/bold green]")
    else:
        console.print("[bold red]Invalid task number![/bold red]")


def remove_task(todo_list):
    if not todo_list:
        console.print("\n[bold red]No tasks to remove![/bold red]")
        return

    view_tasks(todo_list)
    task_number = IntPrompt.ask("\n[bold yellow]Enter the task number to remove[/bold yellow]", default=1)

    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        console.print(f"[bold green]Task '{removed_task['name']}' removed from the to-do list![/bold green]")
    else:
        console.print("[bold red]Invalid task number![/bold red]")


def main():
    todo_list = []
    while True:
        display_menu()
        choice = Prompt.ask("\n[bold cyan]Enter your choice (1-5)[/bold cyan]", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_task_completed(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            console.print("\n[bold cyan]Exiting the To-Do List Application. Goodbye![/bold cyan]")
            break


if __name__ == "__main__":
    main()
