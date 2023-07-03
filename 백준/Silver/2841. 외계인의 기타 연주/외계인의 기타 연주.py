# 1초 / 256MB
# 10:36 ~ 

# 5번 프랫 -> 그대로 7번 프랫
# 더 빠른 번호 프랫을 연주하려면, 그때는 기존꺼 떼야함

# 손가락 움직인다 : "프렛을 한 번 누르거나 / 떼는 거"

import sys
def input():
    return sys.stdin.readline().rstrip()

# N : 50만 / P : 30만
N, P = map(int, input().split())
SIZE = 300001
# 순서대로..
stacks = [[0] * SIZE for _ in range(7)] # append? assign? 
_top = [-1] * 7

cnt = 0
for n in range(N):
    num, p = map(int, input().split())

    # 첫 push
    if _top[num] == -1:
        _top[num] += 1
        stacks[num][_top[num]] = p 
        cnt += 1
        continue

    # num줄의 맨 위에 줄보다, 지금 p가 더 크면, 
    if stacks[num][_top[num]] < p:
        _top[num] += 1
        stacks[num][_top[num]] = p
        cnt += 1
    # num줄의 맨 위에 줄보다, 지금 p가 더 작으면, 
    elif stacks[num][_top[num]] == p:
        continue
    else:     
        # _top[num] = 0
        while _top[num] != -1 and stacks[num][_top[num]] > p:
            _top[num] -= 1
            cnt += 1
        if stacks[num][_top[num]] == p:
            continue

        _top[num] += 1
        stacks[num][_top[num]] = p
        cnt += 1
    # print("num ;", num, ", p:", p, "cnt :", cnt)
print(cnt)