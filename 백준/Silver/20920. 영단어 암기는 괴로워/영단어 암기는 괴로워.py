# 23:02 ~ 

from collections import Counter
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
_words = []
for n in range(N):
    # 단어 입력받고
    # M글자 이상인 단어라면
        # 외울 목록에 추가 
    tmp = input()
    if len(tmp) >= M:
        _words.append(tmp)

_dd = Counter(_words)

_result = sorted(_dd.items(), key = lambda x:(x[1]), reverse=True)
_result.sort(key = lambda x:(- x[1], -len(x[0]), x[0]))

for e in _result:
    print(e[0])
