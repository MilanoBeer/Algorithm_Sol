# 23.08.25 / 15:31 ~ 

# N개 물건
# 무게 W, 가치 V
# 최대 K
import sys
def input():
    return sys.stdin.readline().rstrip()

# N개 물건 / 최대한계 K
N, K = map(int, input().split())
w_v = [[0, 0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for n in range(N):
    w, v = map(int, input().split())
    w_v.append([w, v])

# 순회 : 행 -> 첫번째 w, v - 모든 무게경우에 대해서
for i in range(1, N+1):
    for j in range(1, K+1):
        # w[i], v[i]기준으로 i무게만큼 넣을 수 있는지 / 
        weight = w_v[i][0]
        price = w_v[i][1]

        # i층 -> 물건 구별
        # j열 -> 무게! 

        # 현재 물건을 못 넣으면 -> 위의값을 그대로 가져올 것 
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            # 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + price)


# for line in dp:
#     print(line)

print(dp[N][K])
