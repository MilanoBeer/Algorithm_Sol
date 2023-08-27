# 23.08.27 / 14:00 ~ 
import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

mat = [[0] * (N+1) for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    mat[a][b] = 1 # 단방향임

INF = sys.maxsize
dist = [[0] * (N+1) for _ in range(N+1)]

# init dist
for i in range(1, N+1):
    for j in range(1, N+1):
        dist[i][j] = mat[i][j] 

# Proccess
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][k] != 0 and dist[k][j] != 0:
                dist[i][j] = 1
ans = 0
for v in range(1, N+1):
    # row
    row_tot = sum(dist[v])
    # col
    for i in range(1, N+1):
        row_tot += dist[i][v]
    
    if row_tot == N - 1:
        ans += 1

print(ans)