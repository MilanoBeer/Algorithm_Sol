import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

_list = list(input() for _ in range(N))
_list.sort(key = lambda x:(len(x)))
ans = 0

for i in range(N):
    isFlag = True
    for j in range(i + 1, N):
        if _list[j][:len(_list[i])] == _list[i]:
            isFlag = False
            break 
    # check 
    if isFlag:
        ans += 1
print(ans)