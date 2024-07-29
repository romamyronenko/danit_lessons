import pymysql

# Параметри підключення
host = 'database-2.cpqkkk48wgrk.us-east-1.rds.amazonaws.com'
user = 'admin'
password = 'rrrr1111'

# Підключення до сервера MySQL
connection = pymysql.connect(
    host=host,
    user=user,
    password=password
)

# Створення об'єкта cursor для виконання SQL-запитів
cursor = connection.cursor()

# SQL-запит для створення бази даних
create_db_query = "CREATE DATABASE mydatabase"

# Виконання SQL-запиту для створення бази даних
cursor.execute(create_db_query)

print("Database created successfully!")

# Закриття з'єднання з базою даних
cursor.close()
connection.close()
