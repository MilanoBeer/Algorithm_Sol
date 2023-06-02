# 1초 / 512MB
# 23.06.02 
# 14:12 ~ 14:42


# mat의 밝기 정보 
# -> 구역의 밝기의 평균 구하기

import sys
input = sys.stdin.readline

# 1이상, 1000이하 / Q : 1이상 10000이하 
R, C, Q = map(int, input().split())

mat = [[0] * (C+1) for _ in range(R+1)]
for r in range(1, R+1):
    mat[r][1:] = list(map(int, input().split()))
# mat = [list(map(int, input().split())) for _ in range(R)]
# total_mt = [[0] * C for _ in range(R)]

# SOL
# 합만 더하면?
    # 구간합으로 빼고, 영역의 넓이만 구해서 하면됨!

for i in range(1, R+1):
    for j in range(1, C+1):
        mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

# for i in range(R):
#     for j in range(C):
#         total_mt[i+1][j+1] = mat[i][j]


# for i in range(1, R+1):
#     for j in range(1, C+1):
#         total_mt[i][j] += total_mt[i-1][j] + total_mt[i][j-1] - total_mt[i][j]

# for line in mat:
#     print(*line)

# 평균 계산하기
# def cal_aver():
#     pass


for q in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    
    tmp = mat[x2][y2] - mat[x1-1][y2] - mat[x2][y1-1] + mat[x1-1][y1-1]
    size = (x2-x1 + 1) * (y2-y1 + 1)

    # OUTPUT
    print(tmp//size)
    
    

