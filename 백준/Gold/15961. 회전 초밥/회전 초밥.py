from collections import defaultdict
import sys

def input():
    return sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())
_data = []
for n in range(N):
    _data.append(int(input()))

# init
ans = 0
s, e = 0, k - 1
dd = defaultdict(int)
# dd[c] = 1
tmp_ans = 0
for i in range(e + 1):
    if dd[_data[i]] == 0:
        tmp_ans += 1
    dd[_data[i]] += 1
if dd[c] == 0:
    tmp_ans += 1
    dd[c] = 1

ans = max(tmp_ans, ans)
# search
while s < N:
    dd[_data[s]] -= 1
    if dd[_data[s]] == 0:
        tmp_ans -= 1
    s += 1
    e += 1
    e = e % N # 미리 넘겨주기

    if dd[_data[e]] == 0:
        tmp_ans += 1
    dd[_data[e]] += 1

    if dd[c] == 0:
        tmp_ans += 1
        dd[c] = 1
    ans = max(tmp_ans, ans)
print(ans)

        