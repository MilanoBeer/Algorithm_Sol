# 길이가 N인 컨베이어 벨트 
# 길이가 2N인 벨트 

# i번 칸의 내구도는 Ai 
# 1번칸 : "올리는 위치" / N번 칸 : "내리는 위치"

# 로봇은 올리는 위치에만 올릴 수 있음 / 
# 로봇이 내리는 위치(= N번칸)에 도달 -> 즉시 내림 

# Input> 
# N, K # N은 길이, K 는 내구도가 0인 칸의 갯수 카운트, 종료조건

# Condition > 
# ***** 벨트도, 로봇도 같이 회전한다 ***** 
# *** 가장 처음 단계 : 1단계 ***

N, K = map(int, input().split())
belt_l = list(map(int, input().split()))

# 로봇의 위치들을 담을 리스트 
robot_l = [0] * N # [0, 0, 0]
robot_pos = []
k_cnt = 0 # 내구도 0인 갯수 카운트 

# Def > 벨트와 로봇을 함께 회전시킨다. 
def rotate():
    last_val = belt_l[-1]

    # belt rotate
    for i in range(2*N-1, 0, -1):
        belt_l[i] = belt_l[i-1]
    belt_l[0] = last_val

    # robot rotate
    for i in range(N-1, 0, -1): # 마지막 칸은 "내리는 위치"이므로 검사할 필요가 없음
        robot_l[i] = robot_l[i-1]
        robot_l[i-1] = 0
    robot_l[-1] = 0 # 내리는 위치 -> 로봇 없애기 

# Def > move robots( first robot -> second .. )
def move_robots():
    # 가장 먼저 벨트에 올라간 로봇부터 -> 위쪽 벨트의 가장 오른쪽부터 이동
    # 이동할 칸의 내구도 검사 
    for i in range(N-2, -1, -1): # i = 1, 0
        # 현재 칸에 로봇이 존재하고, 다음 칸에 로봇이 없고, 다음 칸의 내구도가 0이 아니라면 
        if robot_l[i] != 0 and belt_l[i+1] != 0 and robot_l[i+1] == 0:
            robot_l[i+1] = 1
            robot_l[i] = 0
            belt_l[i+1] -= 1
    robot_l[-1] = 0 # 내리는 칸의 로봇 없애기 


# Def > upload robot, on "올리는 위치"
def upload_robot():
    # if > 내구도가 0이 아니라면 
    if belt_l[0] != 0: 
        robot_l[0] = 1
        belt_l[0] -= 1

# Def > 내구도가 0인 칸의 갯수 카운트 
def count_zero_space():
    tmp_answer = 0
    for i in range(N*2):
        if belt_l[i] == 0:
            tmp_answer += 1
    return tmp_answer

phase_cnt = 0
while k_cnt < K:
    phase_cnt += 1
    rotate()                    # 1단계 
    move_robots()               # 2단계
    upload_robot()              # 3단계
    k_cnt = count_zero_space()  # 4단계 : k_cnt 갱신 

print(phase_cnt)