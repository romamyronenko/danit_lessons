# echo-client.py

import socket
import threading

HOST = "localhost"
PORT = 5555


def send(s):
    while True:
        message = input("")
        s.sendall(message.encode())


def recv(s):
    while True:
        data = s.recv(1024)
        print(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    send_thread = threading.Thread(target=send, args=(s,))
    recv_thread = threading.Thread(target=recv, args=(s,))

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()

print(f"end message")
