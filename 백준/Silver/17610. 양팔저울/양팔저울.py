# 23.08.26 / 18:21 ~ 18:57 -> pypy3는 통과, python은 시초.. / 

from itertools import combinations
import sys
def input():
    return sys.stdin.readline().rstrip()

k = int(input())
weights = list(map(int, input().split()))
tot = sum(weights)
checked = [0] * (tot+1)
checked[0] = 1

# Solution >> DFS 
# 하나 더 뽑아서 더하거나
# 안 뽑거나
# 하나 더 뽑아서 기존값에서 빼거나 

def dfs(cnt, val):
    if cnt == k:
        checked[val] = 1
        return 
        
    dfs(cnt + 1, val + weights[cnt])
    dfs(cnt + 1, val)
    dfs(cnt + 1, abs(val - weights[cnt]))
    
dfs(0, 0)
print(checked.count(0))
