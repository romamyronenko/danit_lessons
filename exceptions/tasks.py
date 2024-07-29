"""



Відкриття файлу
Напишіть програму, яка відкриває файл для читання.
Обробіть випадок, коли файл не існує.

***


***

Математичні операції
Напишіть програму, яка обчислює квадратний корінь з числа.
Обробіть випадок, коли число негативне.

***

Словник
Напишіть програму, яка намагається отримати значення з словника за заданим ключем.
Обробіть випадок, коли ключ не існує.

***

Перевірка пароля
Напишіть програму, яка запитує у користувача введення пароля і піднімає виключення, якщо пароль коротший за 8 символів.

***

Напишіть програму, яка читає JSON-файл і обробляє виключення, якщо JSON неправильний.

***

Напишіть програму, яка читає файл, зчитує число з першого рядка та число з другого рядка,
після чого виводить на екран їх частку

***

Напишіть програму, яка запитує у користувача введення дати
у форматі YYYY-MM-DD і обробляє виключення, якщо формат неправильний.

***

Напишіть функцію, яка приймає два аргументи і піднімає виключення, якщо будь-який з них не є числом.
Якщо обидва числа - повертає їх суму

***

Напишіть програму, яка перетворює рядок у верхній регістр і обробляє виключення, якщо вхідні дані не є рядком.

***

Напишіть програму, яка намагається додати елемент до множини та обробляє виключення, якщо елемент не є хешованим.

***

Напишіть програму, яка обробляє виключення у циклі, що намагається поділити числа у списку на 2.

***

напишіть програму, яка читає рядки файлу, де кожен рядок - список у форматі json
для кожного списку програма повертає новий список, кожен елемент якого - відповідний елемент початокового списку,
поділений на наступний
якщо ділення не можливе з будь-яких причин - треба обробити і сповістити про це користувача

***

напишіть декоратор, який обробляє і записує в файл виключення під час виконання функції

приклад файлу:
Exception occurred in function divide: division by zero
Exception occurred in function get_element: list index out of range


***

додати параметри log_file та default_value до декоратору з попереднього завдання

"""

from typing import Any

# def fopen(filename, option='r'):
#     try:
#         with open(filename, option) as file:
#             content = file.read()
#             # jsn = json.loads(content)
#             return content
#     except FileNotFoundError:
#         return None\
"""

Індексація списку
Напишіть програму, яка намагається отримати елемент списку за заданим індексом.
Обробіть випадок, коли індекс виходить за межі списку.


"""
"""
Напишіть програму, яка запитує у користувача введення пароля і піднімає виключення, 
якщо пароль коротший за 8 символів.
"""

"""
що таке декоратор(обгортка)? і чому по суті він не завжди є обгорткою

1. в python будь-що є об'єктом(навіть функція), тому такий код працює

def foo():
    return 42
    
print(foo)

new_func = foo

print(new_func())

2. будь-який об'єкт може повертитися, функція теж

def foo():
    return 42


def boo():
    return foo
    

3. "замикання"

4. як працює @wrapper ?

5. створення декоратору

6. через класи
"""

# def make_multiply(n):
#     def multiply(a):
#         return a * n
#
#     return multiply
# def boo():
#     return 'asd'
#
#
# def create_decorator(text):
#     def decorator(func):
#         def wrapper():
#             print(text)
#             return func()
#
#         return wrapper
#
#     return decorator
#
#
# @create_decorator('user text')
# @create_decorator('asd')
# def foo():
#     return 42
#
#
# foo = create_decorator('user_text')(foo)
# foo = create_decorator('asd')(foo)
# print(foo())


# class BaseA(abc.ABC):
#     @property
#     @abc.abstractmethod
#     def foo(self):
#         pass
#
#
# class A(BaseA):
#     @property
#     def foo(self):
#         return 42
#
#
# a = A()
#
# print(a.foo())
#
#
# class A:
#     @property
#     def foo(self):
#         print('asds')
#         return 42
#
#
# a = A()
#
# print(a.foo)
#
# @create_decorator('asdf')
# def boo():
#     return 42
#
#
# print(foo())
# print(boo())
"""

def decorator(func):
    def wrapper():
        return func()
    return wrapper
"""

# class A:
#     def __init__(self, func, param):
#         self.func = func
#         self.param = param
#
#     def __call__(self, *args, **kwargs):
#         print(f'hello from call, func: {self.func}')
#         print(f'param:{self.param}')
#         return self.func()
#
#
# class DecoratorWIthParam:
#     def __init__(self, param):
#         self.param = param
#
#     def __call__(self, func):
#         return A(func, self.param)
#
#
# @DecoratorWIthParam('asd')
# def foo():
#     return 42


# foo = DecoratorWIthParam('asd')(foo)
# class A:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f'hello from call, func: {self.func}')
#         return self.func()
#
#
# @A
# def foo():
#     return 42
#
#
# # foo = A(foo)
#
# print(foo())

# a = A('asdc')
# print(a())


# foo()
# foo = A(foo)

"""

напишіть декоратор, який обробляє виключення під час виконання функції

"""


def catch_exceptions_decorator(func):
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"exception {type(e).__name__} raised with message '{str(e)}'")

    return wrapper


@catch_exceptions_decorator
def div(a, b):
    return a / b


print(div(1, 10))
print(div(1, 0))
