from collections import deque


def bfs(V):
    # 시작점 큐에 담기 
    queue = [V]
    visited[V] = True

    while queue:
        currV = queue.pop(0)
        print(currV, end=' ')

        for i in range(1, N+1):
            # 연결성, 방문여부 검사
            if mat[currV][i] == 1 and visited[i] == False:
                queue.append(i) # queue에 추가 
                visited[i] = True

def dfs(V):
    visited[V] = True
    print(V, end=' ')
    for i in range(N+1):
        if mat[V][i] == 1 and visited[i] == False:
            dfs(i)


# 정점갯수 N, 간선갯수 M
N, M, V = map(int, input().split())

mat = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    fr, to = map(int, input().split())
    mat[fr][to] = 1
    mat[to][fr] = 1
    

visited = [False] * (N+1); 

dfs(V)
print()
visited = [False] * (N+1); 
bfs(V)

