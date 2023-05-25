# 1초 / 128MB
# 23.05.25 
# 14:10 ~ 

# n개의 별을 이어서 별자리 만든다
    # => n개의 정점을 연결해서 그래프를 만든다 

# 조건
import sys
input = sys.stdin.readline

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
data = [list(map(float, input().split())) for _ in range(n)]

parent = [i for i in range(n)]

dist =[]

for i in range(n-1):
    for j in range(i+1, n):
        tmp = ((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) **2)**0.5
        dist.append((tmp, i, j))
dist.sort()

ans = 0.0
for cost, a, b in dist:
    if find(a) != find(b):
        union(a, b)
        ans += cost 

print(f'{ans:.2f}')