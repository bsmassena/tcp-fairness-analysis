import socket
from threading import Thread

def process_connection(sock, addr):
    bytes_received = 0
    while True:
        data = sock.recv(4096)
        bytes_received += len(data)
        if not data: break
        print(bytes_received)


HOST = ('', 4000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)

while True:
    server.listen(1)
    sock, addr = server.accept()
    new_thread = Thread(target=process_connection, args=[sock, addr])
    new_thread.start()
