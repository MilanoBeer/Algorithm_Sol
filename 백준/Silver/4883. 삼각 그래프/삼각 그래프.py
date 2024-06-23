import sys

k = 0
while True: 
    k += 1
    N = int(input())
    if N == 0:
        break 
    mat = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * 3 for _ in range(N)] # *** ERROR 

    dp[0][0]= mat[0][0]
    dp[0][1] = mat[0][1]
    dp[0][2] = mat[0][1] + mat[0][2]

    dp[1][0] = mat[0][1] + mat[1][0]
    dp[1][1] = min(dp[1][0], dp[0][1], dp[0][2]) + mat[1][1]
    dp[1][2] = min(dp[1][1], dp[0][1], dp[0][2]) + mat[1][2]

    for i in range(2, N):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + mat[i][j] 
            elif j == 1:
                dp[i][j] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][j-1]) + mat[i][j]
            else:
                dp[i][j] = min(dp[i-1][1], dp[i-1][2], dp[i][j-1]) + mat[i][j]
    # for lst in dp:
    #     print(lst)
    # print()
    print(f'{k}. {dp[N-1][1]}')
