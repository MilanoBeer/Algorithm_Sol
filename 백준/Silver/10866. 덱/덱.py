# 0.5초 / 256MB
# 18:05 ~ 

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
que = deque()

def ifEmtpy():
    if len(que) == 0:
        print(-1)

for _ in range(N):
    _info = list(input().split())

    if len(_info) == 2:
        if _info[0] == 'push_back':
            que.append(_info[1])
        else:
            que.insert(0, _info[1])
    else:
        if _info[0] == 'pop_front':
            if len(que) != 0:
                print(que.popleft())
            else:
                ifEmtpy() 
# 2, 1 
        elif _info[0] == 'pop_back':
            if len(que) != 0:
                print(que[-1])
                que.pop()
            else:
                ifEmtpy()

        elif _info[0] == 'size':
            print(len(que))
        elif _info[0] == 'empty':
            if len(que) == 0:
                print(1)
            else:
                print(0)
        elif _info[0] == 'front':
            if len(que) != 0:
                print(que[0])
            else:
                ifEmtpy()
        elif _info[0] == 'back':
            if len(que) != 0:
                print(que[-1])
            else:
                ifEmtpy()


