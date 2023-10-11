# 23.10.11 / 13:35 ~ 
import sys
def input():
    return sys.stdin.readline().rstrip()

ans = 0
N = int(input())
_data = list(map(int, input().split()))
# condition : 중간에 나오는 계산값들 모두 0이상 20이하여야

# init dp
dp = [[0] * 21 for _ in range(N)]
dp[0][_data[0]] += 1

for i in range(1, N-1):
    for j in range(21):
        # 상위 라인에서 경우의 수가 존재하면 : 값이 경우의 수 / j가 그 계산값
        if dp[i-1][j]:
            if j + _data[i] <= 20:
                dp[i][j + _data[i]] += dp[i-1][j]
            # ERROR *** : elif라고 해서......
            if 0 <= j - _data[i]:
                dp[i][j - _data[i]] += dp[i-1][j]
# for line in dp:
#     print(line)
print(dp[N-2][_data[N-1]])

# def call_dp(cnt, 0):
#     # terminal

#     # memoization


#     # backtracking


#     # call function
#     dp[cnt] = dp[]

# call_dp(1)

# output : 만들 수 있는 등식의 갯수
