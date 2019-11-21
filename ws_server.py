import asyncio
import websockets
import pickle
import json
import socket

Gateway_IP = '192.168.43.???'   # Gateway's IP for websocket server
HOST = 'localhost' # sensor device's IP; if localhost, the sensor device role
                   # is also played by the same machine
PORT = 65431    # Port to listen on (non-privileged ports are > 1023)

async def hello(websocket, path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            line = await websocket.recv()
            print(f"< {line}")
            if line is None:
                return
        
            s.sendall(b'get-data')
            data = s.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            await websocket.send(data)

start_server = websockets.serve(hello, Gateway_IP, 8866)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


