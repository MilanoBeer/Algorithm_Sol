import sys
from collections import deque

T = int(input())

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited = [0 for _ in range(n)]

    while dq:
        x, y = dq.popleft()

        # check last
        if abs(x - end_x) + abs(y - end_y) <= macju:
            print("happy")
            return
        
        for i in range(n):
            if visited[i] == 0:
                if abs(x - peon_pos[i][0]) + abs(y - peon_pos[i][1]) <= macju:
                    dq.append((peon_pos[i][0], peon_pos[i][1]))
                    visited[i] = 1
    print("sad")

for t in range(T):
    n = int(input())

    macju = 20 * 50

    start_x, start_y = map(int, input().split())
    peon_pos = []

    for i in range(n):
        x, y = map(int, input().split())
        peon_pos.append((x, y))

    end_x, end_y = map(int, input().split())
    bfs(start_x, start_y)