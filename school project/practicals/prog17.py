import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Alibha98',
    database='empprec'
)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100),
        salary DECIMAL(10, 2)
    )
''')

employees = [
    ('John Doe', 'HR', 50000),
    ('Jane Smith', 'Marketing', 60000),
    ('Alice Johnson', 'Engineering', 75000),
]

insert_query = 'INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)'
cursor.executemany(insert_query, employees)

conn.commit()

cursor.execute('SELECT * FROM employees')
records = cursor.fetchall()

print("Employee Records:")
for record in records:
    print(record)

cursor.close()
conn.close()
