# 1초 / 512MB

# 21:11 ~ 

# 무방향 / N개 정점 / M개의 간선 / 1부터 N번 
# 가중치는 모두 1
# Condition 
    # 인접정점 -> 내림차순으로 방문 ***** 

# output : 방문순서 출력

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# input
# N : 5이상 100,000이하 / M : 1이상, 200,000이하 / R : N이하 
N, M, R = map(int, input().split())
mat = [[] for _ in range(N+1)]
cnt = 1

# 탐색 dfs 함수
def dfs(start):
    global cnt 

    visited[start] = cnt

    # start연결지점 확인
    for i in mat[start]:
        # 방문한적이 없다면
        if visited[i] == 0:
            cnt += 1
            # call dfs(해당정점))
            dfs(i)
    return 



for m in range(M):
    u, v = map(int, input().split())
    mat[u].append(v)
    mat[v].append(u)

# 내림차순 정렬
for i in mat:
    i.sort(reverse=True)

# 탐색시작 : 시작점은 1 
visited = [0] * (N+1)
dfs(R)
for i in range(1, N+1):
    print(visited[i])