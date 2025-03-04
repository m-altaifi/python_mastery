def main():
    my_tuple = ()

    while True:
        print("\nTuple Operations Menu:")
        print("1. Display tuple")
        print("2. Create new tuple")
        print("3. Access element by index")
        print("4. Slice tuple")
        print("5. Check if element exists")
        print("6. Concatenate with another tuple")
        print("7. Count occurrences of an element")
        print("8. Get length")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            print("\nCurrent tuple:", my_tuple)

        elif choice == "2":
            try:
                elements = input("Enter elements for new tuple (separated by spaces): ").split()
                my_tuple = tuple(elements)  # Convert input to tuple
                print(f"Created new tuple: {my_tuple}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            if not my_tuple:
                print("Tuple is empty.")
            else:
                try:
                    index = int(input("Enter index: "))
                    print(f"Element at index {index}: {my_tuple[index]}")
                except (ValueError, IndexError):
                    print("Invalid index.")

        elif choice == "4":
            if not my_tuple:
                print("Tuple is empty.")
            else:
                try:
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                    sliced = my_tuple[start:end]
                    print(f"Slice from {start} to {end}: {sliced}")
                except ValueError:
                    print("Invalid indices.")

        elif choice == "5":
            if not my_tuple:
                print("Tuple is empty.")
            else:
                element = input("Enter element to check: ")
                if element in my_tuple:
                    print(f"{element} exists in the tuple.")
                else:
                    print(f"{element} does not exist in the tuple.")

        elif choice == "6":
            try:
                new_elements = input("Enter elements for new tuple (separated by spaces): ").split()
                new_tuple = tuple(new_elements)
                concatenated = my_tuple + new_tuple
                print(f"Concatenated tuple: {concatenated}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "7":
            if not my_tuple:
                print("Tuple is empty.")
            else:
                element = input("Enter element to count: ")
                count = my_tuple.count(element)
                print(f"'{element}' occurs {count} time(s) in the tuple.")

        elif choice == "8":
            print(f"Tuple length: {len(my_tuple)}")

        elif choice == "9":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1-9.")


if __name__ == "__main__":
    main()
