# BJ_2146_카드2

from collections import deque

N = int(input())
# depue 만들기 
deque = deque([i for i in range(1, N+1)])


# 1장이 될 때까지 
while len(deque) > 1:
    deque.popleft() # 맨 왼쪽에서 pop 
    to_right_num = deque.popleft()
    deque.append(to_right_num)

print(deque[0])