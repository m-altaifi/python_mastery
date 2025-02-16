from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
import time


# Function to count unique words
def count_unique_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()  # Split text into words
            unique_words = set(words)  # Use a set to store unique words
            return len(unique_words)
    except FileNotFoundError:
        return None


# Main function with Rich UI
def main():
    console = Console()

    # Display a welcome message
    console.print(Panel.fit("📖 Unique Word Counter", border_style="blue"))
    console.print("This script counts the number of unique words in a text file.", style="italic")

    # Get file path from user
    file_path = console.input("[bold yellow]Enter the path to your text file:[/bold yellow] ")

    # Simulate loading with a progress bar
    console.print("\n[bold]Processing your file...[/bold]")
    for _ in track(range(100), description="Analyzing..."):
        time.sleep(0.02)  # Simulate some processing time

    # Count unique words
    unique_count = count_unique_words(file_path)

    # Display results
    if unique_count is not None:
        console.print(Panel.fit(Text(f"✅ Found {unique_count} unique words!", justify="center"), border_style="green"))
    else:
        console.print(Panel.fit(Text("❌ File not found! Please check the file path.", justify="center"), border_style="red"))


if __name__ == "__main__":
    main()
