# reference : https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/

from socket import socket
from _thread import start_new_thread

# 서버 binding
print('############')
print('Server Start')
print('############')
multiserver = socket()
multiserver.bind(('localhost', 8082))

# 동시 접속자가 늘어나면 가장 앞에 있는 사람의 Message 을 받지 못한다.
multiserver.listen(5)

# TODO
# 서버가 끊어지면 client 에 모든 연결이 끊어지도록 한다.


# 여러명의 유저를 받을수 있도록 설계합니다.
def threaded_client(connection):
    while True:
        msg = connection.recv(2048)
        print('Message from client : {}'.format(msg.decode('utf-8')))
        # msg 에 아무것도 없으면 while 구문을 벗어난다.
        if not msg:
            break
        connection.sendall(msg)
    connection.close()


thread_count = 0
while True:
    client, addr = multiserver.accept()
    print('Connected from {} to {}'.format(addr[0], addr[1]))
    start_new_thread(threaded_client, (client, ))
    thread_count += 1
