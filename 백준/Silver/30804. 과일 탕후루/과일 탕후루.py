from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)

N = int(input())
_data = list(map(int, input().split()))

s = 0
e = 0
ans = 0
dd = defaultdict(int)

def call_recur(s, e, _max, kind):
    global N

    # terminal
    if e >= N:
        return _max

    # recursive
    # - end는 무조건 이동
    dd[_data[e]] += 1
    if dd[_data[e]] == 1:
        kind += 1
    # kind검사 
    if kind > 2:
        # s를 이동
        dd[_data[s]] -= 1
        if dd[_data[s]] == 0:
            kind -= 1
        s += 1

    _max = max(_max, e - s + 1) 
    return call_recur(s, e + 1, _max, kind)
    
# 재귀 처음 호출부분
 # start, end, max_num, kind) 
print(call_recur(0, 0, 0, 0))