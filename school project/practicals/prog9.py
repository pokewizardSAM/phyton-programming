import csv
records = []
def show_menu():
  print()  
  print("Employee Records")
  print("1. Search Records")
  print("2. View Records")
  print("3. Exit")
  choice = int(input("Enter choice: "))
  perform_action(choice)
def perform_action(choice):
  if choice == 1:
    search_records()
  elif choice == 2:  
    view_records()
  elif choice == 3:
    exit()
  else:
    print("Invalid option")
def search_records():
  emp_no = int(input("Enter employee number to search: "))
  search_record(emp_no) 
def search_record(emp_no):
  for record in records:
    if record['emp_no'] == emp_no:
      print(record['emp_no'], record['salary'])
      return
  print("Employee number not found")
def view_records():
  print("Emp No.\tSalary")
  for record in records:
    print(record['emp_no'], '\t', record['salary']) 
with open('employees.csv', 'w+') as file:
  reader = csv.reader(file)
  # next(reader)
  for row in reader:
    records.append({'emp_no': int(row[0]), 'salary': float(row[1])})
while True:
  show_menu()