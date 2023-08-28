# 23.08.28 / 19:16 ~ 
from collections import deque

T = int(input())

for t in range(1, T+1):
    _data = list(map(int, input().split()))
    num = _data[0]
    _data = _data[1:]

    stack = []
    cnt = 0
    for i in range(20):
        isFind = False
        # print("i : ", i, ", stack :", stack)
        if not stack:
            stack.append(_data[i])
        else:
            for s in range(len(stack)-1, -1, -1):
                if stack[s] < _data[i]:
                    isFind = True
                    break
                else:
                    cnt += 1
            if isFind:
                stack = stack[:s+1] + [_data[i]] + stack[s+1:]
            else:
                # stack.append(_data[i])
                stack.insert(0, _data[i])
    # Output
    print(t,cnt)