# 양방향

import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N, E = map(int, input().split())

mat =[[] for _ in range(N+1)]

for e in range(E):
    a, b, c = map(int, input().split())
    mat[a].append((b, c))
    mat[b].append((a, c))

v1, v2 = map(int, input().split())

# 시작 1 , 목표 N 
# 가능한 경로
# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N

# 1번 dist # v1 dist # v2 dist
INF = sys.maxsize
def dijk(v):
    global N, mat 

    dist = [INF] * (N+1)
    dist[v] = 0
    hq = []
    heapq.heappush(hq, (0, v))

    while hq:
        cur_p, cur_v = heapq.heappop(hq)

        if dist[cur_v] < cur_p:
            continue

        for nv, np in mat[cur_v]:
            if dist[nv] > cur_p + np:
                dist[nv] = cur_p + np
                heapq.heappush(hq, (dist[nv], nv))

    return dist 


dist_1 = dijk(1)
dist_v1 = dijk(v1)
dist_v2 = dijk(v2)


ans = -1
if dist_1[v1] != INF and dist_v1[v2] != INF and dist_v2[N] != INF:
    ans = dist_1[v1] + dist_v1[v2] + dist_v2[N]

if dist_1[v2] != INF and dist_v2[v1] != INF and dist_v1[N] != INF:
    ans = min(ans, dist_1[v2] + dist_v2[v1] + dist_v1[N])

print(ans)

