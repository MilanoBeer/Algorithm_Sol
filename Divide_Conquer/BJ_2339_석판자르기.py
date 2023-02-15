import sys
from typing import Tuple

VERT = 1
HORI = -1

ONE_JEW = 2
INCORR = 3
BAD = 4

N = int(sys.stdin.readline()) 

mat = [ list(map(int, input().split())) for _ in range(N)]

def get_board_status(fr, to):
    # 보드 내부 보석 수, 불순물 수 카운트해서 status판단
    jew_cnt = 0
    bad_cnt = 0

    for i in range(fr[0], to[0] + 1):
        for j in range(fr[1], to[1] + 1):
            if mat[i][j] == 2:
                jew_cnt += 1
            if mat[i][j] == 1:
                bad_cnt += 1
                return BAD
    if jew_cnt == 1:
        return ONE_JEW
    else:
        return INCORR
    
def is_available_cutting(fr, to, cur_pos, dir):
    if dir == HORI:
        for i in range(fr[1], to[1] + 1):
            if mat[cur_pos[0]][i] == 2:
                return False
        return True
    
    if dir == VERT:
        for i in range(fr[0], to[0] + 1):
            if mat[i][cur_pos[1]] == 2:
                return False
        return True
    
def count_case(fr, to, dir):
    # terminal condition 
    status = get_board_status(fr, to)
    if status == ONE_JEW:
        return 1
    if status == INCORR:
        return 0

    cur_pos = (fr[0], fr[1])
    num_case = 0
    # recursive
    for i in range(fr[0], to[0] + 1):
        for j in range(fr[1], to[1] + 1):
            if mat[i][j] == 1:
                cur_pos = (i, j)
                # # terminal condition : 더 이상 검사할 불순물이 없을 때 
                if is_available_cutting(fr, to, cur_pos, dir):
                    if dir == HORI:
                        # 위아래로 나눠서 호출 
                        up_area_bottom = i -1 
                        down_area_top =  i + 1
                        num_case += count_case(fr, (up_area_bottom, to[1]), VERT) * count_case((down_area_top, fr[1]), to, VERT)

                    else:
                        # 좌우 나눠서 호출 
                        left_area_col = j -1
                        right_area_col = j + 1
                        num_case += count_case(fr, (to[0], left_area_col), HORI) * count_case((fr[0], right_area_col), to, HORI)

    # 현재 영역의 num case 반환
    return num_case

result = count_case((0, 0), (N-1, N-1), HORI) + count_case((0, 0), (N-1, N-1), VERT)

if result == 0:
    print("-1")
else:
    print(result)