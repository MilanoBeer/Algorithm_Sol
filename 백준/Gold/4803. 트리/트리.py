import sys
input = sys.stdin.readline

# start 노드부터 시작하여 DFS를 끝까지 돌고
# 사이클 존재 여부를 리턴하는 함수
def findCycle_dfs(start):
    # 진입부분에서 방문처리 
    
    # for: start의 인접노드들 확인
    for adj in mat[start]:
        # if 인접노드가, 부모노드라면 -> continue, 다음 인접정점 검사
        if parent[start] == adj:
            continue

        # 부모노드가 아닌데, 방문이력이 있다면 => cycle => return false
        if parent[start] != adj and visited[adj] != 0:
            # return True
            return False

        # 아직 방문하지 않은 점들 # call dfs
        parent[adj] = start
        visited[start] = 1

        # 싸이클리 리턴되오면, False를 리턴
        if not findCycle_dfs(adj):
            return False
    # 연결된 정점이 없거나 or 더 이상 검사할 정점없이 지나갔을 떼 
    return True

case = 1 # input case count
while True:
    n, m = map(int, input().split())

    # Data DS 
    mat = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    count = 0
    
    parent = [0] * (n+1)
    # TERMINAL CONDITION 
    if n == 0 and m == 0:
        break 

    # 양방향 매핑
    for _ in range(m):
        a, b = map(int, input().split())
        mat[a].append(b)
        mat[b].append(a)
    
    # SOLUTION : ALGO : DFS
    # 모든 vertex에 대해, 시작점으로 한번씩 설정해서 확인해야함
    for i in range(1, n+1):
        # 아직 방문되지 않은 점이라면 
        if visited[i] == 0:
            # 아직 방문하지 않은 점이라면, 부모노드 설정
            parent[i] = i
            visited[i] = 1

            # 트리라면(=사이클이 없으면), count추가 
            if findCycle_dfs(i):
                count += 1

    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')
    case += 1