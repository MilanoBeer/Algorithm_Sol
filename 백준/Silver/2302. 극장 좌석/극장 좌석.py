# 2초 / 128MB
# 23.05.25 
# 23:22 ~ 24:30 / 
# 완탐 -> DFS + 백트래킹을 생각했는데 DP유형.. 

# 한줄 / 1 ~ N번
# 기본은 자기좌석 / 왼 or 오른쪽으로 옮기기 가능
# VIP회원
    # 반드시 자기자리만

# VIP 좌석번호 주어질때, 사람들이 좌석에 앉을 수 있는 서로 다른 방법 수

# IDEA : DFS + Backtracking 

# 좌석 갯수 / 1이상, 40이하 
N = int(input()) 
M = int(input()) # 고정석 갯수 / 0이상, N이하 

vip = []
for m in range(M):
    vip.append(int(input()))

if N >= 2:
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    ans = 1
    start_idx = 1
    for v in vip:
        ans *= dp[v-start_idx]
        start_idx = v+1
    ans *= dp[N - start_idx + 1]
    print(ans)
else:
    print(1)
