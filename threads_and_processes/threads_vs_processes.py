import multiprocessing
import threading
import time
from typing import Union


def foo():
    for i in range(10000000):
        pass


def boo():
    for i in range(100):
        time.sleep(0.01)


def boo1():
    for i in range(100):
        time.sleep(0.1)


def create_threads(func, threads_count: int):
    threads = []
    for i in range(threads_count):
        threads.append(threading.Thread(target=func))
    return threads


def create_processes(func, processes_count: int):
    threads = []
    for i in range(processes_count):
        threads.append(multiprocessing.Process(target=func))
    return threads


def run_all(tasks: list[Union[threading.Thread, multiprocessing.Process]]):
    for i in tasks:
        i.start()


def join_all(tasks: list[Union[threading.Thread, multiprocessing.Process]]):
    for i in tasks:
        i.join()


def run_and_get_time(create_func, func, count, name):
    start = time.time()

    tasks = create_func(func, count)

    run_all(tasks)
    join_all(tasks)
    end = time.time()
    print(f"{name:11} | {count:5} | {end - start:20}")


def run_in_one_thread(func, count, name):
    start = time.time()

    for _ in range(count):
        func()
    end = time.time()
    print(f"{name:11} | {count:5} | {end - start:20}")


if __name__ == "__main__":
    # func = foo
    # func = boo
    func = boo1
    print(f"{'name':^11} | {'count':^5} | {'run time':^20} ")
    for i in [1, 2, 3, 5, 10, 20, 50, 100]:
        run_in_one_thread(func, i, "One Thread")
        run_and_get_time(create_threads, func, i, "Treads")
        run_and_get_time(create_processes, func, i, "Processes")
