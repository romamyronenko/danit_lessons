import sqlite3

# Підключення до БД
conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()


# Функція для виведення всіх записів з таблиці
def print_all_records(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()
    print(f"Records in {table_name}:")
    for record in records:
        print(record)
    print("\n")


# Список всіх таблиць
tables = [
    "Groups",
    "Students",
    "Teachers",
    "Subjects",
    "TeachersSubjects",
    "Days",
    "DaySchedule",
    "Lessons",
    "LessonGroup",
]

# Виведення записів з кожної таблиці
for table in tables:
    print_all_records(table)

# Закриття з'єднання
conn.close()
