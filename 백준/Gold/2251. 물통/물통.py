from collections import deque

# ?: 주고받는게 끝나는 시점..? 
A, B, C = map(int, input().split())
_ans = []
dq = deque()
dq.append((0, 0))
visited = [[0] * 201 for _ in range(201)]
visited[0][0] = 1
# queue에서 관리하는 원소 

def check(a, b):
    if visited[a][b] == 0:
        visited[a][b] = 1
        dq.append((a, b))

def bfs():
    while dq:

        a, b = dq.popleft()
        c = C - a - b

        if a == 0:
            _ans.append(c)

        # 물 이동
        # a - > b
        w = min(a, B - b)
        check(a - w, b + w)

        # a -> c
        w = min(a, C - c)
        check(a - w, b)


        # b -> a
        w = min(b, A - a)
        check(a + w, b - w)

        # b -> c
        w = min(b, C - c)
        check(a, b - w)

        # c - > a
        w = min(c, A - a)
        check(a + w, b)

        # c -> b
        w = min(c, B - b)
        check(a, b + w)

bfs()
_ans.sort()
print(*_ans)