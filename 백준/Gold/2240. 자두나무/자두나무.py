# 3차원 dp같긴한데..

# i초에 자두를 먹을 수 있는 조건
# - 이동횟수가 홀수 & 2번나무에서 자두 떨어질때
    # - 이번엔 먹는거 확실한데, 이전에 더 크게 먹었던 경우 + 1
# - 이동횟수가 짝수 & 1번나무에서 자두 떨어질때
    # - 이번에 먹는거 확실한데, 이전에 더 크게 먹었던 경우 + 1
    # - 이전에 먹은거 고려사항
        # - 

T, W = map(int, input().split())
_data = [0] + [int(input()) for _ in range(T)]

# dp init
dp = [[0] * (W+1) for _ in range(T+1)]
# 1초 
dp[1][0] = _data[1] % 2
dp[1][1] = _data[1] // 2

# traversal 
for i in range(2, T+1):
    for j in range(W+1):
        tmp = _data[i] % 2 if j%2 == 0 else _data[i]//2
        if tmp:
            dp[i][j] = max(dp[i-1][0:j+1]) + 1
        else:
            dp[i][j] = max(dp[i-1][0:j+1])
print(max(dp[T]))
