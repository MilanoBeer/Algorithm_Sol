# 2초 / 128MB
# 23.06.29
# 09:27 ~

# 자기보다 큰 사람이 왼쪽에 몇 명 있었는지 
# 1 ~ N

import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 1이상, 10이하 *** 
_data = list(map(int, input().split()))

# 1. 완탐? 
# 2. DP 
# 3. 그리디
# 4. 스택, 큐
# 5. 정렬 알고리즘

_ans = [0] * (N+1)

def check(idx, n, strd):
    # print(*_ans[:-1])
    # print("check : ", idx, n, strd)
    cnt = 0
    for i in range(idx):
        if _ans[i] > n:
            cnt += 1
    # print("check : ", idx, n, strd, "cnt :", cnt)
    if strd == cnt:
        return True
    else:
        return False

def dfs(n):
    if n == N:
        # 이때 정상적인지 확인! 채우는 도중이 아니라!
        isOrder = True
        for i in range(N):
            # 6 2 3 4 7 5 1 
            if not check(i, _ans[i], _data[_ans[i] - 1]):
                isOrder = False
                break 
        if isOrder:
            print(*_ans[:-1])

        return 
    
    tmp = _data[n]
    # print("n :", n, ", tmp:", tmp)

    for i in range(tmp, N):
        if _ans[i] == 0:
            # 왼쪽에 더 큰 숫자들 카운트 맞는지 확인
            # 0 ~ i-1까지 / n+1 보다 큰 숫자들 카운트 
            # print(_ans)
            # if check(i, n+1, tmp):
            _ans[i] = n+1 # _ans[2] = 1 # -, -, 1, - 
            dfs(n+1)
            _ans[i] = 0

dfs(0)