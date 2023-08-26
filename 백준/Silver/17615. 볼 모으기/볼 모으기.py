# 23.08.26 / 21:34 ~ 

# 최소 이동횟수
# 가능한 경우 중, 최소

N = int(input())
_data = list(input())

ans = -1
# Exception
if 'R' not in _data or 'B' not in _data:
    ans = 0

# Solution >>>
# 빨간 / 파랑
# 파랑 / 빨강 

ans = min(_data.count('R'), _data.count('B'))
r_cnt = _data.count('R')
b_cnt = _data.count('B')

# 왼쪽
for i in range(1, N):
    if _data[i] != _data[0]:
        tmp = i
        if _data[0] == 'R':
            ans = min(ans, r_cnt - i)
        else:
            ans = min(ans, b_cnt - i)
        break 
_data = _data[::-1]
for i in range(1, N):
    if _data[i] != _data[0]:
        tmp = i
        if _data[0] == 'R':
            ans = min(ans, r_cnt - i)
        else:
            ans = min(ans, b_cnt - i)
        break 

print(ans)