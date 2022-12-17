import sys
input = sys.stdin.readline

N, M = map(int, input().split()); 
mat = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)] 

# input dp matrix 
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + mat[i-1][j-1]

K = int(input())

for k in range(K):
    sum = 0
    I, J, X, Y = map(int, input().split())
    sum = dp[X][Y] - dp[X][J-1] - dp[I-1][Y] + dp[I-1][J-1]
    print(sum)