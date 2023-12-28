import mysql.connector

def search_employee(emp_id):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rohit09',
            database='empprec'
        )

        cursor = conn.cursor()

        cursor.execute('SELECT * FROM employees WHERE id = %s', (emp_id,))
        record = cursor.fetchone()

        if record:
            print("Employee Record:")
            print("ID:", record[0])
            print("Name:", record[1])
            print("Department:", record[2])
            print("Salary:", record[3])
        else:
            print("Employee not found with Employee Number:", emp_id)

        cursor.close()
        conn.close()

    except:
        print("Error:")

emp_id_to_search = input("Enter the Employee ID:")

search_employee(emp_id_to_search)