from collections import deque

N, K = map(int, input().split())

# 이동 : x-1 / x+1 / 2*x => 모두 1초후 
# Solution 
# 가장 빠르게 도착하는 시간이 여러 개일 수 있음
# BFS -> 레벨단위 / 
INF = 999999
min_val = INF
cnt = 0

def bfs(start):
    global min_val 
    global cnt 

    queue = deque()
    queue.append(start)
    visited = [-1] * 200002
    visited[start] = 0 # TODO : 나중에 -1 처리 
    
    while queue:
        cur = queue.popleft() # pop 

        # check 
        if cur == K:
            if min_val >= visited[cur]:
                min_val = visited[cur]
                cnt += 1
            continue

        # 3가지 액션
        for d in [cur -1, cur + 1, cur*2]:
            # 경계검사
            if 0 <= d <= 100000:
                if visited[d] == -1 or visited[d] == visited[cur] +1: # K는 방문했어도 통과하도록 
                    # if min_val != INF and min_val < visited[cur] + 1:
                    #     continue
                    visited[d] = visited[cur] + 1
                    queue.append(d)
# 방문여부로 따지면 안된다 / 
bfs(N)
print(min_val)
print(cnt)
