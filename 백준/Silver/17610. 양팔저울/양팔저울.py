# 23.08.26 / 18:21 ~ 

from itertools import combinations
import sys
def input():
    return sys.stdin.readline().rstrip()

cnt = 0

k = int(input())
weights = list(map(int, input().split()))
tot = sum(weights)

# Solution >>> 
# 1. 완탐
    # {1, 2, 6 }
    # {1 + 2 / 1 + 6 / 2 + 6} -> combinations
    # { 1+ 2 + 6}

checked = [0] * (tot + 1) 
checked[0] = 1

# for i to k개 뽑기
_list = []
for i in range(1, k+1):
    for case in combinations(weights, i):
        tmp = sum(case)
        checked[tmp] = 1
        _list.append(tmp)
_list.sort(reverse=True)

for i in range(len(_list)):
    for j in range(i+1, len(_list)):
        idx = abs(_list[i] - _list[j])
        # _list.append(idx)
        if checked[idx] == 0:
            checked[idx] = 1

print(checked.count(0))



    



# output : 불가능한 경우의 수 갯수 