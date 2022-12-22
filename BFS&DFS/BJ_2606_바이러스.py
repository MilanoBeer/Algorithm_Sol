from collections import deque
# 1번에서 바이러스 시작

N = int(input())
E = int(input())

mat = [[0] * (N+1) for _ in range(N+1)]
queue = deque()
visited = [False] * (N+1)
cnt = 0

for i in range(E):
    fr, to = map(int, input().split())
    mat[fr][to] = 1
    mat[to][fr] = 1

def bfs():
    global cnt
    # 1번부터 시작
    queue.append(1)
    visited[1] = True

    while queue:
        currV = queue.popleft()

        for i in range(N+1):
            if visited[i] == False and mat[currV][i] == 1:
                visited[i] = True
                cnt = cnt + 1
                queue.append(i)

bfs()
print(cnt)