# 10:00 ~ 10: 35 / 
# Error : 메모리 초과 -> 
# 0.75초 / 256MB 

# 각 타일 -> 0 or 1 # 0 + 0 -> 00 

# N을 이루는 모든 2진수열 생성불가 

# N : 1이상, 100만이하 
N = int(input())

dp = [0] * (1000000+1)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

# Output : 2진 수열 갯수를 % 15746 
print(dp[N])