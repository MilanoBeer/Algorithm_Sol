from collections import deque

# N x N , M마리의 물고기, 상어 1마리 
# 물고기 , 상어 : 크기를 가지고 있음
# 상어 ; 처음 크기 2 / 1초에 상하좌우 한칸씩 이동

# 조건
# 1. 지날 수 없는 칸 : 자기보다 큰!! 물고기 있는 칸
# 2. 나머지칸 : 모두 지날 수는 있음
# 3. 먹을 수 있는 물고기 : 자기보다 작은!! 물고기 
# 4. 자기랑 같은 크기 물고기 -> 먹을 수는 없음, 지날 수는 있음

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
mat = [ list(map(int,input().split())) for _ in range(N)]

shark_size = 2 # 상어크기 초기값 
fish_queue = deque() # 물고기들 위치
sh_r = 0
sh_c = 0

# 아기 상어 위치 파악 / 물고기 위치 파악 
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            sh_r = i
            sh_c = j 

        if mat[i][j] != 0 and mat[i][j] != 9:
            fish_queue.append([i, j])

def bfs(r, c):

    queue = deque()
    visited = [[-1] * N for _ in range(N)]
    visited[r][c] = 0
    queue.append([r, c])

    # print("r :", r, " c: ", c)

    while queue:
        cur_r, cur_c = queue.popleft()
        # print("cur_r :", cur_r, " cur_c: ", cur_c)

        # 상어위치인지 확인
        if cur_r == sh_r and cur_c == sh_c:
            return visited[cur_r][cur_c]

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 경계검사
            if 0 <= nr < N and 0 <= nc < N:
                # 상어자리이거나 or 상어크기보다 작은경우 and 
                if (mat[nr][nc] <= shark_size or mat[nr][nc] == 9) and visited[nr][nc]== -1 :
                    # print("append nr: ", nr, " nc: ", nc)
                    queue.append([nr, nc])
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
    return 100
    
min_distance = 21
min_r = -1
min_c = -1

eat_fish_cnt = 0
total_time = 0

if len(fish_queue) == 0:
    print(0)
    exit()

while True:
    for (i, j) in fish_queue:
        if mat[i][j] < shark_size and mat[i][j] != 0:
            distance = bfs(i, j)
            # print("distance: ", distance)
            # 최소거리가 같은 경우 > 행, 렬 비교 
            if distance == min_distance:
                # 가장 위, 가장 왼쪽 비교
                if i < min_r:
                    if j > min_c:
                        min_distance = distance
                        min_r = i
                        min_c = j

            if distance < min_distance:
                min_distance = distance
                min_r = i 
                min_c = j
    mat[min_r][min_c] = 0 # 물고기 먹기
    # 상어위치 업데이트
    sh_r = min_r 
    sh_c = min_c 

    total_time += min_distance
    min_distance = 21

    eat_fish_cnt += 1
    # print("min_r :", min_r, ", min_c : ", min_c)
    fish_queue.remove([min_r, min_c])

    # 상어크기 업데이트 
    if eat_fish_cnt == shark_size:
        shark_size += 1
        eat_fish_cnt = 0

    continue_flag = False
    for i, j in fish_queue:
        # 아직 먹을 수 있는 물고기가 존재한다면: 상어사이즈보다 작고, 0도 아님
        if (mat[i][j] < shark_size) and (mat[i][j] != 0):
            continue_flag = True
    
    if continue_flag == False:
        break
            

    # 시간 업데이트 

print(total_time)
