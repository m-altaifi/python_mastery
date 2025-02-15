import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Initialize Rich console
console = Console()

# Sample list-based contacts database
contacts = [["Alice", "123-456-7890"], ["Bob", "987-654-3210"], ["Charlie", "555-555-5555"]]


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
    name = Prompt.ask("Enter the new contact's name").strip()
    phone = Prompt.ask("Enter the phone number").strip()
    contacts.append([name, phone])
    console.print(f"[bold green]Contact added:[/] {name} - {phone}")


def update_contact():
    """Update an existing contact's phone number."""
    name = Prompt.ask("Enter the contact's name to update").strip()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            new_phone = Prompt.ask("Enter the new phone number").strip()
            contact[1] = new_phone
            console.print(f"[bold yellow]Updated:[/] {contact[0]} - {new_phone}")
            return
    console.print("[bold red]Contact not found![/]")


def remove_contact():
    """Remove a contact by name."""
    name = Prompt.ask("Enter the contact's name to remove").strip()
    global contacts
    contacts = [contact for contact in contacts if contact[0].lower() != name.lower()]
    console.print(f"[bold red]Removed contact:[/] {name}")


def main():
    """CLI main menu."""
    while True:
        console.print("\n[bold yellow]List-Based Contact Manager[/]")
        console.print("1. View Contacts")
        console.print("2. Find Contact")
        console.print("3. Add Contact")
        console.print("4. Update Contact")
        console.print("5. Remove Contact")
        console.print("6. Exit")

        choice = Prompt.ask("Choose an option").strip()
        if choice == "1":
            show_contacts()
        elif choice == "2":
            find_contact()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            remove_contact()
        elif choice == "6":
            console.print("[bold blue]Goodbye![/]")
            sys.exit()
        else:
            console.print("[bold red]Invalid choice, please try again.[/]")


if __name__ == "__main__":
    main()
