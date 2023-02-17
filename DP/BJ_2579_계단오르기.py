# input data 
n = int(input()) # 계단의 갯수 
stair_list = []
for i in range(n):
    stair_list.append(int(input()))

D = [[0] * n for _ in range(4)] # 4행 n열

D[0][0] = stair_list[0]
D[1][0] = stair_list[0]
D[2][0] = 0
D[3][0] = 0

for i in range(1, n):
    D[0][i] = D[1][i-1] + stair_list[i]
    D[1][i] = max(D[2][i-1] + stair_list[i], D[3][i-1] + stair_list[i])
    D[2][i] = D[0][i-1]
    D[3][i] = D[1][i-1]

print(max(D[0][n-1], D[1][n-1]))