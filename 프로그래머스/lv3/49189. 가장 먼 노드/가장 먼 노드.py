# 23.08.04 / 19:45 ~ 
from collections import deque

def bfs(v, mat, visited):
    dq = deque()
    dq.append(v)
    visited[v] = 0
    
    while dq:
        cur = dq.popleft()
        
        for nx in mat[cur]:
            if visited[nx] == -1:
                visited[nx] = visited[cur] + 1
                dq.append(nx)

def solution(n, edge):
    answer = 0
    
    # n개의 노드
    # 1번 -> 가장 멀리떨어진 노드의 갯수 = 최단경로, 간선갯수 가장 많이 
    
    # IDEA
    # 1번 노드로부터, 각 정점까지 떨어진 거리를 일단 다 기록
    # 가장 max값이, 겹치는게 있는지 확인할것
    
    # 그래프 만들기 
    mat = [[] for _ in range(n+1)]
    for a, b in edge:
        mat[a].append(b)
        mat[b].append(a)
        
    # visited 정점
    visited = [-1] * (n+1)
    bfs(1, mat, visited)
    
    visited.sort(reverse = True)
    answer = visited.count(visited[0])
    
    return answer