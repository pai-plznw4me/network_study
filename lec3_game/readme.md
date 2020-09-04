# client 2개를 만들어서 게임 누가 먼저 점수 내나 게임 만들기 

### Question 1
게임이 끝나고 서버가 초기화 되고 싶지 않고 점수만 초기화 하고 싶을 때는 어떻게 해야 할까? 
간단하게는 global count 을 심으면 되지만 그러면 다른 문제점들이 생긴다. 

```python
        if goal < global_count:
            connection.sendall('GameOver'.encode())
            global_count = 0 
            break
```
라고 하면 큰 문제가 생긴다. 왜냐면 
user1 이 먼저 게임을 끝내고 user 2가 아직 게임을 하고 있는 도중이라면 
global_count 가 0으로 초기화 되기 때문에 user2 가 다시 게임을 시작하게 된다. 
  
### TODO 
동시 시작 문제 
user 가 방에 대기 하다가 모두 참여하면 게임을 시작하는 형태

### TODO 
동시성 문제
만약 계산 하는데 필요한 시간이 3초라고 하고 t1 시점에 user 1이 
t2 시점에 user2 가 우연히 global_count 에 접근했다. 
t1, t2 시점 모두 global_count 는 동일하다. 
그러면 어떻게 global_count을 update 해야 할까? 

### TODO   
게임이 끝나면 모두에게 동일한 메세지를 보내줘서 멈추고 server 는 초기화 되는것 

 
