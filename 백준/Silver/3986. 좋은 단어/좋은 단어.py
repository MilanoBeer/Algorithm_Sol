# 1초 / 256MB

import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 단어 수 : 최대 100

ans_cnt = 0

for n in range(N):
    data = list(input())
    stack = []
    for i in data:
        # 빈 스택에 push
        if len(stack) == 0:
            stack.append(i)

        # 아니라면
        else:
            # 가장 위에 문자랑, 현재 문자가 같다면
            if stack[-1] == i:
                stack.pop()
            # 다르다면
            else:
                stack.append(i)
    if len(stack) == 0:
        ans_cnt += 1

print(ans_cnt)