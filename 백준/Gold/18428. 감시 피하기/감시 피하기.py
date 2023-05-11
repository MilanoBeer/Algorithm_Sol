# 2초 / 256MB
# 18: 18~ 20:35 ~ 
import copy
import sys
input = sys.stdin.readline

from itertools import combinations

# 4방향 감시 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 장애물 뒤편 학생 볼 수 X
# T, S, O(장애물)

# 장애물 설치 위치 -> 3개 고르기
    # 모든 학생 감시 피할 ㅅ 있는지
# input
N = int(input()) # 3이상, 6이하 
mat = [list(input().split()) for _ in range(N)]

# Solution 
# 빈칸 자리 리스트에 담기
empty_l = []
teacher_l = []
for r in range(N):
    for c in range(N):
        if mat[r][c] == 'X':
            empty_l.append([r, c])
        if mat[r][c] == 'T':
            teacher_l.append([r, c])

# 설치한 장애물들 경우 확인하기
def check(case, copy_mat):
    # 해당 장애물 위치에 설치하기
    for r, c in case:
        copy_mat[r][c] = 'O'
    
    # 감시 피할 수 있는지 확인하기
    # 모든 선생님에 대해
    for tr, tc in teacher_l:
        # 선생님위치기준으로 4방 모두 경계선 or 장애물 만날떄까지 go 
        for d in range(4):
            idx = 1
            while True:
                nr = tr + dr[d]*idx
                nc = tc + dc[d]*idx

                if 0 <= nr < N and 0 <= nc < N:
                    if copy_mat[nr][nc] == 'O':
                        break  # 멈추고 다른 방향 검사 
                    # 학생이면 False
                    if copy_mat[nr][nc] == 'S':
                        return False
                    idx += 1
                else:
                    break 
        # 학생 발견하면, return Fale
        # 감시 모두 피했다는 의미
        # return True
    return True

# 3개 조합으로 뽑기
flag = False
for case in combinations(empty_l, 3):
    # 각 case에 대해서, 모든 학생이 피할 수 있는지 확인
    copy_mat = copy.deepcopy(mat)
    if check(case, copy_mat):
        # 모두 피할 수 있는 경우가 있으면, -> flag, 바로 break 
        flag = True
        break 
# 끝날때까지 불가능
if flag == True:
    print("YES")
else:
    # NO출력 
    print("NO")

# output
# 감시 피할 수 있으면 -> YES  / NO
