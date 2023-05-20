# 1초 / 256MB
# 23.05.20
# 10:56 ~ 11:23 / 

# 자연수 n 
# n초과, 2n이하 소수 하나는 존재

# output : n이 주어졌을때, 2n범위에서 소수의 갯수

import sys
input = sys.stdin.readline

# 처음부터 구하기
_dec_list = [0] * 246913
for i in range(2, 246913): # **** !!! 
    flag = True
    for j in range(2, int(i**0.5) + 1): # *** !!!! 
        if i % j == 0:
            flag = False
            break 
    if flag:
        _dec_list[i] = 1
    
# 누적
for i in range(1, 246913):
    _dec_list[i] += _dec_list[i-1]

while True:
    n = int(input())

    if n == 0:
        break 

    print(_dec_list[2*n] - _dec_list[n])