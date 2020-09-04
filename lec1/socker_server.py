from socket import *

# ipv4, TCP 을 의미한다.
print(AF_INET)
server = socket(AF_INET, SOCK_STREAM)

# address family
server.bind(('localhost', 8080))

# 몇 명 동시 접속자
# server 가 몇명의 connection 을 생성할건지 파악
server.listen(3)

# client 의 요청이 올때까지 대기
connection, addr = server.accept()

# while 구문이 계속 돌기 때문에 ack , deack 을 만들어 dack 이면 server 의 connection 을 끊어야 한다.
while True:
    print('Server 가 데이터를 받았습니다.')
    msg = connection.recv(1024)

    msg = msg.decode('utf-8')
    print('받은 메세지 : {}'.format(msg))
    connection.send(msg.encode('utf-8'))