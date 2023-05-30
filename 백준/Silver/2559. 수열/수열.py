# 1초 / 128MB
# 23.05.30
# 14:32 ~ 

# 매일 아침9시 , 정수 수열 
# 연속 며칠동안의 온도 합이 가장 큰 값인지?

# N : 전체날짜수 / K : 연속날짜수 
N, K = map(int, input().split())

_list = list(map(int, input().split()))
_list.insert(0, 0)

max_val = - 10000000

for i in range(1, N+1):
    _list[i] += _list[i-1]

# find max
idx = 0
for i in range(K, N+1):
    tmp = _list[i] - _list[idx]
    max_val = max(max_val, tmp)
    idx += 1

print(max_val)
    
