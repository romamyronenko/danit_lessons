"""
min
sum
count


unique
primary key





autoincrement

foreign key

join

Групування та агрегатні функції:
    GROUP BY, HAVING.
    Агрегатні функції: COUNT, SUM, AVG, MAX, MIN.


Сортування результатів:
    ORDER BY.


З'єднання таблиць:
    INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN.
    Використання ALIAS для таблиць та колонок.

нормалізація БД
"""

import sqlite3

con = sqlite3.connect("mydb.db")
# con = sqlite3.connect(':memory:')

con.execute("PRAGMA foreign_keys = ON")

cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Students (
	id integer primary key NOT NULL UNIQUE,
	Name TEXT NOT NULL,
	GroupID INTEGER NOT NULL,
    FOREIGN KEY(GroupID) REFERENCES Groups(id)
    );"""
)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Groups (
        id integer primary key NOT NULL UNIQUE,
        Name TEXT NOT NULL
    );"""
)

# cursor.execute("ALTER TABLE Persons AUTO_INCREMENT=100;")
# cursor.execute(
#     'INSERT INTO Groups(id, Name) VALUES (123, "IO-123");'
# )
# cursor.execute(
#     'INSERT INTO Students(Name, GroupID) VALUES ("Roman", 123);'
# )

res = cursor.execute(
    """
SELECT Students.id, Students.Name, Groups.Name 
FROM Students
LEFT JOIN Groups ON Students.GroupID=Groups.id;
"""
)
print(res.fetchall())

con.commit()
