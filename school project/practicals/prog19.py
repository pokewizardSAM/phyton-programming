import mysql.connector

def update_employee_record():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Alibha98',
            database='empprec'
        )

        if conn.is_connected():
            emp_id = input("Enter employee number to update: ")
            new_salary = input("Enter new salary for the employee: ")
            new_dept = input("Enter new department for the employee: ")

            cursor = conn.cursor()

            update_query = "UPDATE employees SET salary = %s, department = %s WHERE ID = %s"
            data = (new_salary, new_dept, emp_id)

            cursor.execute(update_query, data)

            conn.commit()

            print(f"Employee record updated for employee number {emp_id}")

            cursor.close()
            conn.close()

    except mysql.connector.Error as error:
        print("Error:", error)

update_employee_record()