# To-Do List Application


def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Exit")


def view_tasks(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['name']} - {status}")


def add_task(todo_list):
    task_name = input("\nEnter the task: ")
    todo_list.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added to the to-do list!")


def mark_task_completed(todo_list):
    view_tasks(todo_list)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print(f"Task '{todo_list[task_number - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def remove_task(todo_list):
    view_tasks(todo_list)
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' removed from the to-do list!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_task_completed(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            print("\nExiting the To-Do List Application. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
