import os
from datetime import datetime
from typing import List, Tuple
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

# Initialize Rich console
console = Console()

# Sample transaction data: (date, category, amount, type)
transactions: List[Tuple[str, str, float, str]] = [
    ("2023-10-01", "Salary", 3000.0, "income"),
    ("2023-10-02", "Food", 50.0, "expense"),
    ("2023-10-03", "Transport", 30.0, "expense"),
    ("2023-10-04", "Rent", 1000.0, "expense"),
]




def show_menu():
    """Show the main menu with nice colors."""
    console.print(Panel.fit("[bold magenta]💰 Personal Finance Tracker[/bold magenta]", style="bold cyan"))
    console.print("\n[bold]What would you like to do?[/bold]")
    console.print("1. 👀 View Transactions", style="bold yellow")
    console.print("2. ➕ Add Transaction", style="bold yellow")
    console.print("3. 📊 View Summary", style="bold yellow")
    console.print("4. 🛒 View Spending by Category", style="bold yellow")
    console.print("5. 👋 Exit", style="bold yellow")


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


def validate_date(date_str):
    """Validate the date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def view_transactions(transaction_list: List[Tuple[str, str, float, str]]):
    """Display all transactions in a Rich table."""
    if not transaction_list:
        console.print(Panel.fit("❌ No transactions found. Add one first!", border_style="bold red"))
        return

    table = Table(title="[bold]Your Transactions[/bold]", show_header=True, header_style="bold blue")
    table.add_column("#", style="cyan", justify="right")
    table.add_column("Date", style="green")
    table.add_column("Category", style="yellow")
    table.add_column("Amount", style="magenta", justify="right")
    table.add_column("Type", style="bold red")

    for idx, (date, category, amount, type_) in enumerate(transaction_list, 1):
        amount_str = f"${amount:.2f}"
        type_str = "[bold green]Income[/bold green]" if type_ == "income" else "[bold red]Expense[/bold red]"
        table.add_row(str(idx), date, category, amount_str, type_str)

    console.print(table)


def add_transaction(transaction_list: List[Tuple[str, str, float, str]]):
    """Add a new transaction."""
    date = ask_user("Enter the date (YYYY-MM-DD)")
    if date is None:
        return
    if not validate_date(date):
        console.print("❌ Invalid date format. Please use YYYY-MM-DD.", style="bold red")
        return

    category = ask_user("Enter the category (e.g., Food, Transport, Salary)")
    if category is None:
        return

    while True:
        amount = ask_user("Enter the amount")
        if amount is None:
            return

        try:
            amount = float(amount)
            if amount > 0:
                break
            console.print("❌ Please enter a positive number!", style="bold red")
        except ValueError:
            console.print("❌ Please enter a valid number!", style="bold red")

    while True:
        type_ = ask_user("Enter the type (income or expense)")
        if type_ is None:
            return

        if type_.lower() in ["income", "expense"]:
            type_ = type_.lower()
            break
        console.print("❌ Please enter 'income' or 'expense'!", style="bold red")

    transaction_list.append((date, category, amount, type_))
    console.print(Panel.fit(f"[bold green]✓ Added transaction: {category} (${amount:.2f})[/bold green]", border_style="bold green"))


def view_summary(transaction_list: List[Tuple[str, str, float, str]]):
    """Display a summary of total income, expenses, and net savings."""
    total_income = sum(amount for _, _, amount, type_ in transaction_list if type_ == "income")
    total_expenses = sum(amount for _, _, amount, type_ in transaction_list if type_ == "expense")
    net_savings = total_income - total_expenses

    console.print(
        Panel.fit(
            f"[bold cyan]Total Income:[/bold cyan] [bold green]${total_income:.2f}[/bold green]\n"
            f"[bold cyan]Total Expenses:[/bold cyan] [bold red]${total_expenses:.2f}[/bold red]\n"
            f"[bold cyan]Net Savings:[/bold cyan] [bold yellow]${net_savings:.2f}[/bold yellow]",
            title="[bold]Financial Summary[/bold]",
            border_style="bold magenta",
        )
    )


def view_spending_by_category(transaction_list: List[Tuple[str, str, float, str]]):
    """Display expenses grouped by category."""
    expenses = [t for t in transaction_list if t[3] == "expense"]
    if not expenses:
        console.print(Panel.fit("❌ No expenses found!", border_style="bold red"))
        return

    # Group expenses by category
    categories = {}
    for _, category, amount, _ in expenses:
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    table = Table(title="[bold]Spending by Category[/bold]", show_header=True, header_style="bold blue")
    table.add_column("Category", style="green")
    table.add_column("Total Amount", style="yellow", justify="right")

    for category, total in categories.items():
        table.add_row(category, f"${total:.2f}")

    console.print(table)


def main():
    """Run the Personal Finance Tracker."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_menu()

        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3", "4", "5"], default="5")

        os.system("cls" if os.name == "nt" else "clear")

        match choice:
            case "1":
                view_transactions(transactions)
            case "2":
                add_transaction(transactions)
            case "3":
                view_summary(transactions)
            case "4":
                view_spending_by_category(transactions)
            case "5":
                console.print(Panel.fit("👋 Thanks for using Personal Finance Tracker. Goodbye!", style="bold green"))
                return
            case _:
                console.print("❌ Please enter a number between 1 and 5!", style="bold red")

        if choice != "5":
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()