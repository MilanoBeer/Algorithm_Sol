from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    while swan_q:
        x, y = swan_q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if mat[nx][ny] == '.':
                        swan_q.append([nx, ny])
                    else:
                        swan_tmp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while water_q:
        x, y = water_q.popleft()
        if mat[x][y] == 'X':
            mat[x][y] = '.'
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not water_c[nx][ny]:
                    if mat[nx][ny] == 'X':
                        water_q_temp.append([nx, ny])
                    else:
                        water_q.append([nx, ny])
                    water_c[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
water_c = [[0]*n for _ in range(m)]

mat, swan = [], []
swan_q, swan_tmp, water_q, water_q_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    mat.append(row)
    for j, k in enumerate(row):
        if mat[i][j] == 'L':
            swan.extend([i, j])
            water_q.append([i, j])
        elif mat[i][j] == '.':
            water_c[i][j] = 1
            water_q.append([i, j])

# print("** mat **")
# for line in mat:
#     print(line)

# print("** water_c ** ")
# for line in water_c:
#     print(line)

# print("** water_q ** : 물의 위치정보들 저장")
# for line in water_q:
#     print(line)

x1, y1, x2, y2 = swan
swan_q.append([x1, y1])
mat[x1][y1], mat[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    # 녹이기 
    melt()
    # 만날 수 있는지 확인 
    if bfs():
        print(cnt)
        break
    # 영역 갱신 
    swan_q, water_q = swan_tmp, water_q_temp
    swan_tmp, water_q_temp = deque(), deque()
    cnt += 1