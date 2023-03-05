# N개의 시험장 , 각 응시장마다 응시자의 수 정해져있음 
# 총감독관 - B명 / 부감독관 - C명
# 각 응시장마다, 총감독은 1명, 부감독 여러명 가능
# 응시자들은 모두 감시해야 함 / 
# => 필요한 감독관의 최솟값 

# input
# N
# 각 시험장의 응사자의 수 
# B, C

N = int(input())
person_l = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
# traversal : person_l에서 강의실 하나씩 
for i in range(len(person_l)):
    # 각 강의실에서 총감독관B빼기 
    each = person_l[i] - B
    answer += 1

    # if > 뺀 값이 0이거나 0보다 작을 경우
    if each <= 0:
        continue
    # else > 부감독관 계산하기 
    else:
        # 부감독관C로 나누어 떨어질 경우
        if each % C == 0:
            answer += each//C
            continue
        else:
            answer += (each//C+1)

print(answer)
