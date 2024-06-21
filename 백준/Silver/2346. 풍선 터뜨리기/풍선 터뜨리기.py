# 20:32 

from collections import deque

N = int(input())
_data = list(map(int, input().split()))
visited = list([0] * (N))

ans = [1]
visited[0] = 1
ans_cnt = 1
i = 0
# for i in range(len(_data)):
while True:
    val = _data[i]
    cnt = 0
    tmp = 1

    if val < 0:
        while True:
            if visited[(i - tmp) % N] == 0:
                cnt += 1
            if cnt == abs(val):
                ans.append((i-tmp) % N + 1)
                visited[(i-tmp) % N] = 1
                i = (i-tmp) % N
                ans_cnt += 1
                break

            tmp += 1
    else:
        while True:
            if visited[(i + tmp) % N] == 0:
                cnt += 1
            if cnt == abs(val):
                ans.append((i+tmp) % N + 1)
                visited[(i+tmp) % N] = 1
                i = (i+tmp) % N
                ans_cnt += 1
                break
            tmp += 1

    if ans_cnt == N:
        break 

print(*ans)
