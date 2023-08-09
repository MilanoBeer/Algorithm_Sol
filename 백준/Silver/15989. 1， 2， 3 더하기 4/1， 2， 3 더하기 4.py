# 23.08.09 / 09:50 ~ 10:20

# n : 1이상, 10,000이하
dp = [1] * 10001

# 매번 n시점에서 할 수 있는거
# n-1의 값에서 + 1
# 

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(input())

for t in range(T):
    n = int(input())
    print(dp[n])