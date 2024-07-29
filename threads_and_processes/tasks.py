"""

Написати програму, яка паралельно завантажує вміст декількох веб-сторінок за допомогою threading.

***

Створити програму, яка моніторить зміни в декількох директоріях одночасно за допомогою threading.

***

Виконати розподіл великої задачі на декілька процесів для паралельного обчислення з використанням multiprocessing.

***

Розділити великий масив даних на частини та обробляти кожну частину в окремому процесі за допомогою multiprocessing.

***

Використати ThreadPoolExecutor для завантаження декількох веб-сторінок паралельно.

***

Використати ThreadPoolExecutor для обробки списку чисел, піднесення їх до квадрату.

***

Використати ProcessPoolExecutor для обчислення факторіалів великого набору чисел.

***

Розділити великий масив даних на частини і обчислювати суму кожної частини паралельно за допомогою ProcessPoolExecutor.

***

Написати програму, яка завантажує та обробляє великі файли паралельно за допомогою threading.

***

Створити програму, яка розпаралелює обчислення математичних виразів з використанням multiprocessing.

***

Використати ThreadPoolExecutor для паралельного виконання запитів до API.

***

Використати ProcessPoolExecutor для обробки зображень в паралельних процесах.

***

Написати програму, яка здійснює паралельне стиснення файлів за допомогою threading.

***

Створити програму, яка розпаралелює обробку відео файлів за допомогою multiprocessing.

***

Використати ThreadPoolExecutor для паралельної обробки текстових даних.

***

Використати ProcessPoolExecutor для паралельного тренування моделей машинного навчання.

***

Написати програму для паралельного збирання даних з веб-сторінок за допомогою threading.

***

Створити програму, яка виконує паралельне резервне копіювання файлів за допомогою multiprocessing.

***

Використати ThreadPoolExecutor для паралельної обробки логів.

***

Використати ProcessPoolExecutor для паралельного аналізу великих наборів даних.

"""

"""

програма, яка паралельно шифрує текст шифром цезаря з різним зсувом

***

програма яка моніторить паралельно 5 файлів і в разі змін виводить вміст

***

клієнт-сервер на socket які паралельно "читають" та "відправляють"

"""

#
# import threading
#
# threads = []
# for i in range(3):
#     threads.append(threading.Thread(target=caesar_to_file, args=(s, i)))
#
# for i in range(3):
#     threads[i].start()


# import multiprocessing
#
#
# processes = []
#
# for i in range(3):
#     processes.append(multiprocessing.Process(target=caesar_to_file, args=(s, i)))
#
# if __name__ == '__main__':
#     for i in range(3):
#         processes[i].start()
#
# import concurrent.futures
#
# alph = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
#
#
# def get_caesar_symbol(symbol, shift):
#     if symbol not in alph:
#         return symbol
#     index = alph.index(symbol)
#     index = (index + shift) % len(alph)
#     return alph[index]
#
#
# def get_caesar_str(s, shift):
#     retval = ""
#     for char in s:
#         retval += get_caesar_symbol(char, shift)
#     return retval
#
#
# def caesar_to_file(s, i):
#     file_name = f'file_{i}.txt'
#     with open(file_name, 'w+', encoding='utf-8') as f:
#         f.write(get_caesar_str(s, i))
#
#
# s = "тестовий рядок"
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for i in range(10):
#         futures.append(executor.submit(caesar_to_file, s, i))
#
#     for future in futures:
#         print(future.result())
"""
програма яка моніторить паралельно 5 файлів і в разі змін виводить вміст
"""


# time.sleep(1)


# def start_monitoring(i):
#     while True:
#         try:
#             with open(f'file_{i}.txt', 'r') as f:
#                 new_content = f.read()
#         except FileNotFoundError:
#             with open(f'file_{i}.txt', 'a+') as f:
#                 content = f.read()
#                 new_content = content
#
#         if new_content != content:
#             print(new_content)
#             content = new_content


# import os.path
# import threading
#
# lock = threading.Lock()
#
#
# def start_monitoring(i):
#     filename = f"file_{i}.txt"
#     content = ""
#
#     if not os.path.exists(filename):
#         open(filename, 'w+').close()
#
#     while True:
#         with open(filename, 'r') as f:
#             new_content = f.read()
#
#         if new_content != content:
#             with lock:
#                 print(new_content)
#
#             content = new_content
#
#
# threads = []
# for i in range(3):
#     threads.append(threading.Thread(target=start_monitoring, args=(i,)))
#
# for i in range(3):
#     threads[i].start()
