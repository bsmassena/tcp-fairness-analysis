import socket
import string
import random
import sys

def random_string(length=4096):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], 4000))

while True:
    sock.send(random_string().encode())
