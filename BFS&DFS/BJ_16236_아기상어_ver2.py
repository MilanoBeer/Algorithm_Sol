from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    print()

# init
N = int(input())
mat = [ list(map(int, input().split)) for _ in range(N)]
shark_size = 2 # 초기값 2

# 상어 위치, 물고기 위치 
shark_pos = []
fish_pos = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            shark_pos.append([i, j])
        if mat[i][j] != 9 and mat[i][j] > 0:
            fish_pos.append([i, j])

# fish_pos traversal > if less than shark_size

