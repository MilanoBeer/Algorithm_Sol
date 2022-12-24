from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 최소일수 !
# 1 익은 토마토 / -1 토마토가 없는 칸

# 가로칸 M, 세로칸 N 
M, N = map(int, input().split())

# N개의 줄( 행 ) 
mat = [ list(map(int, input().split())) for _ in range(N)]


# 익은 토마토의 위치 찾기 : 익은 토마토가 각 자리에서 동시에 시작 
pos = []
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            pos.append([i, j])

queue = deque()
V = [[0] * M for _ in range(N)]
max_day = -1

ZERO_FLAG = True
for line in mat:
    if 0 in line:
        ZERO_FLAG = False
    
if ZERO_FLAG:
    print(0)
    exit()

def bfs():
    global max_day
    # pos의 모든 토마토 넣기 
    for i, j in pos:
        queue.append([i, j])
        V[i][j] = 1

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 경계검사 
            if 0 <= nr < N and 0 <= nc < M:
                if mat[nr][nc] == 0 and V[nr][nc] == False:
                    mat[nr][nc] = 1
                    queue.append([nr, nc])
                    V[nr][nc] = V[cur_r][cur_c] + 1
                    max_day = max(max_day, V[nr][nc])

bfs()
# 0인 토마토가 있는 지 검사 
FLAG = True
for i in mat:
    if 0 in i:
        FLAG = False
if FLAG:
    print(max_day-1)
else:
    print(-1)

