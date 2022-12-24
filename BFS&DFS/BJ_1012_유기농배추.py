from collections import deque 


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
queue = deque()

def bfs(r, c):
    V[r][c] = False
    queue.append([r, c])

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 경계검사 
            if 0 <= nr < M and 0 <= nc < N:
                if mat[nr][nc] == 1 and V[nr][nc] == False:
                    queue.append([nr, nc])
                    V[nr][nc] = True

for t in range(T):
    # 가로 M, 세로 N, 배추심어진위치의 갯수 K  
    cnt = 0
    M, N, K = map(int, input().split())
    V = [[False] * N for _ in range(M)] 


    mat = [[0] * N for _ in range(M)]
    # 배추의 위치정보 X, Y
    for k in range(K):
        X, Y = map(int, input().split())
        mat[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1 and V[i][j] == False:
                bfs(i, j)
                cnt+= 1
    
    print(cnt)


