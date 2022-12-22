
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())

mat = [ list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
cnt = 0
queue = deque()

def bfs():
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()

        # 도착지 검사
        if r == N-1 and c == M-1:
            break; 

        # 4방 검사
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0<= nc < M:
                # 갈 수 있는지 & 방문검사
                if mat[nr][nc] ==1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1 
                    queue.append([nr, nc])
        
bfs()
print(visited[N-1][M-1])



