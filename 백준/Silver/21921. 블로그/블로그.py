# 1초 / 512MB
# 23.05.31
# 15:00 ~ 

# 블로그시작 N일
# X일동안 가장 많이 들어온 방문자 수, & 기간을 알려고 함

# Output
    # 방문자수, 그 기간의 갯수 

N, X = map(int, input().split())

# **1일부터**
_list = list(map(int, input().split()))
_list.insert(0, 0)

# Exception: 최대 방문자수가 0 -> SㅇAD출력 
# 그게 아니라면, 둘째줄에 기간을 출력

for i in range(1, N+1):
    _list[i] += _list[i-1]

# X일 계산
ans_val = 0
ans_len = 0

for i in range(X, N+1): # i = 2, 3, 4
    tmp = _list[i] - _list[i-X]

    if ans_val < tmp:
        ans_val = tmp
        ans_len = 1
    elif ans_val == tmp:
        ans_len += 1

if ans_val == 0:
    print("SAD")
else:
    print(ans_val)
    print(ans_len)
