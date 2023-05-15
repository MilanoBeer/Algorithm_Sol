# 2초/ 256 MB
# 23.05.15 재도
# 12:00 ~ 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 테스트 케이스 
K = int(input())

# Def 
def find(vert, val):
    # vert에 1 할당
    parent[vert] = val # 시작은 1
    
    # vert에 연결된 지점들에 대해
    for i in graph[vert]:
        # 방문 안했으면 
        if visited[i] == 0:
            # 1의 반대 -1을 할당
            visited[i] = 1
            # parent[i] = -val 
            # return find(i, -val)
            if not find(i, -val):
                return False
        # 방문한 점인데, 현재 vert에 할당된거랑 반대값이면 
        elif visited[i] == 1 and parent[i] != parent[vert]:
            # 지나가기
            continue
        # 방문한 점인데, 현재 vert에 할당된거랑 같으면
        elif visited[i] == 1 and parent[i] == parent[vert]: 
            # 인접, 같은 값, 싸이클
            return False
    return True


for k in range(K):
    # 정점 갯수, 간선 갯수
    # V : 최대 2만 / E : 최대 20만 -> 인접리스트 
    V, E = map(int, input().split())
    # 그래프 DS : 인접 리스트 
    graph = [[] for _ in range(V)]
    visited = [0 for _ in range(V)]

    # 정점정보 : 1부터~ 
    for e in range(E):
        # 간선정보 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # 케이스마다, 이분그래프 판별하기 
    cnt = 0
    parent = [0] * V
    flag = True

    for i in range(V):
        if visited[i] == 0:
            visited[i] = 1
            if not find(i, 1):
                flag = False
                print("NO")
                break 
    if flag:
        print("YES")
    