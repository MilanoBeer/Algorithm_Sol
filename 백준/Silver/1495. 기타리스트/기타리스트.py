# 2초 / 128MB
# 23.06.07
# 01:42 ~ 02:42
# 각 곡이 시작하기전, 바꿀 수 있는 볼륨 리스트 

import sys
input = sys.stdin.readline

# 3, 5, 10 
N, S, M = map(int, input().split())
_vol = list(map(int, input().split()))


# OUTPUT : 마지막 곡을 연주할 수 있는 볼륨 중 최댓값 구하기 

# CONDITON : 0이하 x, M보다 큰 값 

# Def DP -> 1차원? 2차원? => 2차원! 
    # ROW : 
    # COL : 

# M값을 포함하기 위해 + 1 / init을 위한 0행을 포함히기 위해 + 1
dp = [[0] * (M+1) for _ in range(N+1)]

dp[0][S] = 1

for i in range(N):
    for j in range(M+1): # 각 볼륨을 확인
        if dp[i][j] == 1: # 값이 있는 경우라면
            tmp1 = j + _vol[i]
            tmp2 = j - _vol[i]

            # 추가 가능한가 
            if 0 <= tmp1 <= M:
                dp[i+1][tmp1] = 1
            if 0 <= tmp2 <= M:
                dp[i+1][tmp2] = 1

# find max 
ans = -1
for i in range(M+1):
    if dp[N][i] == 1:
        ans = i 
print(ans)
    
