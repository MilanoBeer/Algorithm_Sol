N = int(input())

t_p_list = [list(map(int, input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i + t_p_list[i][0], N+1):
        if dp[j] < dp[i] + t_p_list[i][1]:
            dp[j] = dp[i] + t_p_list[i][1]
print(dp[-1])