# 교실 하나 , NxN크기의 격자 
# 학생 수 : N의 2제곱 수 
# 학생들의 자리 정하기 / 1번부터 카운트 

# Condition>
# 비어있는 칸 중, 좋아하는 학생이 인접한 자리중 하나도 없어도 -> 만족하는 칸이 여러개인 셈 -> 2번 검사
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# input data
N = int(input())
mat = [[0]*N for _ in range(N)]
info_dict = {}
# Functions
# Def > 배치완료후, 학생들의 만족도 조사 
def sum_satisfy():
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            # Do > each 
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]

                if 0 <= nr < N and 0 <= nc < N:
                    if mat[nr][nc] in info_dict[mat[i][j]]:
                        cnt += 1
            if cnt <= 1:
                total += cnt 
            elif cnt == 2:
                total += 10
            elif cnt == 3:
                total += 100
            else: 
                total += 1000
            cnt = 0
    return total 
            
# Def > 자리 찾기 
def find_pos(id, like_l):
    pos_l = []
    pos_cnt = 0
    tmp_pos_cnt = 0
    # 탐색하다가, 빈자리가 있으면, 해당 자리를 기준으로 4방 탐색
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    # 경계검사 # 학생이 앉긴 했는지
                    if 0 <= nr < N and 0 <= nc < N and mat[nr][nc] != 0:
                        # 좋아하는 학생중에 있다면, 카운트 하기 
                        if mat[nr][nc] in like_l:
                            tmp_pos_cnt += 1
                # 현재 빈 자리에서 4방 탐색해서 알아낸 좋아하는 학생의 수
                # 현재 cnt가 더 크다면
                if tmp_pos_cnt > pos_cnt:
                    pos_cnt = tmp_pos_cnt # update
                    pos_l.clear()
                    pos_l.append([i, j])
                # 현재 cnt가 max값과 같다면 -> 추후 고려를 위해 추가 
                elif tmp_pos_cnt == pos_cnt:
                    pos_l.append([i,j])
                tmp_pos_cnt = 0
    return pos_l

def find_more_empty(pos_l):
    empty_space_cnt = 0
    tmp_space_cnt = 0
    empty_space_l = []
    # pos_l의 각 (r, c)에 대해 -> 인접 4방향중 빈칸의 갯수 카운트 
    for pos in pos_l:
        for d in range(4):
            nr = pos[0] + dr[d]
            nc = pos[1] + dc[d]
            # 경계검사
            if 0 <= nr < N and 0 <= nc < N:
                if mat[nr][nc] == 0:
                    tmp_space_cnt += 1
        # Do > compare
        if tmp_space_cnt > empty_space_cnt:
            empty_space_cnt = tmp_space_cnt
            empty_space_l.clear()
            empty_space_l.append([pos[0], pos[1]])
        elif tmp_space_cnt == empty_space_cnt:
            empty_space_l.append([pos[0], pos[1]])

        tmp_space_cnt = 0
    return empty_space_l 
            
# 첫 번째 학생의 자리는 조건에 의해 고정
info = list(map(int, input().split()))
init_id = info[0]
init_l = info[1:]
info_dict[init_id] = init_l
mat[1][1] = info[0]

for i in range(pow(N, 2) - 1):
    # 학생 번호 - 학생이 좋아하는 4명 번호 
    info = list(map(int, input().split()))
    id = info[0] 
    info = info[1:]
    info_dict[id] = info
    # 자리 찾기 
    pos_l = find_pos(id, info)
    # if > 만족하는 칸이 여러 개 
    if len(pos_l) <= 1: # 의심,, 
        mat[pos_l[0][0]][pos_l[0][1]] = id
        
    else:
        empty_space_l = find_more_empty(pos_l)
        # if > 행의 번호가 가장 작은 -> 열의 번호가 가장 작은 칸 찾기 
        if len(empty_space_l) <= 1:
            mat[empty_space_l[0][0]][empty_space_l[0][1]] = id 
        else:
            empty_space_l.sort(key = lambda x:(x[0], x[1]))
            mat[empty_space_l[0][0]][empty_space_l[0][1]] = id

# Answer > 만족도 구하기
answer = sum_satisfy()
print(answer)