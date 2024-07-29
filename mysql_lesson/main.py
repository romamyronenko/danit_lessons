"""
стосовно ДЗ
    1. завантажувати лише файли, що стосуються ДЗ
    2. вказуйте в головному файлі прізвище, ім'я та умови завдання
    3. якщо потрібна "посилена" перевірка(стиль коду, імена змінних, якість алгоритмів і тд), теж вказати в коментарі в ПЕРШОМУ рядку
        (лише для ДЗ з Web HW3)


Класи навіщо потрібні і як використовувати?

environment variables
or, and що повертає
x = d.get("...") or 10




чи треба встановлювати?


sudo apt install mysql-server
sudo mysql
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1'



mysql -u root -p


***

    CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';

pip install mysql-connector-python





"""

# import mysql.connector
#
# connect = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='1',
# )
# cursor = connect.cursor()
# cursor.execute('create database mydb;')
# cursor.execute('use mydb;')
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS `Groups`(
# id integer primary key NOT NULL UNIQUE,
# Name TEXT NOT NULL);
# """)
# print(connect)
# # print(connect.)
# import mysql.connector
#
# connect = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='1',
#     database='test_db'
# )
# with connect, connect.cursor() as cursor:
#
#     # cursor.execute("create database test_db;")
#     # cursor.execute("use test_db;")
#
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS `Groups`(
#     id integer primary key NOT NULL UNIQUE,
#     Name TEXT NOT NULL);
#     """)
