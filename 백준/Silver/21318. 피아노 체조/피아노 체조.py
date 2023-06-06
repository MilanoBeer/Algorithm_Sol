# 0.5초 / 1024MB 
# 23.06.06 
# 09:55 ~ 

# N개의 악보 / 1번 ~ 
    # 각 악보 난이도 : 1 이상, 10^9 / 수가 클술고 어렵
# 악보 두개의 번호 골라서, 순서대로 연주 

# CONDITION : 지금 연주하는 악보 난이도 > +1 바로 다음 악보 난이도 -> 실수 
    # 지금 실수! i시점에! 

# OUTPUT :실수하는 곡이 몇개? 

import sys
input = sys.stdin.readline

N = int(input()) # 1이상, 10만 이하 
_info = list(map(int, input().split()))
_info.insert(0, 0)

Q = int(input()) # 질문갯수
_info_each = [0] * (N+1)
_info_sum = [0] * (N+1)

# MAKE prefix-sum 
for i in range(1, N):
    if _info[i] > _info[i+1]:
        _info_each[i] = -1

_info_sum = _info_each[:]

for i in range(2, N+1):
    _info_sum[i] += _info_sum[i-1]

# print(*_info_sum)

for q in range(Q):
    cnt = 0 
    x, y = map(int, input().split())

    tmp = _info_sum[y] - _info_sum[x-1]

    if _info_each[y]== -1:
        tmp += 1

    if tmp < 0:
        tmp = -tmp
        print(tmp)
    else:
        print(0)

