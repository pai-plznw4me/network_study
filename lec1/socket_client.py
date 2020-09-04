from socket import *
client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8082))
client.send('hello'.encode('utf-8'))
data = client.recv(1024)
print('받은 데이터 : {}'.format(data.decode("utf-8")))
