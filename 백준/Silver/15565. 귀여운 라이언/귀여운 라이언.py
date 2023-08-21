# 23.08.21 / 15:08 ~ 
import sys
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
# 1,000,000 백만
_list = list(map(int, input().split()))

# Exception 
# 라이언 -> 1

# Sol
    # 투포인터?
    # s, e
    # k개 이상 상태 확인
    # 아직 k개보다 작으면
    # 기본은 e 증가

    # k개 이상이면
        # s증가
        # min계속 갱신, k조건을 만족하므로 

s, e = 0, 0
lion_cnt = 0
min_len = sys.maxsize

if _list[s] == 1:
    lion_cnt += 1
# if _list[e] == 1:
#     lion_cnt += 1
    
while s <= e:
    # print(s, e, lion_cnt, min_len)
    if lion_cnt < K:
        e += 1
        if e == len(_list):
            break

        if _list[e] == 1:
            lion_cnt += 1
    else:
        min_len = min(min_len, e - s + 1)
        if _list[s] == 1:
            lion_cnt -= 1
        s += 1

if min_len == sys.maxsize:
    min_len = -1

print(min_len)