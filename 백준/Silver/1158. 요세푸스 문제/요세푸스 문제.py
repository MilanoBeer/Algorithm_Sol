# 2초 / 256MB
# 23:51 ~ 

# 1번 ~ N번
from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

# 7, 3
# 1, 2, 3, 4, 5, 6, 7
# -> 3, 6, 2, 7, 5, 1, 4

# 없어진 원소의 다음부터 1, 2, [3] !!
_data = deque(list(range(1, N+1)))
_res = []

while len(_data) != 0:
    _data.rotate(-(K-1))
    _res.append(_data[0])

    _data.popleft()

print("<", end='')
for i in range(len(_res)):
    if i == len(_res)-1:
        print(_res[i], end='')
    else:
        print(_res[i], end=', ')
print(">")

    
