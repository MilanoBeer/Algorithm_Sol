# ***** 풀기 전 문제 이해하면서 메모한 부분 *****
# 비바라기 마법 : 하늘에 비구름 만들 수 있음
# N x N 
# 각 칸 -> 바구니 / 바구니에 저장할 수 있는 물의 양에는 제한 x
# A[r][c] : (r, c)에 저장되어있는 물의 양

# 1번 행 - N번 행을 연결
# 1번 열 - N번 열을 연결

# 구름 만들기
# 구름 이동을 M번 명령함
    # 이동 : 방향 d_i / 거리 s_i
    # 방향은 8개, 8개의 정수 

# 구름의 이동 #
# 1. 모든 구름이 di, si로 구이동
# 2. 각 구름에서 비 -> 각 칸의 바구니 물의 양 + 1
# 3. 구름이 모두 사라짐

# 4. 2단계에서 물이 증가한 칸에, 마법
    # 해당 칸에서, 대각선 방향으로, 거리가 1인 칸에 물이 있는 바구니의 수만큼, 
    # (r, c)에 있는 바구니의 물의 양이 증가한다 

# 5. 바구니에 저장된 물의 양이 2 이상이 모든 칸에 구름이 생김
    # 물의 양은 2가 줄어듬. 
    # 이때 구름이 생기는 칸은, 3에서 굴므이 사라진 칸은 아니영야 한다.. 

# input
# N,M
# map info ( N x N ) 
# M개의 줄, 이동정보

# ***** 구름의 존재랑 각 칸의 물의 양은 다르게 봐야.. *****
from collections import deque
import sys
input = sys.stdin.readline

# 이동 순서 # 좌 / 좌상 / 상 / 우상 / 우 / 우하 / 하 / 좌하 
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split()) # tc > 5, 4 
mat = [list(map(int, input().split())) for _ in range(N)]

# Def> 모든 구름이! dir방향으로 dist만큼 이동하기 
# ****** 연결성 적용 ***** 

visited = [[0]*N for _ in range(N)]
def move_cloud(dir, dist, cloud_queue):
    global visited

    new_cloud_queue = []

    for cloud in cloud_queue:
        
        move_r = (cloud[0] + dr[dir]*dist) % N
        move_c = (cloud[1] + dc[dir]*dist) % N

        # 여기서 바로 옮겨진 구름 위치들에, 물의 양 추가
        mat[move_r][move_c] += 1
        visited[move_r][move_c] = 1

        new_cloud_queue.append([move_r, move_c])
    
    return new_cloud_queue

# 구름이 있던 칸들에 대해, 대각선 방향으로 검사한 후, 빗물 양 추가하기 
def check_adjust_dir(new_cloud_queue):
    for cloud in new_cloud_queue:
        # dir 대각선 번호 : 2, 4, 6, 8
        r, c = cloud
        rain_cnt = 0
        for d in range(2, 9, 2):
            nr = r + dr[d]
            nc = c + dc[d]
            # 경계검사 
            if 0 <= nr < N and 0 <= nc < N:
                # 빗물이 있는지 검사
                if mat[nr][nc] >= 1:
                    rain_cnt += 1
        # 대각선에 물 있는 바구니 갯수만큼 +  
        mat[r][c] += rain_cnt 

# Def > 구름이 있던 칸들을 제외하고, 전체 mat에 대해, 물 2이상인 칸에 대해 구름 생성 /물의 양은 -2
def make_cloud_and_minus_rain(new_cloud_queue):

    global visited
    new_cloud_queue = []
    for i in range(N):
        for j in range(N):
            # 구름이 있던 칸이 아니라면 # not in을 쓰지말고, 방문체크배열이 시간을 줄여준다! 
            if visited[i][j] == 0 and mat[i][j] >= 2:
                mat[i][j] -= 2
                new_cloud_queue.append([i, j])
    return new_cloud_queue

def sum_total_rain():
    answer = 0
    for i in range(N):
        answer += sum(mat[i])
    return answer

# 비구름 만들기
cloud_queue = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

# M번의 명령 처리
for m in range(M):
    dir, dist = map(int, input().split())

    # 구름들이 이동한 후, 해당 칸에 비 내리기 
    new_cloud_queue = move_cloud(dir, dist, cloud_queue) # & rain! 

    # 구름이 있던 칸들에 대해, 대각선 방향으로 검사한 후, 빗물 양 추가하기 
    check_adjust_dir(new_cloud_queue)

    # 구름이 있던 칸들을 제외하고, 전체 mat에 대해, 물 2이상인 칸에 대해 구름 생성 / 물의 양은 -2
    new_cloud_queue = make_cloud_and_minus_rain(new_cloud_queue)

    cloud_queue = new_cloud_queue
    visited = [[0]*N for _ in range(N)] # 구름 옮길 거니까, 거기서 다시 갱신! 

# 모든 이동이 끝난 후, 전체에서 빗물 양 합 구하기
print(sum_total_rain())