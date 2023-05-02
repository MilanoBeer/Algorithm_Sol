'''
23.05.02 
16:00 ~ 17:30 / 
'''
# 1초 / 256MB 

# 문제파악
# 2n개 -> 2행 n열 
# 스티커 떼면 -> 4방도 못 씀
# 목적
    # 스티커의 점수 합이 최대가 되도록 스티커 떼기 
    # => 최대가되면서, 서로 변을 공유하지 않는 스티커의 집합 구하기 
import sys
input = sys.stdin.readline

T = int(input()) #
for t in range(T):
    n = int(input()) # 1이상, 10만 이하 
    # 두 줄, n개의 정수 : 각 점수 -> 0이상 100이하 
    dp = [list(map(int, input().split())) for _ in range(2)]

    # Solution 
    # DP배열 : 2차원
    if n == 1 :
        print(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for i in range(2, n):
            dp[0][i] += max(dp[1][i-2], dp[1][i-1])
            dp[1][i] += max(dp[0][i-2], dp[0][i-1])
        # output : 최대 점수 
        print(max(dp[0][n-1], dp[1][n-1]))