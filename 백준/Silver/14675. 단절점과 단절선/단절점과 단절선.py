# 1초 / 512MB
# 23.05.26
# 12:15 ~ 

import sys
input = sys.stdin.readline

N = int(input()) # 정점 개수 / 2이상, 10만 이하 

# 트리 생성
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 특정 점이 단절점인가 판단
def isVertex(v):
    # 리프노드거나 루트노드면 no 
    if len(tree[v]) < 2:
        return False
    else:
        return True
    
q = int(input())# 질의 개수 
for _ in range(q):
    # t : 1 -> k 가 단절점인가? / =2 -> 단절선인가? 
    t, k = map(int, input().split())

    if t == 1:
        if isVertex(k):
            print("yes")
        else:
            print("no")
    else:
        print("yes")
