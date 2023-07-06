# 1초 / 512MB
# 09:36 ~ 
import copy
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
_data = list(map(int, input().split()))

stacks = []
result = [-1] * N

# data에서 하나씩 뽑아
for i in range(N):
    # stack에 원소가 아직 있고, top원소가 현재 data보다 클동안
    while stacks and stacks[-1][1] < _data[i]:
        idx, popped = stacks.pop()
        # result[id]
        result[idx] = _data[i]
    stacks.append((i, _data[i]))

print(*result)
# 4
# 3, 5, 2, 7
# output
# 5, 7, 7, -1 


