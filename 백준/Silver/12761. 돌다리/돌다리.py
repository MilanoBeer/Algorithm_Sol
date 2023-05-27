# 1초 / 128MB
# 23.05.27
# 13:20 ~ 

# 돌다리 일직선 -> 선형 , 리스트
# 0부터 10만
# N번 - M번
# 최소시간
# +1, -1 / +A, -A / +B, -B / A배 , B배


from collections import deque

A, B, N, M = map(int, input().split())
dr = [1, -1, A, -A, B, -B]
dm = [A, B]

move_cnt = 0 # 최소이동한 횟수 
visited = [-1] * (400000)

def bfs(v):
    # init queue
    queue = deque()
    queue.append(v)

    while queue:
        cur = queue.popleft()

        # 목적지 확인
        if cur == M:
            print(visited[cur])
            break 
        # 계속 이동
        for plus in dr:
            nv = cur + plus
            # 경계검사 & 방문검사 
            if 0 <= nv <= 100000 and visited[nv] == -1:
                visited[nv] = visited[cur] + 1
                queue.append(nv)

        # 곱하기 이동
        for mul in dm:
            nm = cur * mul
            if 0 <= nm <= 100000 and visited[nm] == -1:
                visited[nm] = visited[cur] + 1
                queue.append(nm)

# 첫 시작 방문체크 
visited[N] = 0
bfs(N)