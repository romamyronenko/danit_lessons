# def my_gen():
#     print(1)
#     yield print(2)
#     print(3)
#     return ['asd',1]
#
#
# x = my_gen()
# next(x)
#
# try:
#     next(x)
# except Exception as e:
#     ...
# # next(x)
# # next(x)

# def fib_generator():
#     nums = [0, 1]
#
#     while True:
#         yield nums[-1]
#         nums.append(nums[0] + nums[1])
#         nums.pop(0)
#
#
# fib = fib_generator()

# for i in fib:
#     print(i)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# def some_action(name, count):
#     for i in range(count):
#         print(f'{name}-{i}')
#         yield
#
#     return 42
#
#
# t1 = some_action('fff', 5)
# t2 = some_action('ddd', 10)
#
# tasks = [t1, t2]
#
# while tasks:
#     task = tasks.pop(0)
#     try:
#         next(task)
#     except StopIteration as e:
#         print(e.args[0])
#         continue
#     else:
#         tasks.append(task)

"""asyncio"""
# import asyncio
# import time


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
#
#     print(1)
#     await task1
#     print(2)
#     await task2
#     print(3)
#
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))

"""
server using select
"""
import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        resp = await session.get("http://google.com")
        print(resp.status)
        print(await resp.text())


asyncio.run(main())
