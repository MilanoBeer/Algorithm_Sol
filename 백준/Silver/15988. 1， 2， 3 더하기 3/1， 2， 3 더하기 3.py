# 18:19 ~ 

T = int(input())

dp = [0] * (1000001)

# init
dp[1] = 1
dp[2] = 2
dp[3] = 4

# dp
for i in range(4, 1000001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for t in range(T):
    n = int(input())

    print(dp[n])

