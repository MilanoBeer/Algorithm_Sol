# 1초 / 512MB
# 23.05.22
# 19:20 ~ 20:00 / 출력초과 (나머지계산처리안함)
# 시간초과 

# 제한 : 두번이상 연속사용은 X
    # 1개 이상은 사용해야함
import sys
input = sys.stdin.readline

T = int(input())

dp = [[0] * (100001) for _ in range(4)]

dp[1][1], dp[2][2] = 1, 1
dp[1][3], dp[2][3], dp[3][3] = 1, 1, 1

# traversal 
for i in range(4, 100001):
    dp[1][i] = (dp[2][i-1] + dp[3][i-1]) % 1000000009
    dp[2][i] = (dp[1][i-2] + dp[3][i-2]) % 1000000009
    dp[3][i] = (dp[1][i-3] + dp[2][i-3]) % 1000000009

for t in range(T):
    n = int(input()) # 양수, 10만 이하
    # n을 1,2,3합으로 나타내는 방법의 수 

    # 확인
    print((dp[1][n] + dp[2][n] + dp[3][n]) % 1000000009)