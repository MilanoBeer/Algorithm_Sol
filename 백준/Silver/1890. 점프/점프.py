# 1초 / 128MB
# 17:20 ~ 
from collections import deque
import sys
input = sys.stdin.readline

# N x N 
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

# init dp 
dp = [[0]*(N) for _ in range(N)]
dp[0][0] = 1

# Traversal 
for r in range(N):
    for c in range(N):
        # 방문한적이 있고( = 첫번째 칸을 통해서 지나친 칸) 
        if dp[r][c] != 0 and mat[r][c] != 0:
            gap = mat[r][c]

            # 오른쪽
            if c + gap < N:
                dp[r][c + gap] += dp[r][c]
            # 아래 
            if r + gap < N:
                dp[r + gap][c] += dp[r][c]
print(dp[N-1][N-1])