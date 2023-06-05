# 1초 / 512<B

from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

# 특정위치에, 바이러스 M개 설치 
# NxN / 빈칸, 벽
# 한번 4방으로 퍼지는데 걸리는 시간 1초 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# Condition 
    # '2'자리 : 바이러스를 놓을 수 있는 칸 
    # 바이러스는 빈칸으로만 복제 가능 

# Output : 모든 빈칸에 바이러스를 퍼뜨리는 최소 시간 구하기 
    # 어떻게 해도 모든 칸엔 x -> -1 출력 

# N : 5이상, 50이하 / M : 10이하 
N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

# DS: 4방으로 동시에 / BFS, queue

# 2인자리 찾기
_two_list =[]
for i in range(N):
    for j in range(N):
        if mat[i][j] == 2:
            _two_list.append((i, j))

def bfs(copy_mat, case, visited):
    last_time = 0

    # init queue : 바이러스 위치들 추가 
    queue = deque()
    for r, c in case:
        queue.append((r, c))
        copy_mat[r][c] = 3

    # 퍼트리기 
    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            # 경계 검사
            if 0 <= nr < N and 0 <= nc < N:
                # 빈칸이면
                if copy_mat[nr][nc] == 0 or copy_mat[nr][nc] == 2:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[cr][cc] + 1 # 시간 재기 
                        queue.append((nr, nc)) # 추가 
                        copy_mat[nr][nc] = 3

    # visited 의 max가 마지막으로 도착한 값
    # last_time = max(max(visited))
    for line in visited:
        last_time = max(last_time, max(line))
    return last_time

# Solution 
min_time = 9999999
# 원소2인 모든 자리에서, M 개를 고르는 경우 
for case in combinations(_two_list, M):
    # 고르고, 그 자리에서 바이러스 퍼트리기
    visited = [[0] * (N) for _ in range(N)]
    copy_mat = copy.deepcopy(mat)
    last_time = bfs(copy_mat, case, visited)

    # 다 퍼트리고 나서, 남은 빈칸 있는지 확인
    zero_cnt = 0
    for line in copy_mat:
        zero_cnt += line.count(0)
    # 남은 빈칸이 없으면, 최소시간 갱신하기
    if zero_cnt == 0:
        min_time = min(min_time, last_time)
        
# 모든 경우 확인했는데, 최소시간값이 여전히 초기값이면 -> 어떻게 해도 못채워지는 케이스 
if min_time == 9999999:
    print("-1")
else:
    print(min_time)
    