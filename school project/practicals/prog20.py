import mysql.connector

def delete_record():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rohit09',
            database='empprec'
        )

        if conn.is_connected():
            emp_id = input("Enter employee ID to delete: ")

            cursor = conn.cursor()

            delete_query = "DELETE FROM employees WHERE ID = %s"
            data = (emp_id,)

            cursor.execute(delete_query, data)

            conn.commit()

            if cursor.rowcount == 0:
                print(f"No employee record found with ID {emp_id}")
            else:
                print(f"Employee record with ID {emp_id} deleted successfully")

            cursor.close()
            conn.close()

    except mysql.connector.Error as error:
        print("Error:", error)

delete_record()