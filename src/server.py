import socket
import csv
import time
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt

def process_connection(sock, addr):
    bytes_received = 0
    start = time.time()
    ys = []

    while True:
        data = sock.recv(4096)
        bytes_received += len(data)
        if not data: break
        if time.time() - start <= 1: continue

        ys.append(bytes_received/1000)
        # plt.plot(ys)
        # plt.pause(0.0001)

        print(bytes_received*8)
        start = time.time()
        bytes_received = 0


HOST = ('', 4000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)

while True:
    server.listen(1)
    sock, addr = server.accept()
    new_thread = Thread(target=process_connection, args=[sock, addr])
    new_thread.start()
