"""
яка система оцінювання?

скільки спроб?

функції генератори з використанням yield?(для наступного заняття) не проходили

скільки разів можна здати дз?
чи можете ви його переробити поки я не оцінив?


декоратор з параметром через клас

https://superfastpython.com/asyncio-vs-threading/#What_is_Asyncio
https://www.codingdeeply.com/asyncio-vs-threading-in-python/

threading lock vs rlock
https://stackoverflow.com/questions/22885775/what-is-the-difference-between-lock-and-rlock

mutex vs semaphore
https://www.geeksforgeeks.org/mutex-vs-semaphore/

semaphore
https://www.linkedin.com/pulse/understanding-semaphores-synchronization-resource/

https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods

паралельне[ та асинхронне] програмування

мютекси та семафори потрібні для безпечного доступу до спільних ресурсів
    mutex - "MUTual EXclusion" - "взаємний виняток"

    semaphore - мютекст для декількох потоків

    атомарність операцій

deadlock

нащо потрібно паралельне та асинхронне програмування?

GIL - global interpreter lock - мютекс, який дозволяэ одночасно виконувати лише один потік
навіщо потрібен?
    Це необхідно, оскільки керування пам’яттю CPython (еталонна реалізація Python) не є потоково-безпечним.
    Python використовує підрахунок посилань для керування пам’яттю. Це означає, що об’єкти, створені в Python,
    мають змінну підрахунку посилань, яка відстежує кількість посилань, які вказують на об’єкт. Коли цей рахунок
    досягає нуля, пам'ять, зайнята об'єктом, звільняється. Проблема полягала в тому, що ця змінна підрахунку посилань
    потребувала захисту від умов змагання, коли два потоки збільшували або зменшували її значення одночасно.
    Якщо це станеться, це може спричинити витік пам’яті, який ніколи не звільниться, або неправильне звільнення
    пам’яті, поки посилання на цей об’єкт все ще існує.


як уникнути:
    використовувати процеси, а не потоки


1. пришвидшення обчислень
2. не чекати відповіді від серверу, а робити в цей час іншу задачу

процес та потік

процес - екземпляп програми, наприклад, інтерпретатор Python, один GIL для кожного процесу
потік - об'єкт ОС, який виконує інструкції процесу
        об'єкт у  процесі, який можна "запланувати для виконання"


висновок
через GIL threading працює більш як "конкурентні" потоки, а не паралельні які "змагаються" за час виконання

різниця з asyncio:
    потоками керує ОС, корутини є значно "дешевші"

процес:
    окремий простір пам'яті
    уникає обмежень GIL
    використовує переваги кількох ЦП і ядер
    дочірні процеси можна знищити/перервати

    більший обсяг пам'яті
    довше запускається
    більш складна комунікація


потік
    мало пам'яті
    спільна пам'ять

    обмеження GIL
    не можна перервати/знищити


багатопоточність, конкурентність, асинхронність


використання

процеси
    multiprocessing, concurrent.futures.ProcessPoolExecutor

потоки
    threading, concurrent.futures.ThreadPoolExecutor

асинхронність
    asyncio



threading
    Thread

    start
    join

    Lock
    Rlock - відпустити може лише той самий потік

    Semaphore
    BoundedSemaphore - не можна відпустити більше ніж "захоплено"


multiprocessing


ThreadpoolExecutor
ProcessPoolExecutor
"""

# import time


# import threading
#
# # Загальна змінна
# counter = 0
#
# # Створюємо мютекс
# lock = threading.RLock()
#
#
# def do(num):
#     while True:
#         # with lock
#         lock.acquire()
#         print(num)
#         lock.release()
#
#
# threads = []
# for _ in range(10):
#     thread = threading.Thread(target=do, args=(_,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print("Final counter value:", counter)


# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
#
#
# def sum_chunk(data):
#     return sum(data)
#
#
# data = [i for i in range(1000000)]
# chunk_size = len(data) // 4
# chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
# with ThreadPoolExecutor(max_workers=4) as executor:
#     results = executor.map(sum_chunk, chunks)
#
# total_sum = sum(results)
# print(f"Total sum is {total_sum}")


# class decorator:
#     def __init__(self, param):
#         self.param = param
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func()
#             print(self.param, time.time() - start)
#             return result
#
#         return wrapper
#
#
# @decorator('param')
# def foo():
#     for i in range(100000000):
#         pass
#     return 42
#
#
# async def get_smth():
#     data = ...
#     response = await requests.get(data)
#     print(response.json())
#
#
# async def get_smth_1():
#     data = ...
#     response = await requests.get(data)
#     print(response.json())
#
#
# get_smth()
# get_smth_1()
#
# requests = ...
# requests.get()


import threading

print_lock = threading.RLock()
semaphore = threading.BoundedSemaphore(3)


def foo(param):
    for _ in range(100):
        with semaphore:
            print(param)


n = 5
threads = []
for i in range(n):
    threads.append(threading.Thread(target=foo, args=(i,)))

for i in range(n):
    threads[i].start()
