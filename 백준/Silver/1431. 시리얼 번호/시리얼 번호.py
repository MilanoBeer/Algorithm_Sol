# 2초 / 128MB
# 23.06.22

# 정렬기준
    # 시리얼번호의 길이짧은게 먼저 
    # 서로 같은 길이 -> 모든 자리수의 합 -> 작은 합이 먼저 
    # 사전순 
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) 
_data = [list(input()) for _ in range(N)]

# 최대 길이 50 / 각 번호길이 50 

# bubble sort? 

def total(x):
    # 숫자만 
    res = 0 
    for i in x:
        if i.isdigit():
            res += int(i)
    return res

_data.sort()
_data.sort(key = lambda x:(len(x), total(x)))

for i in _data:
    print(''.join(i))


