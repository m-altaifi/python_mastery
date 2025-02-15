# Personal Habit Tracker

from datetime import datetime, timedelta

def display_menu():
    print("\n--- Habit Tracker Menu ---")
    print("1. Add a Habit")
    print("2. Log a Habit Completion")
    print("3. View Habit Progress")
    print("4. View Streaks")
    print("5. Exit")

def add_habit(habits):
    habit_name = input("\nEnter the name of the habit: ")
    goal = int(input("Enter your goal (number of times per week): "))

    habit = {
        "name": habit_name,
        "goal": goal,
        "completions": [],
        "streak": 0
    }
    habits.append(habit)
    print(f"Habit '{habit_name}' added with a goal of {goal} times per week!")

def log_habit_completion(habits):
    if not habits:
        print("\nNo habits found. Add a habit first!")
        return

    print("\n--- Your Habits ---")
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['name']}")

    try:
        habit_index = int(input("\nEnter the habit number to log completion: ")) - 1
        if 0 <= habit_index < len(habits):
            habits[habit_index]["completions"].append(datetime.now())
            print(f"Completion logged for '{habits[habit_index]['name']}'!")
        else:
            print("Invalid habit number!")
    except ValueError:
        print("Please enter a valid number!")

def view_habit_progress(habits):
    if not habits:
        print("\nNo habits found. Add a habit first!")
        return

    print("\n--- Habit Progress ---")
    for habit in habits:
        completions_this_week = sum(1 for date in habit["completions"] if datetime.now() - date < timedelta(days=7))
        print(f"{habit['name']}: {completions_this_week}/{habit['goal']} (this week)")

def calculate_streaks(habits):
    if not habits:
        print("\nNo habits found. Add a habit first!")
        return

    print("\n--- Habit Streaks ---")
    for habit in habits:
        completions = sorted(habit["completions"])
        streak = 0
        current_streak = 0

        for i in range(1, len(completions)):
            if (completions[i] - completions[i - 1]).days == 1:
                current_streak += 1
                if current_streak > streak:
                    streak = current_streak
            else:
                current_streak = 0

        habit["streak"] = streak
        print(f"{habit['name']}: {streak} day streak")

def main():
    habits = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            log_habit_completion(habits)
        elif choice == "3":
            view_habit_progress(habits)
        elif choice == "4":
            calculate_streaks(habits)
        elif choice == "5":
            print("\nExiting the Habit Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()