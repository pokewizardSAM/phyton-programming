import mysql.connector

def delete_employee_record():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Alibha98',
            database='empprec'
        )

        if conn.is_connected():
            print("Connected to MySQL database")

            ID = input("Enter employee number to delete: ")

            cursor = conn.cursor()

            delete_query = "DELETE FROM employees WHERE ID = %s"
            data = (ID,)

            cursor.execute(delete_query, data)

            conn.commit()

            if cursor.rowcount == 0:
                print(f"No employee record found with employee number {ID}")
            else:
                print(f"Employee record with employee number {ID} deleted successfully")

            cursor.close()
            conn.close()

    except mysql.connector.Error as error:
        print("Error:", error)

delete_employee_record()


