"""
питання?
про дз з декораторами

декілька слів про потоки та процеси


генератори

iter/next
StopIteration

yield
return

send

генератор чисел Фібоначчі
def fib_generator():
    nums = [0, 1]

    while True:
        yield nums[-1]
        nums.append(nums[0] + nums[1])
        nums.pop(0)

завдання: написати генератор факторіалів(кожен раз повертає факторіал наступного числа)
https://uk.wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB%D1%96%D1%87%D0%BD%D0%B5_%D0%BF%D0%BB%D0%B0%D0%BD%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F

Round Robin
def some_action(name, count):
    for i in range(count):
        print(f'{name}-{i}')
        yield


t1 = some_action('fff', 5)
t2 = some_action('ddd', 10)

tasks = [t1, t2]

while tasks:
    task = tasks.pop(0)
    try:
        next(task)
    except StopIteration:
        continue
    else:
        tasks.append(task)



event loop

asyncio
    Офіційна документація asyncio(зрозуміло, вичерпна і чудово організована) розрахована швидше на творців фреймворків,
    ніж на розробників додатків користувача. Там стільки всього очі розбігаються. А тим часом: "Вам потрібно знати
    всього близько семи функцій для використання asyncio" (c) Юрій Селіванов, автор PEP 492, в якій були додані
    інструкції asyncтаawait


run
gather
create_task
get_event_loop().run_until_complete()

асинхронні http реквести
aiohttp


https://pypi.org/project/aiofiles/
async with/for


асинхронний asyncio socket сервер
асинхронний сервер без async/await

"""

import inspect
import time

"""
1 1 2 3 5 8 13
"""

"""
написати генератор факторіалів
"""

# def fib_generator():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# def factorial_generator():
#     res = 1
#     cur_num = 2
#     while True:
#         yield res
#         res *= cur_num
#         cur_num += 1
#
#
# x = factorial_generator()
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# next(my_gen)
# def task_generator(name, count):
#     for i in range(count):
#         print(name, i)
#         yield
#
#
# task1 = task_generator('aaa', 5)
# task2 = task_generator('bbb', 10)
#
# tasks = [task1, task2]
#
#
# def event_loop():
#     while tasks:
#         task = tasks.pop(0)
#         try:
#             next(task)
#         except StopIteration:
#             pass
#         else:
#             tasks.append(task)
#
#     print('done')
#
#
# event_loop()
"""
tasks = [task1, task2]

task = task1
next(task1)
tasks = [task2, task1]

"""

# import asyncio
#
#
# async def empty_async():
#     return 42
#
#
# async def foo_async():
#     print(1)
#     x = await empty_async()
#     print(x)
#
#
# async def boo_async():
#     print('a')
#     print('b')
#
#
# def empty():
#     return 42
#
#
# def foo():
#     print(11)
#     x = empty()
#     print('dd', x)
#
#
# def boo():
#     print('aa')
#     print('bb')
#
#
# async def main():
#     await asyncio.gather(foo_async(), boo_async())
#
#
# # print(foo())
# # asyncio.run(foo())
# # asyncio.run(boo())
# asyncio.run(main())
# print('\n\n***********\n\n')

# foo()
# boo()
# import asyncio
#
#
# async def fun1(x):
#     print(x ** 2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
#
# async def fun2(x):
#     print(x ** 0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#     await asyncio.sleep(1)
#
#     print(1)
#     await task1
#     print(2)
#     await task2
#     print(3)
#
#
# asyncio.run(main())
import requests

import asyncio
import aiohttp


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time: {end - start}")
        return res

    return wrapper


def time_decorator_async(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        res = await func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time: {end - start}")
        return res

    return wrapper


def unique_decorator(func):
    async def wrapper_async(*args, **kwargs):
        start = time.time()
        res = await func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time: {end - start}")
        return res

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time: {end - start}")
        return res

    if inspect.iscoroutinefunction(func):
        retval = wrapper_async
    else:
        retval = wrapper
    return retval


def foo(url):
    print("start", url)
    response = requests.get(url)
    print("done")
    return response


async def async_foo(url):
    print("start", url)
    async with aiohttp.ClientSession() as session:
        resp = await session.get("http://google.com")
        print("async done")
        return resp


@unique_decorator
async def main(urls):
    tasks = [async_foo(url) for url in urls]
    await asyncio.gather(*tasks)


@unique_decorator
def get(func, urls):
    for url in urls:
        func(url)


urls = [
    "https://www.facebook.com/",
    "http://google.com",
    "https://docs.python.org/3/library/asyncio-task.html#creating-tasks",
]
get(foo, urls)
asyncio.run(main(urls))
