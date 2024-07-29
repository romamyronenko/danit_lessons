"""
тестування бота

трішки про гіт
    що таке гіт?

    гіт зберігає лише зміни

    створення гіт репозиторію
    клон
    перший коміт

    створення гілки
    merge vs rebase

    пул реквест

    .gitignore


SQL
https://w3schoolsua.github.io/sqltryit/trysql_select_all.html

трохи про типи даних

CREATE TABLE - створює нову таблицю
DROP TABLE - видаляє таблицю
INSERT INTO - вставляє нові дані в базу даних

SELECT - витягує дані з бази даних
UPDATE - оновлює дані в базі даних
DELETE - видаляє дані з бази даних

CREATE DATABASE - створює нову базу даних
ALTER DATABASE - змінює базу даних
ALTER TABLE - змінює таблицю
CREATE INDEX - створює індекс (ключ пошуку)
DROP INDEX - видаляє індекс


https://www.w3schools.com/sql/sql_create_table.asp



рефакторинг!(якщо буде час)
"""

import sqlite3

con = sqlite3.connect("tutorial.db")

cursor = con.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);"""
)


class Persons:
    id = ...


# cursor.execute(
#     """INSERT INTO Persons(PersonID, LastName, FirstName, Address, City)
#     VALUES(2, "Myrasdonenko", "Romaasdn", "...", "Kasdyiv");"""
# )
# con.commit()

result = cursor.execute("""SELECT * from Persons;""")
print(result.fetchall())
# cursor.execute("DELETE FROM Persons WHERE LastName=\"Myrasdonenko\"")
# con.commit()

cursor.execute(
    """UPDATE Persons
    SET City="Odesa"
    WHERE FirstName="Roman";"""
)
con.commit()
