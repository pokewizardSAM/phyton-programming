student_records = []

def add_student():
    roll = int(input("Enter student roll number: "))
    name = input("Enter student name: ")
    student_records.append((roll, name))
    student_records.sort()
    print("Student added successfully!")

def search_by_roll():
    roll = int(input("Enter roll number to search: ")) 
    i = 0
    j = len(student_records) - 1
    while i <= j:
        mid = (i + j) // 2
        if student_records[mid][0] == roll:
            print(f"Name for roll {roll} is {student_records[mid][1]}")
            return
        elif roll < student_records[mid][0]:
            j = mid - 1
        else:
            i = mid + 1
    print("Roll number not found")

while True:
    print("1. Add Student")
    print("2. Search by Roll Number")
    print("3. Exit")
    
    choice = int(input("Enter choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        search_by_roll()
    elif choice==3:
        break
    else:
        print("Invalid choice")