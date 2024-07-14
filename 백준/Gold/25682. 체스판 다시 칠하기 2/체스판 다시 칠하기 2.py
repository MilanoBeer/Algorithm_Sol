import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
mat = [list(input()) for _ in range(N)]

_pre = [[0] * (M+1) for _ in range(N+1)]


for i in range(1, N + 1):
    for j in range(1, M + 1):
        if (i + j) % 2 == 0:
            if mat[i - 1][j - 1] == 'B':
                _pre[i][j] = _pre[i-1][j] + _pre[i][j-1] - _pre[i-1][j-1]
            else:
                _pre[i][j] = _pre[i-1][j] + _pre[i][j-1] - _pre[i-1][j-1] + 1
        else:
            if mat[i - 1][j - 1] == 'W':
                _pre[i][j] = _pre[i-1][j] + _pre[i][j-1] - _pre[i-1][j-1]
            else:
                _pre[i][j] = _pre[i-1][j] + _pre[i][j-1] - _pre[i-1][j-1] + 1
max_ = - sys.maxsize
min_ = sys.maxsize

for r in range(K, N + 1):
    for c in range(K, M + 1):
        max_ = max(_pre[r][c] - _pre[r-K][c] - _pre[r][c-K] + _pre[r-K][c-K], max_)
        min_ = min(_pre[r][c] - _pre[r-K][c] - _pre[r][c-K] + _pre[r-K][c-K], min_)

print(min(max_, min_, K*K - min_, K*K - max_))