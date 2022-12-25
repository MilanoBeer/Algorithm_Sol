from collections import deque

N = int(input())

mat = [ list(map(int, input().split())) for _ in range(N) ]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * (N) for _ in range(N)]
queue = deque()

max_num = -1
min_num = 101
max_cnt = 0

def water(height):
    global visited

    for i in range(N):
        for j in range(N):
            if mat[i][j] <= height:
                visited[i][j] = True 

def bfs(r, c):
    visited[r][c] = False
    queue.append([r, c])

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0<= nc < N:
                if visited[nr][nc] == False:
                    queue.append([nr, nc])
                    visited[nr][nc] = True

def main():
    global visited
    # global max_num
    # global min_num
    max_num = -1
    min_num = 101
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            max_num = max(max_num, mat[i][j])
            min_num = min(min_num, mat[i][j])

    for height in range(min_num, max_num+1):
        visited = [[False] * (N) for _ in range(N)]
        water(height)

        cnt = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False: 
                    bfs(i, j)
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

    if max_cnt == 0:
        print(1)
    else:
        print(max_cnt)


main()