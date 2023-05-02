lst = []
while True:
    print("1. Insert element")
    print("2. Delete element")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to insert: "))
        lst.append(value)
    elif choice == 2:
        print("1. Delete by value")
        print("2. Delete by position")
        print("3. Delete by list slice")
        delete_choice = int(input("Enter your choice: "))
        if delete_choice == 1:
            value = int(input("Enter the value to delete: "))
            lst.remove(value)
        elif delete_choice == 2:
            position = int(input("Enter the position to delete: "))
            lst.pop(position)
        elif delete_choice == 3:
            start = int(input("Enter the start index of slice: "))
            end = int(input("Enter the end index of slice: "))
            lst[start:end] = []
        print("List after deletion: ", lst)
    else:
        break
print("Exiting program")

