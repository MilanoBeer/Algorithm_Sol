# 무방향
# 유지비 
# 마을 => 두개의 분리된 마을

# 분리 : 
# 각 마을안에 집들이 서로 연결되도록

# 분리된 두 마을사이에는 길 없어도 됨

# 목표 
    # 유지비의 합을 최소로 

import sys
input = sys.stdin.readline

# N : 2이상, 100,000이하 
# M : 1이상, 1,000,000이하 
# -> sprase matrix -> kruskal 
N, M = map(int, input().split())

edges = []
for m in range(M):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

parent = [i for i in range(N+1)]

# sort
edges.sort(key = lambda x:x[2])

# find, 
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union 
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# traversal edges
ans = 0
choice_e = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        choice_e += 1
        ans += cost
    if choice_e == N-2:
        break 


print(ans)
