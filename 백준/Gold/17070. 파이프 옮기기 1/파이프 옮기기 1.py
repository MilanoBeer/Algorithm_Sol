# 1초 / 512MB
# 23.05.20
# 11:45 ~ 12:14 / 15:40 ~ 

# BFS
from collections import deque

N = int(input()) # N * N 
mat = [list(map(int, input().split())) for _ in range(N)]

# dp init
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

for i in range(1, N):
    if mat[0][i] != 1:
        dp[0][0][i] = 1
    else:
        break 

# dp 
for r in range(1, N):
    for c in range(1, N):
        # 해당 지점에 대각선으로도 올 수 있는지 
        if mat[r][c] != 1 and mat[r-1][c] == 0 and mat[r][c-1] == 0:
            # 대각선포함해서 가능
            dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1]  + dp[2][r-1][c-1]

        # 대각선으로는 못오면
        if mat[r][c] != 1:
            dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1] 
            dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])

