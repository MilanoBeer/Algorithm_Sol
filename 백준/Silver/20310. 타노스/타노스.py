# 19:26 ~

from collections import Counter

data = list(input())

# 0, 1의 갯수 카운트하기
zero = data.count('0')
one = data.count('1')

zero //= 2
one //= 2

ans = '0'*zero + '1'*one
print(ans)