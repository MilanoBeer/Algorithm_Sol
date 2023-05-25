# 크루스칼
# Greedy Method!!! 

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
for e in range(E):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))
#sort
edges.sort(key = lambda x:x[2]) # cost기준으로 오름차순 정렬
# parent list 
parent = [i for i in range(V+1)]
    
# find
def find(v):
   if parent[v] == v:
       return v
   parent[v] = find(parent[v])

   return parent[v]  

# parent
def union(a, b):
    a = find(a)
    b = find(b)

    # 더 값이 작은쪽을 부모로 삼기 
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
# Traversal : 크루스칼은 "간선 선택""
for u, v, cost in edges:
    # u, v를 잇는 정점이 사이클을 이루지 않으면
    if find(u) != find(v):
        union(u, v)
        ans += cost 

print(ans)

    
