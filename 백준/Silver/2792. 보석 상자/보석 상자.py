# 1초 / 128Mb
# 23.05.27(SAT)

# 1:10 ~ 

# 각 보석 M 가지, 서로 다른 색상

# 모든 보석 -> N명

# 질투심 == 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 갯수
# 질투심이 최소가 되도록... 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

_list = [] # 각 보석의 갯수 

for m in range(M):
    _list.append(int(input()))

max_val = max(_list)

ans = 1000000001

# 막대로 생각하고 자르기
def find(val):
    # traversal 
    cnt = 0
    for i in range(M):
        d, m = _list[i]//val, _list[i]%val
        cnt += d
        if m > 0:
            cnt += 1

    return cnt

def binSearch(left, right):
    global ans

    if left > right:
        return 
    
    mid = (left + right)//2

    # 현재 mid값을 가질 때, 각 보석에 대해서 나눠지는 구간의 총 갯수를 계산 
    res = find(mid)

    # 나눠진 조각이 N명보다 많으면 -> 조각의 갯수 줄이기 -> mid감소시키기 
    if res > N:
        binSearch(mid+1, right)
    # 나눠진 조각이 N명보다 적으면 -> mid증가 
    else: 
        ans = min(ans, mid)
        binSearch(left, mid-1)

binSearch(1, max_val)

print(ans)