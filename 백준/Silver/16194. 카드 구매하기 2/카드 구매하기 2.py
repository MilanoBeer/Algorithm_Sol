# 23.07.09
# 13:41 ~ 

# 카드팩 형태로만 구매가능
# 카드팩 종류 : 1개, 2개..N개

# 돈 최소, 카드 N개 
# N개 딱 맞게 사야함

N = int(input())
_list = list(map(int, input().split()))

# dp[N][N(=p)]
dp = [[0] * (N+1) for _ in range(N+1)]

# N이 1일 경우 예외처리
if N == 1:
    dp[N][N] = _list[0]

# 카드를 총 1장 구매하는 최소비용은, p1, p2 ..일때도 p1으로 구매만 가능
for i in range(1, N+1):
    dp[1][i] = _list[0]

for i in range(2, N+1):
    for j in range(1, N+1):
        if j == 1:
            dp[i][j] = _list[0]*i
        elif i < j:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = min(dp[i-j][j] + _list[j-1], dp[i][j-1])

# for line in dp:
#     print(*line)
print(dp[N][N])