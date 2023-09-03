
import sys
import heapq 

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

mat = [[] for _ in range(N+1)]

for m in range(M):
    a, b, p = map(int, input().split())
    mat[a].append((b, p))

s, e = map(int, input().split())

# 출발점 -> 도착점 / 최소비용 / 간선이 양의 가중치 

INF = sys.maxsize
dist = [INF] * (N+1)

# Init
dist[s] = 0
hq = []
heapq.heappush(hq, (0, s))

while hq:
    # pop
    cur_cost, cur_v = heapq.heappop(hq)

    # 백트래킹 : 이미 해당 dist[v]값이 더 작으면 볼 필요 없음. 이전에 갱신된 것임
    if dist[cur_v] < cur_cost:
        continue

    # 순회 : 갈 수 있는 지점들
    for nv, ncost in mat[cur_v]:
        # 확인 : 더 최소비용인가
        if dist[nv] > cur_cost + ncost:
            # 갱신 : dist 배열
            dist[nv] = cur_cost + ncost
            # heappush 
            heapq.heappush(hq, (dist[nv], nv))

print(dist[e])
