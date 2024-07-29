"""

Асинхронний таймер з зворотнім відліком(декілька)
з різними проміжками(один рахує кожну секунду, інший кожні 5 і тд)

name1 1
name1 2
name2 2
 ***

асинхронні http запити

написати синхронну та асинхронну програму які роблять запити за одними і тими ж адресами
порівняти час виконання для 1, 2, 5 та 10 запитів

***

асинхронне читання та запис файлів
напишіть програму яка записує будь-який текст у 2 файли асинхронно
contents = [
    'a'*1000,
    'asdwqdvc'*1000,
    '12321'*1000
]
***

попередня програма, але програма записує кожну секунду щось у файл протягом 10 секунд


***

моніторинг декількох сайтів на доступність(якщо статус код 200 - все ок)

***
асинхронний геренатор чисел Фібоначчі

"""

# import asyncio
#
# import aiofiles
#
#
# async def main_async():
#     async with aiofiles.open('file', mode='r') as f:
#         contents = await f.read()
#         print(contents)
#
#
# asyncio.run(main_async())
# """
# Асинхронний таймер з зворотнім відліком(декілька)
# з різними проміжками(один рахує кожну секунду, інший кожні 5 і тд)
#
# name1 1
# name1 2
# name2 2
# """
#
#
# async def timer(name, step, process_time):
#     for i in range(0, process_time, step):
#         await asyncio.sleep(step)
#         print(f'{name}: {i + step}')
#
#
# timers = [
#     timer('a', 1, 10),
#     timer('      b', 5, 20),
#     timer('            c', 2, 20),
# ]
#
#
# async def main():
#     await asyncio.gather(*timers)
#
#
# asyncio.run(main())
# import asyncio
#
# import aiofiles
#
# lock = asyncio.Lock()
#
#
# async def read_files(name):
#     async with lock:
#         async with aiofiles.open('file', mode='a') as f:
#             print('start', name)
#             await f.write(name)
#             await f.write(name)
#             await f.write(name)
#             # print(contents)
#             print('end', name)
#
#
# async def main():
#     await asyncio.gather(*tasks)
#
#
# tasks = [
#     read_files('aaa'),
#     read_files('bbb')
# ]
# asyncio.run(main())

# def unique_decorator(func):
#     async def wrapper_async(*args, **kwargs):
#         start = time.time()
#         res = await func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} time: {end - start}")
#         return res
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} time: {end - start}")
#         return res
#
#     if inspect.iscoroutinefunction(func):
#         retval = wrapper_async
#     else:
#         retval = wrapper
#     return retval
#
#
# async def async_write_one(filename, content):
#     async with aiofiles.open(filename, mode='w+') as f:
#         await f.write(content)
#
#
# @unique_decorator
# def write(contents):
#     for i, content in enumerate(contents):
#         with open(f'file_{i}', 'w+') as f:
#             f.write(content)
#
#
# @unique_decorator
# async def async_write(contents):
#     tasks = []
#     for i, content in enumerate(contents):
#         tasks.append(f'async_file_{i}', content)
#
#     tasks = [async_write_one(f'async_file_{i}', content) for i, content in enumerate(contents)]
#
#     await asyncio.gather(*tasks)
#
#
# contents = [
#     'a' * 10000,
#     'asdwqdvc' * 10000,
#     '12321' * 100000000
# ]
# write(contents)
# asyncio.run(async_write(contents))


"""
list dict comprehensions

"""

# # def generator():
# #     yield 1
# #     yield 2
# #     yield 3
# #     yield 4
# tasks = []
# #
# # my_dict = {1:2, 3:4}
# for i in range(20):
#     if i % 2 == 0:
#         tasks.append(i)
#     else:
#         tasks.append(f'a{i}')
#
# tasks_compr = [i for i in range(20) if i % 2]
# dict_compr = {i: str(i) for i in range(20)}
# print(tasks)
# print(tasks_compr)
# print(dict_compr)

#
# def gen():
#     for i in range(10):
#         yield i
#
#
# x1 = [1, 2, 3]
# # x2 = [foo(i) for i in x1]
# x2_map = map(lambda a: a * 10, x1)
# #
# # print(x1)
# # print(x2)
# # print(list(x2_map))
# x2_filter = filter(lambda a: a % 2 == 1, x1)
# x2_reduce = reduce(lambda a, b: a+b, x1)
# print(list(x2_filter))
#
# print(x2_reduce)
#
# """
# [1, 2, 3]
# 6
# """
# from typing import TYPE_CHECKING
#
# if TYPE_CHECKING:
#     from threading import Thread
#
#
# def foo(a: int):
#     print(a)
#
#
# foo(2)
# foo('asd')
"""
public

_protected

__private


"""


# class A:
#     __value = 10
#
#     def _foo(self):
#         pass
#
#     def foo(self):
#         self._foo()
#
#
# a = A()
#
# a.foo()
# a._foo()
# print(a._A__value)
class Stack:
    def __init__(self):
        self._data = []

    def pop(self):
        return self._data.pop()

    def add(self, elem):
        self._data.append(elem)


stack = Stack()

stack.add("")
print(stack.pop())
print(stack._data)
