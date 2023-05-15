# 1초 / 512MB

# 23.05.15 
# 13:44 ~ 

# 무방향 그래프 
# 1번 ~ 
# 모든 간선 가중치 1 => 다익스트라일 필요는 x
 
# 정점R에서 시작
# 인접 -> 오름차순 방문
from collections import deque
import sys
input = sys.stdin.readline

CNT = 2
def bfs(R):
    global CNT 

    # init queue
    queue = deque()
    queue.append(R)
    visited[R] = 1

    while queue:
        cur= queue.popleft() # pop

        # 연결된 지점들 확인
        cnt = 1
        for v in mat[cur]:
            # if아직 방문안했으면
            if visited[v] == 0:
                # 방문처리, 큐에 추가 
                visited[v] = CNT
                queue.append(v)
                CNT += 1
            
# 정점 수 / 간선 수 / 시작 정점 R 
# 5이상, 10만 이하 / 1이상, 20만 이하 / 
N, M, R = map(int, input().split())

mat = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())

    mat[u].append(v)
    mat[v].append(u)

# 접점정보들 오름차순 정렬
for n in range(1, N+1):
    mat[n].sort()

visited = [0] * ( N+1 )

# R에서 탐색시작
bfs(R)

for i in range(1, N+1):
    print(visited[i])