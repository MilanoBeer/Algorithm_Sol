# 23.10.13 / 15:01 ~ 

N = int(input())
_list = list(map(int, input().split()))

stack = []
_ans = [0] * (N)

for i in range(len(_list)):
    if not stack:
        stack.append((_list[i], i))
    else:
        # i원소보다 더 큰 top을 만날때까지 pop
        while stack and stack[-1][0] < _list[i]:
            stack.pop()
        if stack:
            _ans[i] = stack[-1][1] + 1
        stack.append((_list[i], i))

print(*_ans)