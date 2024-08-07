N = int(input())


# init
mat = list(map(int, input().split()))
min_dp = mat[::]
max_dp = mat[::]

for i in range(1, N):
    tmp = list(map(int, input().split()))

    min_dp = [tmp[0] + min(min_dp[0], min_dp[1]), 
              tmp[1] + min(min_dp), 
              tmp[2] + min(min_dp[1], min_dp[2])]
    max_dp = [tmp[0] + max(max_dp[0], max_dp[1]), 
              tmp[1] + max(max_dp), 
              tmp[2] + max(max_dp[1], max_dp[2])]
print(max(max_dp), min(min_dp))

# ERROR
    # - 2차원 min_dp, max_dp 메모리 초과 
# Sol
    # 슬라이딩 윈도우,,, 구글링 
