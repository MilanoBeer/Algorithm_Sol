# 0.5초 -> 약 1000만회  / 128 MB 
import heapq
import sys
input = sys.stdin.readline
# 한 도시 출발 -> ㄷ른 도시에 도착하는 M개의 버스 => M개의 간선
# Purpose
    # A번째 도시 -> B까지 가는 버스비용의 최소화

# N개의 도시 : 1이상 1000이하 
N = int(input())
# M개의 버스가 있음 
M = int(input())

INF = 999999999
graph = [[] for _ in range(N+1)]

for m in range(M):
    # 출발도시 번호 / 도착지의 번호 / 버스 비용 : 0이상, 100,000미만 
    fr, to, cost = map(int, input().split())
    graph[fr].append([cost, to])

# 구하고자하는 출발도시, 도착도시 번호: 갈 수 있는 경우만 주어진다 
A, B = map(int, input().split()) 
dist = [INF] * (N+1)
# visited = [False] * (N+1)
def dij(start):
    # init heapq
    hq = []
    heapq.heappush(hq, [0, start])

    while hq:
        # pop
        cost, min_vert = heapq.heappop(hq)

        # ***** 백트래킹 요소 *****
        # 최소거리에 있는 min_vert까지 가는 거리가, 현재 dist[min_vert] 에 저장된 값보다 크다면, 
        if cost > dist[min_vert]:
            # WHY : dist[min_vert]에는 이미 여러 번의 갱신을 통해 작은 값이 들어가 있을 수 있음, 
            # 그런데 큐에 초기에 INF->작은값으로 push됐던 값이 큐를 비우는 과정에서 나오게 된다
            # 그 때는 이미 dist가 상당히 최소화 되고 난 이후가 될 것임 
            # -> 늦게 나온, 초기의 cost값이 더 크다면, 이전에 이미 더 작은 값으로, 다른 점들을 갱신한 이후다! 더 이상 볼 필요가 없다! 백트래킹!
            continue

        # 기존 vertex중, min_vert를 통해 거쳐 도착햇을 때 최소인지 확인
        for d, i in graph[min_vert]:
            if dist[i] > cost + d:
                dist[i] = cost + d
                heapq.heappush(hq, [dist[i], i])                

dij(A)
print(dist[B])
