def main():
    my_dict = {}
    
    while True:
        print("\nDictionary Operations Menu:")
        print("1. Display dictionary")
        print("2. Add key-value pair")
        print("3. Remove key-value pair")
        print("4. Access value by key")
        print("5. Check if key exists")
        print("6. Update dictionary with another dictionary")
        print("7. Get all keys")
        print("8. Get all values")
        print("9. Get length")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            print("\nCurrent dictionary:", my_dict)
            
        elif choice == '2':
            try:
                key = input("Enter key: ")
                value = input("Enter value: ")
                my_dict[key] = value
                print(f"Added {key}: {value}. Updated dictionary: {my_dict}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            if not my_dict:
                print("Dictionary is empty.")
            else:
                key = input("Enter key to remove: ")
                if key in my_dict:
                    del my_dict[key]
                    print(f"Removed {key}. Updated dictionary: {my_dict}")
                else:
                    print(f"Key '{key}' not found in dictionary.")
                    
        elif choice == '4':
            if not my_dict:
                print("Dictionary is empty.")
            else:
                key = input("Enter key to access: ")
                if key in my_dict:
                    print(f"Value for key '{key}': {my_dict[key]}")
                else:
                    print(f"Key '{key}' not found in dictionary.")
                    
        elif choice == '5':
            if not my_dict:
                print("Dictionary is empty.")
            else:
                key = input("Enter key to check: ")
                if key in my_dict:
                    print(f"Key '{key}' exists in the dictionary.")
                else:
                    print(f"Key '{key}' does not exist in the dictionary.")
                    
        elif choice == '6':
            try:
                new_dict = {}
                pairs = input("Enter key-value pairs for new dictionary (format: key1:value1 key2:value2): ").split()
                for pair in pairs:
                    key, value = pair.split(":")
                    new_dict[key] = value
                my_dict.update(new_dict)
                print(f"Updated dictionary: {my_dict}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '7':
            print(f"Keys in dictionary: {list(my_dict.keys())}")
            
        elif choice == '8':
            print(f"Values in dictionary: {list(my_dict.values())}")
            
        elif choice == '9':
            print(f"Dictionary length: {len(my_dict)}")
            
        elif choice == '10':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-10.")

if __name__ == "__main__":
    main()