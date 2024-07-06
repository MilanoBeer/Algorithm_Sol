# 16:40 ~ 
import sys

def input():
    return sys.stdin.readline().rstrip()

N, S = map(int, input().split())
_data = list(map(int, input().split()))
ans = sys.maxsize

# init prefix sum
_pre = [0] * (N+1)
_pre[1] = _data[0]

for i in range(2, N + 1):
    _pre[i] += _pre[i-1] + _data[i - 1]

s = 0
e = 1
while s <= e and e <= N:
    if _pre[e] - _pre[s] < S:
        e += 1
    else:
        ans = min(ans, e - s)
        s += 1
if ans == sys.maxsize:
    ans = 0
print(ans)

# *** ERROR: 예외케이스 0되는거 고려안함 
# *** 