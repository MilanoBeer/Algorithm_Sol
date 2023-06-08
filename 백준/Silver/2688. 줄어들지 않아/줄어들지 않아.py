# 1초 / 128MB
# 23.06.08
# 13:10 ~ 

# T갯수는 1000, n의 최대가 64 => 64자리에 대해 미리 구하는게 낫다고 생각



T = int(input()) 

# dp : 1차원? 1차원?
# n =1  -> 0 ~ 9 => 10개 
# n = 2 -> 55 
# 줄어들지 않는 경우 : 뒤의 수에 의해 결정된다 
# 2차원 dp 
    # 행 => n자릿수 
    # 열 => 0, 1, .. 9 
dp = [[1] * (10) for _ in range(65)]

for i in range(2, 65):
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for t in range(T):
    n = int(input())

    # n자릿수 -> n행의 sum
    print(sum(dp[n]))