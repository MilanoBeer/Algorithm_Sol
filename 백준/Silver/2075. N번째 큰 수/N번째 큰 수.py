# 16:10 ~ 16:44 , 메모리 초과 , pypy3 -> 틀림 / 
# ~ 17:04, gg... / 

import heapq

N = int(input())
hq = []

for i in range(N):
    tmp = list(map(int, input().split()))

    for e in tmp:
        if len(hq) < N:
            heapq.heappush(hq, e)
        else:
            # 현재 최솟값보다 e가 더 작으면 -> 지나가기 : hq에는 최댓값부터 채워져야하므로, 더 작은건 지나간다
            if e < hq[0]:
                continue
            else:
                tmp = heapq.heappop(hq)
                heapq.heappush(hq, e)
print(heapq.heappop(hq))