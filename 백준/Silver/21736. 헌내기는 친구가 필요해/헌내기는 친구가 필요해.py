from collections import deque

N, M = map(int, input().split())
mat = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
# exception -> TT 

# I 도연이에서 시작
I = ()
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'I':
            I = (i, j)
            break 

def bfs():
    global ans 

    dq = deque()
    dq.append((I[0], I[1]))
    visited = [[0] * M for _ in range(N)]
    visited[I[0]][I[1]] = 1

    while dq:
        cr, cc = dq.popleft()

        for d in range(4):
            # 영역, 방문검사
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if mat[nr][nc] == 'O':
                    dq.append((nr, nc))
                elif mat[nr][nc] == 'P':
                    ans += 1
                    dq.append((nr, nc))
                visited[nr][nc] = 1

bfs()
if ans == 0:
    print("TT")
else:
    print(ans)
