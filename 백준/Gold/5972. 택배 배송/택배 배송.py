# 23.10.13 / 

import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
mat = [[] for _ in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    mat[a].append((b, c))
    mat[b].append((a, c))

# 1 -> N
def dijk(start):
    # init dist array : INF, start = 0
    INF = sys.maxsize
    dist = [INF] * (N+1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        # pop : dist, vertex
        cost, vtx = heapq.heappop(hq)

        # backtracking: 현재 vtx까지의 dist가, cost보다 작을 떄 
        if dist[vtx] < cost:
            continue

        # for , vertex, cost 
        for nvtx, ncost in mat[vtx]:
            if dist[nvtx] > cost + ncost:
                dist[nvtx] = cost + ncost
                heapq.heappush(hq, (dist[nvtx], nvtx))
    
    return dist[N]

print(dijk(1))
