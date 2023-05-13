# 0.1초 / 1024MB
# 23.05.13 / 16:46 ~
# 20:00 ~ 
# 접속순서 / 3번 ~ N+2번
# 지환-> 한명 출석코드 
# 본인의 배수인 학생들 -> 코드 보냄
# K명은 안보냄 체크도 안함

# Q번 반복
# 특정구간의 입장 번호 받은 학생들 중, 출석이 되지 않은 학생들의 수
import sys
input = sys.stdin.readline
# 5000이하 
# N : 학생 수 / K : 졸고있는 수 / Q: 출석코드 보낼 학생 수 / M : 구간의 수 
N, K, Q, M = map(int, input().split())

# K 정보 
k_list = list(map(int, input().split()))

# Q명 출석코드 정보
q_list = list(map(int, input().split()))

ans_list = [1] * ( N + 3) # 구간합 리스트 : 0으로 초기화 
k_visit = [0] * (N + 3)
# K정보 계산해두기
for k in k_list:
    k_visit[k] = 1 # k에는 전달해도, 출석도 x, 전달도 x

# Q정보 전달
for q in q_list:
    # 각 q에 대해 경계까지 퍼트리기

    # ** 이렇게 반복문 짜는게 더 깔끔 *** 
    # if q not in k_list:
    #     for num in range(1, ((N+2)//q) + 1):
    #         if k_visit[q*num] == 0:
    #             ans_list[q*num] = 0
    if k_visit[q] == 0: 
        ans_list[q] = 0
        tmp = q
        while True:
            q += tmp 
            if q >= N+3:
                break 
            if k_visit[q] == 1:
                continue
            ans_list[q] = 0

# 누적합 처리
for i in range(3, N+3):
    ans_list[i] += ans_list[i-1]

for m in range(M):
    # 구간 범위
    S, E = map(int, input().split())
    print(ans_list[E] - ans_list[S-1])
    
# **** 반복되는 같은 구간(= 연속된 구간)을, 반복해서 탐색할 필요가 없도록 **** # 