import time
import json
import socket

HOST = '??????' # sensor device's IP or hostname (localhost)
PORT = 65431    # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        s.sendall(b'get-data')
        data = s.recv(1024).decode('utf-8')
        print('Received from socket server : ', data)
        time.sleep(0.5)
