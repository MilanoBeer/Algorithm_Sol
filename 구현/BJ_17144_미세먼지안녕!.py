

# input
# R, C, T 
# 공기청정기 위치 : -1 , 2줄 
# 다른 위치 : 미세먼지 양 수치로 표시 

# 확산 > 
# TO DO : 예외처리 
# 확산 양 : /5, 소수점은 버리기 
# 해당 칸에 남은!양 > 
# ex > 확산방향 : 4 
# 46 - ( 46/5 = 9 ) * 4 => 36 

# 공기청정기 >
# 나오느 바람 > 
# 윗칸 > 반시계방향
# 아랫칸 > 시계방향
# 바람의 방향대로 한칸씩 이동함

# 4방향 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, T = map(int, input().split()) # T초 후 , 방의 미세먼지 총 양 출력

mat = [ list(map(int, input().split())) for _ in range(R)]
UP = 1
DOWN = -1

# Def > 미세먼지 확산 1회 / 전체가 한 번에 
def spread():
    # copy mat > 확산된 값만 여기서 개별 축적 
    copy_mat = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            # if > 미세먼지라면
            if mat[r][c] > 0:
                # 4방향 검사
                spread_cnt = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    # 경계검사
                    if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] != -1:
                        copy_mat[nr][nc] += mat[r][c]//5 
                        spread_cnt += 1
                # 남은 양 계산
                mat[r][c] -= (mat[r][c]//5 * spread_cnt)
    # 퍼뜨렸던 copy_mat의 값 합치기
    for r in range(R):
        for c in range(C):
            mat[r][c] += copy_mat[r][c]

def left_to_right(pos):
    # col을 이동 / 시작col인 0은 제외 
    for c in range(1, C-1): # C-1 : 7 
        if mat[pos[0]][c] != 0:
            copy_mat[pos[0]][c+1] = mat[pos[0]][c]

def bottom_to_up(pos, DIR): 
    start = 0 
    end = 0
    col = 0

    if DIR == UP:
        start = pos[0]
        end = 0
        col = C-1
    else:
        start =  R-1
        end = pos[0]
        col = 0

    for r in range(start, end, -1):
        if mat[r][col] != 0:
            copy_mat[r-1][col] = mat[r][col]
        
def right_to_left(pos, DIR):
    start = 0 
    end = 0
    col = 0

    if DIR == UP:
        start = C-1
        end = 0
        row = 0
    else:
        start =  C-1
        end = 0
        row = R-1

    for c in range(start, end, -1):
        if mat[row][c] != 0:
            copy_mat[row][c-1] = mat[row][c]     

def up_to_bottom(pos, DIR):
    start = 0 
    end = 0
    col = 0

    if DIR == UP:
        start = 0
        end = pos[0]
        col = 0
    else:
        start =  pos[0]
        end = R-1
        col = C-1

    for r in range(start, end):
        if mat[r][col] != 0:
            copy_mat[r+1][col] = mat[r][col]    

# Def > 공기청정 1회 / 위 아래칸 방향대로 
def clean():
    global up_air
    global down_air
    
    # 상단부 작동하기 > 반시계방향 / -> , 위로, <-, 아래로 
    left_to_right(up_air)
    bottom_to_up(up_air, UP)
    right_to_left(up_air, UP)
    up_to_bottom(up_air, UP)

    # 하단부 작동하기 > 시계방향
    left_to_right(down_air)
    up_to_bottom(down_air, DOWN)
    right_to_left(down_air, DOWN)
    bottom_to_up(down_air, DOWN)

    # copy_mat을 mat으로 복사 
    # copy up, down row> 
    mat[0] = [0] * C
    mat[R-1] = [0] * C
    for i in range(C):
        if copy_mat[0][i] != 0:
            mat[0][i] = copy_mat[0][i]
        if copy_mat[R-1][i] != 0:
            mat[R-1][i] = copy_mat[R-1][i]
    
    # init
    for i in range(1, R-1):
        mat[i][0] = 0
        mat[i][C-1] = 0

    for i in range(1, R-1):
        if copy_mat[i][0] != 0:
            mat[i][0] = copy_mat[i][0]
        if copy_mat[i][C-1] != 0:
            mat[i][C-1] = copy_mat[i][C-1]   

    for i in range(1, C-1):
        mat[up_air[0]][i] = 0
        mat[down_air[0]][i] = 0

    for i in range(1, C-1):
        if copy_mat[up_air[0]][i] != 0:
            mat[up_air[0]][i] = copy_mat[up_air[0]][i] 
        if copy_mat[down_air[0]][i] != 0:
            mat[down_air[0]][i] = copy_mat[down_air[0]][i] 
    mat[up_air[0]][0] = -1
    mat[down_air[0]][0] = -1

# TO DO : 공기 청정기 위치 파악하기 / *** 항상 1번 열, 위아래 두칸 차지 ***
up_air =[0, 0]
down_air = [0, 0]
for r in range(R):
    if mat[r][0] == -1:
        up_air[0] = r
        down_air[0] = r+1
        break 

def sum_mat():
    answer = 0
    for i in range(R):
        for j in range(C):
            answer += mat[i][j]
    return answer

copy_mat = [[0] * C for _ in range(R)]
answer = 0
for t in range(T):
    spread() # 미세먼지 확산 1회 
    clean() # 공기 청정 1회 
    # 1회 먼지 퍼지기 & 공기청정 후 
    copy_mat = [[0] * C for _ in range(R)]

answer = sum_mat() + 2
print(answer)
# 미세먼지 양 출력




