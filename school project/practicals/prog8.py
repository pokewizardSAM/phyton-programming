import pickle
import os

records = []

def show_menu():
    print("\nStudent Records")
    print("1. Add New Student")
    print("2. Update Marks")
    print("3. View Records")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    perform_action(choice)

def perform_action(choice):
    if choice == 1:
        add_student()
    elif choice == 2:
        update_marks()
    elif choice == 3:
        view_records()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")

def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    records.append({'roll':roll, 'name':name, 'marks':marks})
    print("Record added successfully!")

def update_marks():
    roll = int(input("Enter roll number to update marks: "))
    new_marks = int(input("Enter new marks: "))
    update_record(roll, new_marks)
    
def update_record(roll, new_marks):
    for record in records:
        if record['roll'] == roll:
            record['marks'] = new_marks
            print("Marks updated successfully!")
            return
    print("Roll number not found")
        
def view_records():
    for record in records:
        print(record['roll'], record['name'], record['marks'])

if os.path.exists('student_data.pkl'):
  with open('student_data.pkl', 'rb') as f:
    records = pickle.load(f)

while True:
  show_menu()

  with open('student_data.pkl', 'wb') as f: 
    pickle.dump(records, f)