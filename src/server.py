import socket
import csv
import time
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt

COLORS = ['b', 'g', 'r']

def process_connection(sock, addr, results):
    bytes_received = 0
    start = time.time()
    ys = [0]

    if results:
        ys = ys * len(results[0])

    results.append(ys)

    while True:
        data = sock.recv(4096*8)
        bytes_received += len(data)
        if not data: break
        if time.time() - start <= 1: continue

        ys.append(bytes_received*8/1000000)
        
        print("{} Mb/s".format((bytes_received*8)/1000000.0))
        start = time.time()
        bytes_received = 0

def plot(results):
    while(True):
        plt.clf()
        for i in range(len(results)):
            plt.plot(results[i], color=COLORS[i])
        plt.pause(0.001)


HOST = ('', 4000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)

results = []
Thread(target=plot, args=[results]).start()

while True:
    server.listen(1)
    sock, addr = server.accept()
    new_thread = Thread(target=process_connection, args=[sock, addr, results])
    new_thread.start()
