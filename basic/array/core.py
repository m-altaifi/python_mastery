import array

def main():
    # Initialize an array of integers (typecode 'i')
    my_array = array.array('i')
    
    while True:
        print("\nArray Operations Menu:")
        print("1. Display array")
        print("2. Add element")
        print("3. Remove element by value")
        print("4. Remove element by index")
        print("5. Access element by index")
        print("6. Slice array")
        print("7. Count occurrences of an element")
        print("8. Reverse array")
        print("9. Get length")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            print("\nCurrent array:", my_array)
            
        elif choice == '2':
            try:
                num = int(input("Enter number to add: "))
                my_array.append(num)
                print(f"Added {num}. Updated array: {my_array}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
        elif choice == '3':
            if not my_array:
                print("Array is empty.")
            else:
                try:
                    num = int(input("Enter number to remove: "))
                    my_array.remove(num)
                    print(f"Removed {num}. Updated array: {my_array}")
                except ValueError:
                    print("Number not found in array.")
                    
        elif choice == '4':
            if not my_array:
                print("Array is empty.")
            else:
                try:
                    index = int(input("Enter index to remove: "))
                    my_array.pop(index)
                    print(f"Removed element at index {index}. Updated array: {my_array}")
                except (ValueError, IndexError):
                    print("Invalid index.")
                    
        elif choice == '5':
            if not my_array:
                print("Array is empty.")
            else:
                try:
                    index = int(input("Enter index: "))
                    print(f"Element at index {index}: {my_array[index]}")
                except (ValueError, IndexError):
                    print("Invalid index.")
                    
        elif choice == '6':
            if not my_array:
                print("Array is empty.")
            else:
                try:
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                    sliced = my_array[start:end]
                    print(f"Slice from {start} to {end}: {sliced}")
                except ValueError:
                    print("Invalid indices.")
                    
        elif choice == '7':
            if not my_array:
                print("Array is empty.")
            else:
                try:
                    num = int(input("Enter number to count: "))
                    count = my_array.count(num)
                    print(f"'{num}' occurs {count} time(s) in the array.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    
        elif choice == '8':
            if not my_array:
                print("Array is empty.")
            else:
                my_array.reverse()
                print(f"Reversed array: {my_array}")
                
        elif choice == '9':
            print(f"Array length: {len(my_array)}")
            
        elif choice == '10':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-10.")

if __name__ == "__main__":
    main()