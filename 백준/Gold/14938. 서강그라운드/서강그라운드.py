# 16:52 ~ 17:32, 9퍼센트에서 틀림 / 

# setting
import sys
import heapq
def input():
    return sys.stdin.readline()

def dijk(start):
    global n, m

    # init 
    INF = sys.maxsize
    hq = []
    heapq.heappush(hq, (0, start))
    dist = [INF] * (n+1)
    dist[start] = 0 
    # 2 -> 1, 3, 5까지 갈 수 있음
    # 3, 0, 3, INF, 4 
    # 다른 지점까지의 거리를 갱신할 때, m비교해서 갱신, 안되면 갱신 x

    while hq:
        cur_cost, cur_vx = heapq.heappop(hq)

        if dist[cur_vx] < cur_cost:
            continue

        for nxt, nxt_cost in mat[cur_vx]:
            if dist[nxt] > cur_cost + nxt_cost:
                if cur_cost + nxt_cost <= m:
                    dist[nxt] = cur_cost + nxt_cost
                    heapq.heappush(hq, (dist[nxt], nxt))
    
    return dist

# 양방향 그래프 
# src 지점 -> 모든 지점을 경우의 수로 둔다 
# 제한조건 : 범위 -> 가중치의 누적합

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items.insert(0, 0)
mat = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    mat[a].append((b, c))
    mat[b].append((a, c))

# 모든 vertex를 시작점으로 다익스트라 탐색 
ans = -1
INF = sys.maxsize
for i in range(1, n+1):
    dist = dijk(i)
    # dist배열에서 INF가 아닌 지점들에 대해, vertex자체의 값들 더하고
    # 최대 갱신
    tmp = 0
    for d in range(1, n+1):
        if dist[d] != INF:
            tmp += items[d]
    ans = max(ans, tmp)

print(ans)