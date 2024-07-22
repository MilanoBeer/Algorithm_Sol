from collections import deque
from unittest import result

# 첫번째 물통이 비어 있을 때, 세번재 물통에 담겨있을 수 있는 물의 양을 '모두' 구하기

A, B, C = map(int, input().split())

# 방문처리
visited = [[False] * ( B+1) for _ in range(A+1)]

result_list = []
c_list = [-1] * (C+1)
queue = deque()

def pour(x, y):
    # 이미 계산했던 경우가 아니라면
    if visited[x][y] == False:
        visited[x][y] = True
        queue.append([x, y])

def bfs(a, b):
    queue.append([a, b])

    while queue:
        x, y= queue.popleft()
        z = C - x - y 

        # 매번 A물통이 비어있는지 검사 
        if x == 0:
            result_list.append(z) 

        # x -> y
        # 부을 양 정하기 : 다 붓거나, 다른 병이 다 채워질때까지 붓거나 
        water = min(x, B - y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, C - z)
        pour(x - water, y)

        # y -> z
        water = min(y, C - z)
        pour(x, y - water)
        # y -> x
        water = min(y, A - x)
        pour(x + water, y - water)

        # z -> x
        water = min(z, A -x)
        pour(x + water, y)
        # z -> y
        water = min(z, B - y)
        pour(x, y + water)

bfs(0, 0)
result_list = list(set(result_list))
result_list.sort() 

for i in result_list:
    print(i, end=' ')

        

            


