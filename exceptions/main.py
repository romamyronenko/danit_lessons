"""
Виключення - це

приклад обробки ZeroDivisionError

семантичні помилки - програма працює, але не атк як очікував програміст
види виключень


синтаксичні
    SyntaxError
        невірне значення, конструкція
        виникає коли синтаксичний аналізатор не може розпізнати структуру
        наприклад, значення 0ab за жодних умов не може існувати в пайтоні, так само конструкція
        for:

    IndentationError
        Специфічний тип SyntaxError, що виникає, коли неправильно використовуються пробіли або табуляція для відступів.

    синтаксичні помилки не можно спіймати (за виключенням якщо ви використовуєте eval та імпортів)


помилки виконання
    виникають коли в ході виконання програми сталося щось непередбачуване

синтаксичний аналіз в імпортованих модулях виконується ПІСЛЯ імпорту


спочатку працюэє синтаксичний аналізатор який перевіряє УВЕСЬ код,
незалежно виконувався він чи ні(наприклад, всередині функції)

якщо синтаксичний аналізатор відпрацював без помилок, тоді код починає "виконуватися"
інтерпретатор спочатку


основні типи помилок
https://husky-glazer-9f3.notion.site/b7d85cd8b64b4c2bbfdb6a6c7883221a

try:
    ...
except ValueError as e:
    ...
except ZeroDivisionError:
    ...
else:
    ... # no exceptions
finally:
    ... # any way


"користувацькі" виключення
    можна створити власне виключення, створивши клас, який наслідується від Exception
        class MyException(Exception):
            pass
    щоб викликати виключення треба написати ключове слово raise після чого тип виключення, наприклад:
        raise TypeError
        raise TypeError('error message')

    власні виключення можна розширити, визначивши метод __init__ та додавши параметри
    class SalaryNotInRangeError(Exception):
        def __init__(self, salary, message="Salary {salary} is not in (5000, 15000) range"):
            self.salary = salary
            self.message = message
            super().__init__(self.message.format(salary=salary))


assert/AssertionError


"""

# def foo():
#  print(111)
# a = 10
# b = 0
#
#
# def div(a, b):
#     return a / b
# try:
#     print(div(a, b))
# except ZeroDivisionError as e:
#     print(111, e)
# # import asd
# print(12)
# # def foo():
# #     x = 0ab
#
# # class A:
# #     x = a0b # виконається
#     # def __init__(self):
#     #     x = 0ab # не виконається поки не буде створено об'єкт класу
#
#     # @property
#     # def 0b(self):
#     #     return a0b
# print(12)
# nums = [1, 2, 3]
# nums[3]
# # 3 / 0
# def      boo():
#  'as'
#
# def aaa():
#     'asd'
# # for + 4
# # a = 0b32  # синтаксична
# # for:
# def check_number(a):
# 'asd'
#
# a = 5
# result = check_number(a)
# print(result)
#
# def foo():
# try:
#     def foo():
#     ''
# except IndentationError:
#     print(111)
# print(111)
# try:
#     import script
# except SyntaxError:
#     print(111)
# for + 'a'

# class Foo:
#     pass
# try:
#     raise Foo
# except TypeError:
#     print()
#
#
# class SalaryNotInRangeError(Exception):
#     def __init__(self, salary, message="Salary {salary} is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message.format(salary=salary))
#
#
# raise SalaryNotInRangeError(100)


# # 10 / 0
# #
# # int('a')
#
# try:
#     import mymodule
#
# except SyntaxError:
#     print(111)
#
# with open('newfile', 'r') as f:
#     print(f.read())

# a = [1, 23]
# print(a.value())

# from mymodule import a
#
# print(a)

# try:
#     1 / 0
# except ZeroDivisionError:
#     pass
# except Exception as e:
#     print(type(e))
#     print(str(e))
# import my_package
# print(a1)
# print(my_module2)


# class SalaryNotInRangeError(Exception):
#     def __init__(self, salary, message="Salary {salary} is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message.format(salary=salary))
#
# salary = 600
#
# if salary < 5000 or salary > 15000:
#     raise SalaryNotInRangeError(salary)

# assert 2 == 1, 'sdcsdf'

password = "asasdd"

assert password == "asd", "wrong password"

# if password != 'asd':
#     raise ValueError
print(password)
