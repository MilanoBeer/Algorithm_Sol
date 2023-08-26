# 23.08.26 / 23:10 ~ 
# 그래프상의 정점간에 이동하는데, 간선비용이 양수이다 
# 모든 정점간의 관계값을 구해서, 그 비용들 중 최솟값을 구하기 
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
INF = sys.maxsize
# 버스정보 -> matrix
mat = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, p = map(int, input().split())
    mat[a][b] = min(mat[a][b], p)

# init dist matrix

dist = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            continue
        if mat[i][j] != 0:
            dist[i][j] = mat[i][j] 

# print("** 초기 dist **")
# for line in dist:
#     print(*line)
# print()

# Process
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] != 0 and dist[k][j] != 0:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end = " ")
        else:
            print(dist[i][j], end = " ")
    print()