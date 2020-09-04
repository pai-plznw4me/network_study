from socket import socket
import random

client = socket()
client.connect(('localhost', 1122))

while True:
    a = random.randint(0, 10)
    client.send(str(a).encode())
    msg = client.recv(1024)

    if msg.decode() == 'GameOver':
        print(msg)
        break

client.close()
