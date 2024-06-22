
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N, A, B = map(int, input().split())

adjList = [[] for _ in range(N+1)]
ans = sys.maxsize

for n in range(N-1):
    a, b, val = map(int, input().split())
    adjList[a].append((b, val))
    adjList[b].append((a, val))

def dijk(start):
    INF = sys.maxsize
    hq = []
    
    dist = [INF] * (N+1)
    dist[start] = 0
    
    heapq.heappush(hq, (dist[start], start))

    while hq:
        val, cur = heapq.heappop(hq)
        for nxt, cost in adjList[cur]:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                heapq.heappush(hq, (dist[nxt], nxt))

    return dist

# A에 대한 다익스트라 호출 # B에 대한 다익스트라 호출
dist_a = dijk(A)
dist_b = dijk(B)

if A == B:
    ans = 0
else:
    # A에 연결된 리스트 목록 뽑고 
    # 순회 : 최솟값 갱신 
    # for nxt, cost in adjList[A]:
    #     if nxt != B:
    #         ans = min(ans, dist_b[nxt])
    # # B에 연결된 리스트 목록 뽑고
    # # 순회 : 최솟값 갱신
    # for nxt, cost in adjList[B]:
    #     if nxt != A:
    #         ans = min(ans, dist_a[nxt])
    for cur in range(1, N+1):
        for nxt, _ in adjList[cur]:
            ans = min(ans, dist_a[cur] + dist_b[nxt])

print(ans)


