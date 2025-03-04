def main():
    my_set = set()

    while True:
        print("\nSet Operations Menu:")
        print("1. Display set")
        print("2. Add element")
        print("3. Remove element")
        print("4. Check if element exists")
        print("5. Union with another set")
        print("6. Intersection with another set")
        print("7. Difference with another set")
        print("8. Get length")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            print("\nCurrent set:", my_set)

        elif choice == "2":
            try:
                num = int(input("Enter number to add: "))
                my_set.add(num)
                print(f"Added {num}. Updated set: {my_set}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == "3":
            if not my_set:
                print("Set is empty.")
            else:
                try:
                    num = int(input("Enter number to remove: "))
                    my_set.remove(num)
                    print(f"Removed {num}. Updated set: {my_set}")
                except KeyError:
                    print("Number not found in set.")

        elif choice == "4":
            if not my_set:
                print("Set is empty.")
            else:
                try:
                    num = int(input("Enter number to check: "))
                    if num in my_set:
                        print(f"{num} exists in the set.")
                    else:
                        print(f"{num} does not exist in the set.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == "5":
            try:
                new_set = set(map(int, input("Enter numbers for new set (separated by spaces): ").split()))
                union_set = my_set.union(new_set)
                print(f"Union of {my_set} and {new_set}: {union_set}")
            except ValueError:
                print("Invalid input. Please enter valid integers.")

        elif choice == "6":
            try:
                new_set = set(map(int, input("Enter numbers for new set (separated by spaces): ").split()))
                intersection_set = my_set.intersection(new_set)
                print(f"Intersection of {my_set} and {new_set}: {intersection_set}")
            except ValueError:
                print("Invalid input. Please enter valid integers.")

        elif choice == "7":
            try:
                new_set = set(map(int, input("Enter numbers for new set (separated by spaces): ").split()))
                difference_set = my_set.difference(new_set)
                print(f"Difference of {my_set} and {new_set}: {difference_set}")
            except ValueError:
                print("Invalid input. Please enter valid integers.")

        elif choice == "8":
            print(f"Set length: {len(my_set)}")

        elif choice == "9":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1-9.")


if __name__ == "__main__":
    main()
