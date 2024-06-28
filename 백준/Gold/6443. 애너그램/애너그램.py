# 모든 경우 
# 정렬
# 중복처리 

# output: 알파벳 순서대로
from itertools import permutations
from collections import defaultdict
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ss = set()
def back(_val, cnt, visited, length, prev): # 백트래킹 -> index, visited
    # terminal condition 
    if cnt == len(_val):
        print(prev)
        return

    for k, v in visited.items(): 
        if v:
            # print(" kkkk : ", k)
            prev += k
            visited[k] -= 1
            
            back(_val, cnt + 1, visited, length, prev)
            
            visited[k] += 1
            prev = prev[:-1]

for _ in range(N):
    _val = sorted(list(input()))
    visited = defaultdict(int)

    for v in _val:
        visited[v] += 1
    back(_val, 0, visited, len(_val), '')