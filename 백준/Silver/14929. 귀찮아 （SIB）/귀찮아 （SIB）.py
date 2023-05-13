# 2초/ 512MB

# 23.05.13
# 16:00 ~
n = int(input())
_origin_list = list(map(int, input().split()))

# list누적합 구하기
_list = _origin_list[:]
for i in range(1, n):
    _list[i] += _list[i-1]

# 계산하기
ans = 0
for i in range(n):
    ans += _origin_list[i]*(_list[n-1] - _list[i])

print(ans)