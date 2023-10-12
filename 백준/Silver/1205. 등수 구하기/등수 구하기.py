# 23.10.12 / 23:25 ~ 
from bisect import bisect_left, bisect_right
# N : 리스트에 있는 점수 N개
# P : 리스트에 올라갈 수 있는 점수 N개
N, score, P = map(int, input().split())

if N > 0:
    _data = list(map(int, input().split()))

    def insertion(s):
        _data.append(s)
        _data.sort(reverse = True)
        _idx = [0] * (len(_data))
        _idx[0] = 1
        val = 1
        for i in range(1, len(_data)):
            if _data[i] == _data[i-1]:
                _idx[i] = _idx[i-1]
                val += 1
            else:
                _idx[i] = _idx[i-1] + val
                val = 1
        
        return _idx[_data.index(s)]
    
    if N < P:
        ans = insertion(score)
    else:
        if _data[-1] >= score: ans = -1
        else: ans = insertion(score)
else:
    ans = 1

# output
print(ans)

# def : 자리 찾는 함수 
# _data에 맨 뒤에 일단 추가
# sort, reverse
# score의 위치찾기 -> bisect 활용 

# 아직 들어갈 자리가 있다면
    # 자리찾기

# 들어갈 자리가 없다면
    # if : 맨 뒤의 값보다 작다면 -1 
    # else
        # 자리찾기






