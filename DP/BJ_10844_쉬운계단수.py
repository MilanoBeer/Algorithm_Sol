# 0을 제외한 한자릿수도 계단수

# 1 <= N <= 100
N = int(input())
DP = [[0] * 10 for _ in range(N)]

# init
DP[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    DP[i][0] = DP[i-1][1]
    DP[i][9] = DP[i-1][8]
    for k in range(1, 9):
        DP[i][k] = DP[i-1][k-1] + DP[i-1][k+1]

print(sum(DP[N-1])%1000000000)