# 2초 / 256MB
# 23:50 ~ 
# B - > A 

A, B = map(int, input().split())
m = int(input())
_data = list(map(int, input().split()))

# A진법의 수 -> 10진법 -> B진법
# 1 3
# 1*(10^1) + 3*(10^0) => 13

# 2 16
# 2*(17*1) + 16*(17*0) =. 50
tmp = 0
for i in range(len(_data)):
    tmp += _data[i] * (A**(m - 1 - i))

result = []
while tmp != 0:
    result.append(tmp%B)
    tmp //= B

result.reverse()
print(*result)