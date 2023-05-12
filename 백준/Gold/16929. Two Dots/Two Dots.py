# 2초 / 512MB : 메모리 제한 큼! 
# 2:25 ~ 3:10분 ! 

# Purpose > 같은 색으로 이루어진 사이클 찾기 

# DS / Algo
    # 2차원 맵 / DFS / 
    # DFS => Terminal Condtion : 시작점으로 돌아왔을 때! 

import sys
input = sys.stdin.readline

# 점 k개로 이루어진 사이클의 정의 # 4방 인접 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# N x M 게임판 / N, M 최대 50 
N, M = map(int, input().split())

# mat
mat = [list(input()) for _ in range(N)]

def dfs(s_r, s_c, r, c, cnt):
    # 4방향 
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # terminal condition 
        if cnt >= 4 and s_r == nr and s_c == nc:
            print("Yes")
            exit(0)

        # 경계검사
        if 0 <= nr < N and 0 <= nc < M:
            # 방문한적이 없으면서, 이전 알파벳이랑 같으면
            if visited[nr][nc] == 0 and mat[nr][nc] == mat[r][c]:
                visited[nr][nc] = 1
                dfs(s_r, s_c, nr, nc, cnt + 1)
                visited[nr][nc] = 0
                
# 각 점에 대해 dfs
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        #방문체크
        visited[i][j] = 1
        dfs(i, j, i, j, 1)
        visited[i][j] = 0

print("No")