# NxN 판
# 사탕의 색은 모두 같지 않을 수 있음
# 색이 다른 인접한 두 칸 고르기
    # 두 칸의 사탕 서로 교환함
# 모두 같은 색, 가장 긴 연속 부분(행 or 열) 고르고, 사탕 모두 먹기 

# 색 : 4가지 

# Purpose
    # 상근이가 먹을 수 있는 최대 사탕 갯수? 

N = int(input())
mat = [list(input()) for _ in range(N)]

# visited = [[False] * N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

find_candy_cnt = -1

def find_max_eat(r1, c1):
    global find_candy_cnt
    pivot = mat[r1][c1]

    # 위     
    tmp_cnt = 1
    for i in range(r1-1, -1, -1): # 현재 지점으로부터 위 
        if mat[i][c1] != pivot:
            break 
        tmp_cnt += 1

    # 현 지점으로부터 아래 
    for i in range(r1+1, N):
        if mat[i][c1] != pivot:
            break 
        tmp_cnt += 1
    find_candy_cnt = max(find_candy_cnt, tmp_cnt)


    tmp_cnt = 1 # 초기화 
    # 좌
    for i in range(c1-1, -1, -1):
        if mat[r1][i] != pivot:
            break 
        tmp_cnt +=1 
        
    # 우
    for i in range(c1+1, N):
        if mat[r1][i] != pivot:
            break 
        tmp_cnt += 1
    find_candy_cnt = max(find_candy_cnt, tmp_cnt)

    return find_candy_cnt

# 바꾸지 않았을 때 상태로 최댓값 init 
for i in range(N):
    for j in range(N):
        find_candy_cnt = max(find_candy_cnt, find_max_eat(i, j))

for i in range(N):
    for j in range(N):
        pivot = mat[i][j]
        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]

            # 경계검사 # pivot과 다른지 확인
            if 0 <= nr < N and 0 <= nc < N and pivot != mat[nr][nc]:
                    # 값 바꾸기 
                    mat[i][j], mat[nr][nc] = mat[nr][nc], mat[i][j]
                    # 바꾼 후, 한번에 먹을 수 있는 칸 확인

                    # 바꾼 값 주위만 확인
                    find_candy_cnt = max(find_candy_cnt, find_max_eat(i, j))
                    find_candy_cnt = max(find_candy_cnt, find_max_eat(nr, nc))

                    # 다시 값 바꿔주기 
                    mat[i][j], mat[nr][nc] = mat[nr][nc], mat[i][j]

print(find_candy_cnt)
            
