from socket import socket
from _thread import start_new_thread

server = socket()
server.bind(('localhost', 1122))

# 동시 접속 가능한 유저의 수
n_user = 5
server.listen(n_user)

goal = 1000000

# 유저별 thread 할 당 후
global_count = 0


def thread_allocate(connection, address):
    while True:
        global global_count

        value = int(connection.recv(2048).decode())
        print('{}:{} , value:  {}'.format(address[0], address[1], value))
        global_count = global_count + value
        print('global count : {}'.format(global_count))
        # 만약 특정 값이 커지면 client 의 접속을 모두 끊어 버립니다.
        if goal < global_count:
            connection.sendall('GameOver'.encode())

            break
        elif goal > global_count:
            connection.sendall('Not Finish'.encode())

    connection.close()


connect_user = 0
while True:
    client, addr = server.accept()
    connect_user += 1
    print('################################################')
    print('Connected from {}:{}'.format(addr[0], addr[1]))
    print('################################################')
    # message
    start_new_thread(thread_allocate, (client, addr))
