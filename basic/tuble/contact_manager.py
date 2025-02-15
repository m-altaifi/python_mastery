import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Initialize Rich console
console = Console()

# Sample tuple-based contacts database
contacts = (
    ("Alice", "123-456-7890"),
    ("Bob", "987-654-3210"),
    ("Charlie", "555-555-5555"),
    ("David", "111-222-3333"),
    ("Eve", "444-555-6666"),
    ("Frank", "777-888-9999"),
    ("Grace", "000-111-2222"),
    ("Hannah", "333-444-5555"),
    ("Ian", "666-777-8888"),
    ("Jack", "999-000-1111"),
)


def show_contacts():
    """Display all contacts."""
    table = Table(title="Contact List")
    table.add_column("Name", style="cyan", justify="left")
    table.add_column("Phone Number", style="green", justify="left")

    for contact in contacts:
        table.add_row(contact[0], contact[1])

    console.print(table)


def find_contact():
    """Find a contact by name."""
    name = Prompt.ask("Enter the name to search").strip()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            console.print(f"[bold green]Found:[/] {contact[0]} - {contact[1]}")
            return
    console.print("[bold red]Contact not found![/]")


def add_contact():
    """Add a new contact."""
    global contacts
    name = Prompt.ask("Enter the new contact's name").strip()
    phone = Prompt.ask("Enter the phone number").strip()
    contacts = contacts + ((name, phone),)
    console.print(f"[bold green]Contact added:[/] {name} - {phone}")


def main():
    """CLI main menu."""
    while True:
        console.print("\n[bold yellow]Tuple-Based Contact Manager[/]")
        console.print("1. View Contacts")
        console.print("2. Find Contact")
        console.print("3. Add Contact")
        console.print("4. Exit")

        choice = Prompt.ask("Choose an option").strip()
        if choice == "1":
            show_contacts()
        elif choice == "2":
            find_contact()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            console.print("[bold blue]Goodbye![/]")
            sys.exit()
        else:
            console.print("[bold red]Invalid choice, please try again.[/]")


if __name__ == "__main__":
    main()
