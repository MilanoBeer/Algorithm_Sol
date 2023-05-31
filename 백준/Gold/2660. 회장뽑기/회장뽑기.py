# 1초 / 128MB
# 23.05.31 
# 10:11 ~ 10:36

# 직접은 몰라도, 몇사람 통하면 모두 서로 알수도 있음
# 각 회원 -> 다른 회원들과 가까운 정도에 따라 점수를 받는다 

# Exception 
    # a - b가 친구 && a - 다른사람 - b 
    # => "친구사이"

import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 50이하

# DS
_score = [0] * (N+1) # 점수기록 배열 # 회원번호는 1부터 **** 
_ans = [] # 회장후보 리스트 / append할 때 회원 번호로
ans_val = 0 # 회장 후보의 점수 # 최솟값 
mat = [[] for _ in range(N+1)] # Adj List가 적절

# Sol
# 각 회원의 점수를 먼저 찾기
# 그중에서 최솟값 확인
# 해당 최솟값을 점수로 가지는 회원들의 목록 
# 정렬 하기 ***** 

# 몇 depth안에서 모든 친구를 만나는지? 
    
while True:
    a, b = map(int, input().split()) 
    
    if a == -1 and b == -1:
        break 
    
    mat[a].append(b)
    mat[b].append(a)

def bfs(vert):
    # init
    queue = deque()
    queue.append(vert)

    while queue:
        # pop -> 
        cur = queue.popleft()

        # cur의 인접회원들에 대해
        for adj in mat[cur]:
            # 아직 방문전이면
            if visited[adj] == -1:
                visited[adj] = visited[cur] + 1
                queue.append(adj)

# 각 회원에 대해 BFS
for i in range(1, N+1):
    # visited갱신
    visited = [-1] * (N+1)
    visited[i] = 0

    bfs(i)
    _score[i] = max(visited[1:])

# OUTPUT 
    # 점수가 가장 작은 사람이 회장
    # 회장의 점수와 , 회장이 될 수 있는 모든 사람을 찾기 
_score = _score[1:]
ans_val = min(_score)
print(ans_val, _score.count(ans_val))
for i in range(len(_score)):
    if _score[i] == ans_val:
        print(i+1, end=' ')
print()
    

