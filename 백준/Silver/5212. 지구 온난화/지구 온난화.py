# 1초 / 128MB

from collections import deque
import copy

# R x C 
# X : 땅 / . : 바다


# 인접 : 3칸 or 4칸 / 50년
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

mat = [list(input()) for _ in range(R)]
copy_mat = copy.deepcopy(mat)

# 섬 자리 찾기
que = deque()
for r in range(R):
    for c in range(C):
        if mat[r][c] == 'X':
            que.append((r, c))

# 조건 : X의 인접 자리에 바다도 카운트, 범위 벗어나도 카운트 
for r, c in que:
    cnt = 0

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < R and 0 <= nc < C:
            if mat[nr][nc] == '.':
                cnt += 1
        else:
            cnt += 1
    if cnt >= 3:
        copy_mat[r][c] = '.'
    
# for line in copy_mat:
#     print(*line)

# 출력 : 각 라인에 X가 있는지 검사..? 
# for line in copy_mat:
#     if 'X' not in line:
#         continue
#     else:
#         print(*line)

# 탐색하다가, X가 나오면, r, c 값을 max로 갱신해가기 
max_r, max_c = 0, 0
min_r, min_c = 11, 11

for r in range(R):
    for c in range(C):
        if copy_mat[r][c] == 'X':
            max_r = max(max_r, r)
            max_c = max(max_c, c)

            min_r = min(min_r, r)
            min_c = min(min_c, c)

for r in range(min_r, max_r+1):
    for c in range(min_c, max_c+1):
        print(copy_mat[r][c], end='')
    print()
