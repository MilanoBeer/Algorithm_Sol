# 15:16 ~ 

# *** Solution 
# 테케마다 값을 출력해야 한다 
# -> 미 피보나치 숫자 리스트를 만들어둘 것

import sys
def input():
    return sys.stdin.readline().rstrip()

# - 피보나치 숫자 리스트 목록 만들기
fibo = [0, 1]
a = 0
b = 1

while True:
    # 만들다가 마지막으로 추가한 숫자가 1,000,000,000이상이면 그만 
    tmp = a + b
    fibo.append(tmp)
    b = a
    a = tmp

    if a > 1000000000:
        break 

T = int(input())

for t in range(T):
    n = int(input())
    # 선언 : 합을 이루는 숫자리스트 배열
    _eles = []

    # while n
    while n != 0:
        # n이랑 같거나, 보다 작은 피보나치수면 _eles에 추가
        # n의 범위도 감소해주기 -> n - 원소
        for i in range(len(fibo)-1, -1, -1):
            if fibo[i] <= n:
                _eles.append(fibo[i])
                n -= fibo[i]
            if n == 0:
                break

    # Output
    _eles.reverse()
    print(*_eles)
