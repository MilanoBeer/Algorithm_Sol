# 1초 / 256MB
# 23.05.06
# 23:15 ~ 25 / stop / 18:30 ~ 

# 한개의 안테나 
# 목적 : 안테나로부터, 모든 집까지의 거리 총 합 -> 최소 
# Condition: 집이 위치한 곳에만 설치 가능
    # 동일한 위치에 집 여러 개 가능 


# N : 집의 수 / 1이상, 20만 이하 
N = int(input())

# 집 위치정보
pos = list(map(int, input().split()))
# pos.insert(0,0)
pos.sort()


#처음 집위치를 기준으로 첫번째 합 구하기
tmp_sum = 0
for i in range(N):
    tmp_sum += abs(pos[0] - pos[i])

# 2번째부터 min 갱신 
sum_list = [tmp_sum]
for i in range(1, N):
    diff = pos[i] - pos[i-1]
    tmp_val = sum_list[i-1] + (i * diff) - ( N - i)*diff
    sum_list.append(tmp_val)

min_val = min(sum_list)

for i in range(len(sum_list)):
    if min_val == sum_list[i]:
        print(pos[i])
        break 

# output : 안테나를 설치할 위치를 선택하는 프로그램
# Exception : 설치가능한 위치값 여러개 -> 가장 작은 값
    # -> list에 매번 담거나, min 을 갱신하거나 

