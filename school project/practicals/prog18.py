import mysql.connector

def search_employee(employee_number):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Alibha98',
            database='empprec'
        )

        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM employees WHERE id = %s', (employee_number,))
        record = cursor.fetchone()

        if record:
            print("Employee Record:")
            print("ID:", record[0])
            print("Name:", record[1])
            print("Department:", record[2])
            print("Salary:", record[3])
        else:
            print("Employee not found with Employee Number:", employee_number)

        cursor.close()
        conn.close()

    except :
        print("Error:")

employee_number_to_search = input("enters the emp id:")

search_employee(employee_number_to_search)
