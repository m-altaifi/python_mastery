import sys
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

# Initialize Rich console
console = Console()

# Sample list-based contacts database
contacts = [["Alice", "123-456-7890"], ["Bob", "987-654-3210"], ["Charlie", "555-555-5555"]]


def show_menu():
    """Show the main menu with nice colors."""
    console.print(Panel.fit("[bold magenta]📇 Contact Manager[/bold magenta]", style="bold cyan"))
    console.print("\n[bold]What would you like to do?[/bold]")
    console.print("1. 👀 View Contacts", style="bold yellow")
    console.print("2. 🔍 Find Contact", style="bold yellow")
    console.print("3. ➕ Add Contact", style="bold yellow")
    console.print("4. ✏️ Update Contact", style="bold yellow")
    console.print("5. ❌ Remove Contact", style="bold yellow")
    console.print("6. 👋 Exit", style="bold yellow")


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
        return None

    return answer


def show_contacts():
    """Display all contacts in a Rich table."""
    if not contacts:
        console.print(Panel.fit("❌ No contacts found. Add one first!", border_style="bold red"))
        return

    table = Table(title="[bold]Contact List[/bold]", show_header=True, header_style="bold blue")
    table.add_column("Name", style="cyan", justify="left")
    table.add_column("Phone Number", style="green", justify="left")

    for contact in contacts:
        table.add_row(contact[0], contact[1])

    console.print(table)


def find_contact():
    """Find a contact by name."""
    name = ask_user("Enter the name to search")
    if name is None:
        return

    for contact in contacts:
        if contact[0].lower() == name.lower():
            console.print(Panel.fit(f"[bold green]✓ Found:[/] {contact[0]} - {contact[1]}", title="[bold]Search Result[/bold]", border_style="bold green"))
            return
    console.print(Panel.fit("[bold red]✗ Contact not found![/bold red]", title="[bold]Search Result[/bold]", border_style="bold red"))


def add_contact():
    """Add a new contact."""
    name = ask_user("Enter the new contact's name")
    if name is None:
        return

    phone = ask_user("Enter the phone number")
    if phone is None:
        return

    contacts.append([name, phone])
    console.print(Panel.fit(f"[bold green]✓ Contact added:[/] {name} - {phone}", title="[bold]Add Contact[/bold]", border_style="bold green"))


def update_contact():
    """Update an existing contact's phone number."""
    name = ask_user("Enter the contact's name to update")
    if name is None:
        return

    for contact in contacts:
        if contact[0].lower() == name.lower():
            new_phone = ask_user("Enter the new phone number")
            if new_phone is None:
                return

            contact[1] = new_phone
            console.print(Panel.fit(f"[bold yellow]✓ Updated:[/] {contact[0]} - {new_phone}", title="[bold]Update Contact[/bold]", border_style="bold yellow"))
            return
    console.print(Panel.fit("[bold red]✗ Contact not found![/bold red]", title="[bold]Update Contact[/bold]", border_style="bold red"))


def remove_contact():
    """Remove a contact by name."""
    name = ask_user("Enter the contact's name to remove")
    if name is None:
        return

    global contacts
    initial_count = len(contacts)
    contacts = [contact for contact in contacts if contact[0].lower() != name.lower()]

    if len(contacts) < initial_count:
        console.print(Panel.fit(f"[bold red]✓ Removed contact:[/] {name}", title="[bold]Remove Contact[/bold]", border_style="bold red"))
    else:
        console.print(Panel.fit("[bold red]✗ Contact not found![/bold red]", title="[bold]Remove Contact[/bold]", border_style="bold red"))


def main():
    """Run the contact manager."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_menu()

        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4", "5", "6"], default="6")

        os.system("cls" if os.name == "nt" else "clear")

        match choice:
            case "1":
                show_contacts()
            case "2":
                find_contact()
            case "3":
                add_contact()
            case "4":
                update_contact()
            case "5":
                remove_contact()
            case "6":
                console.print(Panel.fit("👋 Thanks for using Contact Manager. Goodbye!", style="bold green"))
                sys.exit()
            case _:
                console.print(Panel.fit("❌ Invalid choice, please try again.", border_style="bold red"))

        if choice in ["1"]:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
