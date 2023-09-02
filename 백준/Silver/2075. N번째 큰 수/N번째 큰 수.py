import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
hq = []

for i in range(N):
    tmp = list(map(int, input().split()))

    for e in tmp:
        if len(hq) < N:
            heapq.heappush(hq, e)
        else:
            # 현재 최솟값보다 e가 더 작으면 -> 지나가기 : hq에는 최댓값부터 채워져야하므로, 더 작은건 지나간다
            if e > hq[0]:
                tmp = heapq.heappop(hq)
                heapq.heappush(hq, e)
print(heapq.heappop(hq))