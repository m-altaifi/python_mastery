def main():
    my_list = []
    
    while True:
        print("\nList Operations Menu:")
        print("1. Display list")
        print("2. Add element")
        print("3. Remove element")
        print("4. Access element by index")
        print("5. Slice list")
        print("6. Sort list")
        print("7. Reverse list")
        print("8. Get length")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            print("\nCurrent list:", my_list)
            
        elif choice == '2':
            try:
                num = int(input("Enter number to add: "))
                my_list.append(num)
                print(f"Added {num}. Updated list: {my_list}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
        elif choice == '3':
            if not my_list:
                print("List is empty.")
            else:
                try:
                    num = int(input("Enter number to remove: "))
                    my_list.remove(num)
                    print(f"Removed {num}. Updated list: {my_list}")
                except ValueError:
                    print("Number not found in list.")
                    
        elif choice == '4':
            if not my_list:
                print("List is empty.")
            else:
                try:
                    index = int(input("Enter index: "))
                    print(f"Element at index {index}: {my_list[index]}")
                except (ValueError, IndexError):
                    print("Invalid index.")
                    
        elif choice == '5':
            if not my_list:
                print("List is empty.")
            else:
                try:
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                    sliced = my_list[start:end]
                    print(f"Slice from {start} to {end}: {sliced}")
                except ValueError:
                    print("Invalid indices.")
                    
        elif choice == '6':
            if not my_list:
                print("List is empty.")
            else:
                my_list.sort()
                print(f"Sorted list: {my_list}")
                
        elif choice == '7':
            if not my_list:
                print("List is empty.")
            else:
                my_list.reverse()
                print(f"Reversed list: {my_list}")
                
        elif choice == '8':
            print(f"List length: {len(my_list)}")
            
        elif choice == '9':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-9.")

if __name__ == "__main__":
    main()