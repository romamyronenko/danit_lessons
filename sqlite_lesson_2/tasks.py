"""
створити таблицю Students яка має такі поля

Ім'я | Прізвище | Клас | Вік

додайте декілька учнів(створіть зручний інтерфейс для додавання)

напишіть запит, який показує всіх учнів, які молодше 8 років

напишіть запит, який покаже кількість учнів в кожному класі

***

створіть схему БД для зберігання наступних даних

Студенти(група, ПІБ)
Розклад
Викладачі(ПІБ, предмети які викладає)
Оцінки учнів за семестр з кожного предмету


БД має бути у 3 НФ
"""

import sqlite3

con = sqlite3.connect("students.db")

cursor = con.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Students (
    PersonID INTEGER PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255),
    Birthdate DATE,
    Class INTEGER
);"""
)

# cursor.executemany(
#     "INSERT INTO Students(LastName, FirstName, Birthdate, Class) VALUES (?, ?, ?, ?)",
#     [
#         ('Roman', "Myronenko", "2000-10-10", 5),
#         ('Ivan', "ASdqwr", "2015-10-10", 8),
#         ('ASD', "das", "2010-10-10", 7),
#         ('123', "df", "2020-10-10", 5),
#         ('789', "987", "2017-10-10", 6),
#     ],
# )
# con.commit()

result = cursor.execute("SELECT * FROM Students;")
for i in result:
    print(i)

print("\n\n")
# result = cursor.execute("""
# SELECT COUNT(PersonID), Class
# FROM Students
# GROUP BY Class;
# """)
# result = cursor.execute("""
# SELECT TIMESTAMPDIFF (Birthdate, Birthdate, \"2024-06-06\") FROM Students;
# """)
for i in result:
    print(i)
# print(result.fetchall())
