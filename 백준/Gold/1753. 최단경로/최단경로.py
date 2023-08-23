# 23.08.23 / 10:31 ~

import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()

INF = sys.maxsize
V, E = map(int, input().split())
start = int(input())

mat = [[] for _ in range(V+1)]

for e in range(E):
    u, v, w = map(int, input().split())
    mat[u].append((v, w))

dist = [INF] * (V+1)
dist[start] = 0

# init heapq
hq = []
heapq.heappush(hq, (0, start))

while hq:
    cost, cur_v = heapq.heappop(hq)

    # backtracking
    if dist[cur_v] < cost:
        continue

    # update
    for nxt, n_cost in mat[cur_v]:
        if dist[nxt] > cost + n_cost:
            dist[nxt] = cost + n_cost
            heapq.heappush(hq, (dist[nxt], nxt))

for x in range(1, V+1):
    if dist[x] == INF:
        print("INF")
    else:
        print(dist[x])