import sys
input = sys.stdin.readline

# 크기 N / 합을 구해야하는 횟수 M 
N, M = map(int, input().split())

# input data
mat = [ list(map(int, input().split())) for _ in range(N)]
mat_sum = [[0] * (N+1) for _ in range(N+1)]

# Do > (1, 1)부터 각 칸까지의 합을 구하기 
    # (1,1)부터 mat[0][0]값으로 채워지면서 시작
    # 따로 mat_sum을 초기화할 필요는 없음
for i in range(1, N+1):
    for j in range(1, N+1):
        mat_sum[i][j] = mat_sum[i-1][j] + mat_sum[i][j-1] - mat_sum[i-1][j-1] + mat[i-1][j-1]

# # M개의 명령
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = mat_sum[x2][y2] - mat_sum[x1-1][y2] - mat_sum[x2][y1-1] + mat_sum[x1-1][y1-1]
    print(res)

