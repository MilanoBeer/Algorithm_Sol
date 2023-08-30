# 16:15 ~ 

N, K = map(int, input().split())
cost = []
for n in range(N):
    cost.append(int(input()))
cost.insert(0, 0)

# 행 -> 가치정보 / 열 -> k원 정1보
# dp[i][j] : 0 ~ i번째 동전까지 사용해서, j원을 만들 때, 적어도 i번째 동전을 사용할때의 경우의 수 
dp = [0] * (K+1)

# init first low
# for i in range(1, K+1):
#     if cost[0] <= i:
#         dp[i] = 1 # 하나의 동전으로 만들 수 있는 경우는 모두 1가지 뿐
#     else:
#         dp[i] = dp[i-1]
dp[0] = 1
# print("init :", dp)
# dp 
for r in range(1, N+1):
    for c in range(1, K+1):
        if cost[r] <= c:
            dp[c] += dp[c - cost[r]]

# print(dp)
print(dp[K])

# 경우의 수 / 동전 중복 사용가능
# dp[i] = 가치의 합이 i가 되도록하는 조합 경우의 수 
# dp[1] 에 대해 -> cost의 배열돌면서 만들 수 있는 조합
# dp[2] -> cost배열 돌면서, 확인