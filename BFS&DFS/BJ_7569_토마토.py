from collections import deque

dh = [0, 0, 0, 0, 1, -1] # 상, 하, 좌, 우, 위, 아래
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]


# h, r, c 
M, N, H = map(int, input().split()) # 가로, 세로, 높이

# 3차원 배열 선언하는 법 !!!! 
mat = [[ list(map(int, input().split())) for _ in range(N) ] for _ in range(H) ]

# 익지 않은 토마토가 처음부터 없는지 먼저 검사 
ZERO_EXIST = False
for board in mat:
    for line in board:
        if 0 in line:
            ZERO_EXIST = True
            break 
if ZERO_EXIST is False:
    print("0")
    exit()



pos = []
# 토마토 pos 찾기
for h in range(H):
    for n in range(N):
        for m in range(M):
            if mat[h][n][m] == 1:
                pos.append([h, n, m])

visited = [[ [0] * (M) for _ in range(N) ] for _ in range(H) ]
max_day = 0
def bfs():
    global max_day
    queue = deque()

    # pos의 모든 위치정보 queue에 넣기
    for h, n, m in pos:
        queue.append([h, n, m])
        visited[h][n][m] = 1

    while queue:
        h, n, m = queue.popleft()

        for i in range(6):
            nh = h + dh[i]
            nn = n + dr[i]
            nm = m + dc[i]

            # 경계 검사 
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if mat[nh][nn][nm] == 0 and visited[nh][nn][nm] == 0:
                    mat[nh][nn][nm] = 1
                    queue.append([nh, nn, nm])
                    visited[nh][nn][nm] = visited[h][n][m] + 1
                    max_day = visited[nh][nn][nm]
        
bfs()
# 남은 토마토 있는지 검사
ZERO_EXIST = False
for board in mat:
    for line in board:
        if 0 in line:
            ZERO_EXIST = True
            break 

if ZERO_EXIST:
    print(-1)
else:
    print(max_day-1)




    


