# 1초 / 256MB
# 23.05.09
# 10:00 ~ 

# N, M 미로 
# 각 방 <- 사탕
# (1, 1)기준, 시작점 / 목표는 N, M 
# 이동 : 하, 오, 오른쪽 아래 
# 목적 : N,M으로 이동하면서 가져올 수 있는 사탕의 최대갯수 

from collections import deque
import sys
input = sys.stdin.readline

# 1이상, 1000이하 
N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

# 3방향
dr = [1, 0, 1]
dc = [0, 1, 1]

max_val = 0
visited = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        visited[r][c] = mat[r][c]

def check(r, c):
    # 3방향
    for d in range(3):
        nr = r + dr[d]
        nc = c + dc[d]
        # 경계검사 
        if 0 <= nr < N and 0 <= nc < M:
            visited[nr][nc] = max(visited[nr][nc], visited[r][c] + mat[nr][nc])
        # max갱신 

# 배열 순회
    # 각각 3방향, max값 갱신
for r in range(N):
    for c in range(M):
        check(r, c)

print(visited[N-1][M-1])