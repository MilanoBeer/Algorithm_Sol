
from collections import deque
import sys

a, b = map(int, input().split())
N, M = map(int, input().split())

# mat = [[0] * (M+1) for _ in range(N+1)]
mat = [[] for _ in range(N+1)]
for m in range(M):
    c, d = map(int, input().split())
    mat[c].append(d)
    mat[d].append(c)

ans = sys.maxsize

def bfs(start):
    global ans 

    dq = deque()
    # visited = [[0] * (M+1) for _ in range(N+1)]
    visited = [-1] * (N+1)
    dq.append(start)
    visited[start] = 0

    while dq:
        cur = dq.popleft()

        if start == a and cur == b:
            ans = min(ans, visited[cur])
        if start == b and cur == a:
            ans = min(ans, visited[cur])

        # if visited[cur] == 0:
        for nxt in mat[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1 
                dq.append(nxt)

bfs(a)
bfs(b)
if ans == sys.maxsize:
    ans = -1
print(ans)