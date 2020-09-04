# reference : https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8082))

while True:
    msg = input('Input : ')
    client.send(msg.encode('utf-8'))
    ret_msg = client.recv(1024)
    print('받은 데이터 : {}'.format(ret_msg.decode("utf-8")))
