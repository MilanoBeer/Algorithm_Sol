# 2초 / 128MB
import sys
input = sys.stdin.readline

from collections import deque
# 게임조건
# 가로 == 세로칸수 같은 영역 
# 출발 : (0, 0)
# 오른쪽, 아래
dr = [0, 1]
dc = [1, 0]
# 이동가능: 현재 칸의 value

# TERMINAL CONDITION: (마지막, 마지막)

# OUTPUT: 도달 가능 여부 출력

N = int(input()) # 2이상, 64이하 

mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
flag = False
def bfs(r, c):
    global flag
    # init 
    queue = deque()
    queue.append((r, c)) 
    visited[r][c] = 1 # visited

    while queue:
        cr, cc = queue.popleft() 

        # TERMINAL
        if cr == N-1 and cc == N-1:
            flag = True
            print("HaruHaru")
            break
        
        for d in range(2):
            nr = cr + dr[d] * mat[cr][cc]
            nc = cc + dc[d] * mat[cr][cc]

            # 경계,방문
            if nr < N and nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1 # 방문
                queue.append((nr, nc))
                
bfs(0, 0) # 시작 
if not flag:
    print("Hing")