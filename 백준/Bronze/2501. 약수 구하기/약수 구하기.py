

N, K = map(int, input().split())

_list = []

# 1부터 N까지 확인
for i in range(1, N+1):
    # 0으로 나눠떨어지면, 추가 
    if N % i == 0:
        _list.append(i)
    
_list.sort()

if len(_list) < K:
    print(0)
else:
    print(_list[K-1])

