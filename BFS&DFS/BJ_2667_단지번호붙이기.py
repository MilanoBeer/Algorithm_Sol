from collections import deque

# 1 : 집 있는 곳

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())

mat = [ list(map(int, input())) for _ in range(N)]
queue = deque()
V = [[False] * N for _ in range(N)]
total = 1
each_area = 0

def bfs(r, c):
    global each_area
    each_area += 1
    queue.append([r, c])
    mat[r][c]= total
    V[r][c] = True

    while queue:
        curR, curC = queue.popleft()

        for i in range(4):
            nr = curR + dr[i]
            nc = curC + dc[i]

            # 경계검사
            if 0 <= nr < N and 0 <= nc < N:
                if V[nr][nc] == False and mat[nr][nc] == 1:
                    mat[nr][nc] = total 
                    V[nr][nc] = True
                    each_area += 1
                    queue.append([nr, nc])



each_list = []
for i in range(N):
    for j in range(N):
        if V[i][j] == False and mat[i][j] == 1:
            each_area =0
            bfs(i, j)
            each_list.append(each_area)
            total += 1  


print(total-1)
each_list.sort()
for i in each_list:
    print(i)

