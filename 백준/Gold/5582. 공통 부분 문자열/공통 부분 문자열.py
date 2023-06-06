# 2초 / 256MB
# 23.06.06
# 15:53 ~ 

import sys
input = sys.stdin.readline

# 1이상, 4000이하 
A = list(input().strip())
B = list(input().strip())

# A문자열에서 1, 2, ... 4000 
    # 각 문자열 -> B에서 찾기 

# 빈 문자열도 포함 
_ans = []
a_size = len(A)
b_size = len(B)

dp = [[0] * (b_size) for _ in range(a_size)]
ans = 0 

for i in range(a_size):
    for j in range(b_size):
        if A[i] == B[j]:
            if i == 0 or j ==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)




