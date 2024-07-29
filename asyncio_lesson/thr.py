import threading

results = []


def foo():
    return 42


thread1 = threading.Thread(target=foo)
thread1.start()
res = thread1.join()
print(res)
