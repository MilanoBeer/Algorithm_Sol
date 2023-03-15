# 1 <= N < 100,000개의 로프
# 로프 : 들 수 있는 중량이 각각 다름

# 여러개 로프 병렬로 연결 -> 각 로프에 걸리는 중량을 나눌 수 있다 

# Condition 
    # K개의 로프 사용해, W무게를 들어올릴 때, 
    # 각각의 로프에 모두 고르게 W/k만큼의 중량이 걸리게 된다 

# Purpose
    # 로프들에 대한 정보 -> 들어올릴 수 있는 물체의 최대 중량 구하기 
    # 모든 로프 사용할 필요는 X / 임의 몇개만 사용해도 무방

N = int(input())
weight_l = []

# 로프 정보 
for i in range(N):
    weight_l.append(int(input()))

# 정렬하기
weight_l.sort()
max_weight = -1
# 로프를 1개 사용-> 2개 -> .. / N = 4 / 10, 30, 150, 200
for i in range(N): # 1개만 사용, 2개만 사용, ... N개 모두 사용
    # if > i= 2
    # N-2, N-1 자리의 로프만 사용해서 들 수 있는 최댓값
        # => 현재 시점의 최솟값 * 현재 사용되는 로프의 갯수 
    max_weight = max(max_weight, weight_l[N-1-i] * (i+1))
    # max_list.append(weight_l[N-1-i] * (i+1)) # 다 추가해두고, 마지막에 max찾는것도 방법

print(max_weight)