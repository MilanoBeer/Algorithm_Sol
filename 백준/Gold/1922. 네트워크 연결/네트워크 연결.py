
import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터의 수 / 최대 1000
M = int(input()) # 연결할수 있는 선의 수 == 간선의 수 

edges = []
for m in range(M):
    # a와 b는 같을수도 있음
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

# sort
edges.sort(key = lambda x:x[2])

# parent
parent = [i for i in range(N+1)]

# find
def find(u):
    if parent[u] == u:
        return u 
    parent[u] = find(parent[u])
    return parent[u]

# union 
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# execute
ans = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b) 
        ans += cost
print(ans)
