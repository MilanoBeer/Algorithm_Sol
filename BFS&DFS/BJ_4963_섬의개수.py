from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(8):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 경계 검사
            if 0 <= nr < H and 0 <= nc < W:
                if mat[nr][nc] == 1 and visited[nr][nc] == False:
                    queue.append([nr, nc])
                    visited[nr][nc] = True


while(True):
    W, H = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    # 0, 0 확인
    if W == 0 and H == 0:
        break

    mat = [ list(map(int, input().split())) for _ in range(H)]
    land_cnt = 0
    for i in range(H):
        for j in range(W):
            if mat[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                land_cnt += 1

    print(land_cnt)
    
