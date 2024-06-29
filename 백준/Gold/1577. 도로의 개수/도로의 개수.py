# 19:35~ 

N, M = map(int, input().split())
K = int(input())

dp = [[0] * (N+1) for _ in range(M+1)]
_not = []
for k in range(K):
    a, b, c, d = map(int, input().split())
    
    a, b = b, a
    c, d = d, c

    _not.append((a, b, c, d))
    _not.append((c, d, a, b))

# init
dp[0][0] = 1
# if (0, 0, 0, 1) not in _not:
#     dp[0][1:] = [1] * (N+1)
# if (0, 0, 1, 0) not in _not:
#     for i in range(M+1):
#         dp[i][0] = 1

# travel
for i in range(M+1):
    for j in range(N+1):
        if j > 0:
            if (i, j-1, i, j) not in _not:
                dp[i][j] += dp[i][j - 1]
            # else:
            #     dp[i][j] = 0
        if i > 0:
            if (i-1, j, i, j) not in _not:
                dp[i][j] += dp[i-1][j]
        
print(dp[M][N])