# 1초 / 256MB
# 23.05.26
# 12:45 ~ 

# 이진검색트리
# 조건
    # 전위순회 결과 주어진 -> 후위순회결과 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 노드 갯수는 1만개 이하 / 같은 키 노드는 없음
data = []
while True:
    try:
        num = int(input())
        data.append(num)
    except:
        break 

def postorder(s, e):
    if s > e:
        return 
    
    mid = e + 1

    for i in range(s + 1, e + 1):
        if data[i] > data[s]:
            mid = i
            break 
    postorder(s + 1, mid -1) 
    postorder(mid, e)
    print(data[s])

postorder(0, len(data) - 1)
    