# 16:56 ~ 

N, M, x, y, K = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 정보
dice = [0, 0, 0, 0, 0, 0]

# direction : # 동, 서, 북, 남
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def move_dice(com):
    global dice 
    
    # 현재 주사위 정보 copy
    one, two, three, four, five, six = dice

    if com == 1: # 동
        dice = [four, two, one, six, five, three]
    elif com == 2: # 서 
        dice = [three, two, six, one, five, four]
    elif com == 3: # 북
        dice = [five, one, three, four, six, two]
    elif com == 4: # 남
        dice = [two, six, three, four, one, five]

# 명령 수행
for c in commands:
    nr, nc = x + dr[c], y + dc[c]

    # 경계검사
    if 0 <= nr < N and 0 <= nc < M:
        # def > 주사위 굴리기
        move_dice(c)

        # mat 판별
        if mat[nr][nc] == 0:
            mat[nr][nc] = dice[-1]
        else:
            dice[-1] = mat[nr][nc]
            mat[nr][nc] = 0

        # ***** 위치갱신 *****
        x, y = nr, nc
    # output : 이동 후, 주사위 상단에 쓰인 값 
        print(dice[0])

