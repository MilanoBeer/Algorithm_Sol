# 2초 / 128MB
# 23.05.20
# 16:20 ~ 

# N개의 원소 / 양방향 순환 큐 
from collections import deque

# 큐의 크기 N : 50보다 작거나 같은 자역수 / "50"
# 뽑아내려는 수의 갯수 M : N보다 작거나 같은 자연수 
N, M = map(int, input().split())

# 뽑아내려고 하는 수의 "위치"
_list = list(map(int, input().split()))
_data = deque()

for i in range(1, N+1):
    _data.append(i) # list통째로 append하면 안됨

# 1부터 ~ N
op_cnt = 0
# _list의 맨 앞부터 찾기 
for i in range(len(_list)):
    # _data의 맨 앞이 현재 list의 목표값이면 종료 
    if _data[0] == _list[i]:
        _data.popleft()
        continue
    # 그게 아니면, 
    else:
        # 타겟을 기준으로 왼쪽 것들을 보낼지, 오른쪽을 보낼지 정하기
        idx = _data.index(_list[i])
        other_idx = len(_data) - idx
        # 타겟까지 포함하여 앞으로 보내기
        if idx > other_idx:
            _data.rotate(other_idx)
            op_cnt += other_idx
        else:
            # 타겟은 포함하지 않고, 앞에것들 뒤로 보내기 
            _data.rotate(-idx)
            op_cnt += idx
        # 뽑기
        _data.popleft()
print(op_cnt)            