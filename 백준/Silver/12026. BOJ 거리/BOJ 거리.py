# 2초 / 512MB
# 23.06.20
import sys

N = int(input())
_data = list(input())
INF = sys.maxsize

dp = [INF] * (N+1)

# 문자 순서 판단 -> data리스트의 문자보고,, 
match = {'B':'O', 'O':'J', 'J':'B'}

def call_dp(num): # PARAM : 이전에서 몇칸 뛰어서 온건지?도 필요
    # TERMINAL
    if num == N-1:
        return 0

    # MEMO
    if dp[num] != INF:
        return dp[num]
    
    # Call
    # num -> num+1, .. N
    for i in range(num+1, N):
        # 현재 num번째 문자를 key로 하는 다음 문자 == _data[i]
        if match[_data[num]] == _data[i]:
            dp[num] = min(dp[num], call_dp(i) + (i-num)**2)

    return dp[num]

ans = call_dp(0)
if ans == INF:
    print(-1)
else:
    print(ans)


# 완탐? => 
    # N이 1이상, 1000이하 
    # 각 자리에서 할 수 있는 점프 1, 2, 3.. 
    # 너무 많다,, / 
    # 시간복잡도 : 


# dp[N]
    # dp[i] : i번째칸에서 갈 수 있는 곳
        # => i+1 ~ N번칸
        # 그중, 최솟값? .. 
    # dp[]