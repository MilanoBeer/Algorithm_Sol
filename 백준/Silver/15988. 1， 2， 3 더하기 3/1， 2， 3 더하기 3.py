# 1초 / 512MB
# 23.06.05

T = int(input()) 

dp = [0] * (1000001)

# init
dp[1] = 1
dp[2] = 2
dp[3] = 4

for d in range(4, 1000001):
    dp[d] = (dp[d-3] + dp[d-2] + dp[d-1]) % 1000000009
    
for t in range(T):
    n = int(input()) 
    print(dp[n])
