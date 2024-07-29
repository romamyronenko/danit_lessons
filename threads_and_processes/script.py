import threading


def ceasar(text: str, shift):
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    encoded = []
    for char in text:
        if char in alphabeth:
            i = alphabeth.index(char)
            encoded.append(alphabeth[i + shift])
        else:
            encoded.append(char)
    return "".join(encoded)


test = "This is the house that jack built".lower()
print(test, "\n", ceasar(test, 2))


def t1(fname):
    with open(fname, "w") as f:
        test = "This is the house that jack built".lower()
        print(test, "\n", ceasar(test, 2))
        f.write(f"{ceasar(test, 2)}\n")


th1 = threading.Thread(target=t1, args=("t1.txt",))
th2 = threading.Thread(target=t1, args=("t2.txt",))

th1.start()
th2.start()
