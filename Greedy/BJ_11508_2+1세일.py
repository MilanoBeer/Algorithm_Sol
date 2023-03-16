import sys
input = sys.stdin.readline

N = int(input())
price_l = []
for i in range(n):
    price_l.append(int(input()))

# 비싼 것부터 앞에 나와야, 묶음이 되는 세가지중 제일 저렴해서 빠지는 물건이 비싼물건이 된다. 
# ***** revers 내림차순으로 해야 이득인데, 오름차순으로 정렬했다.. 
# ***** 저렴하려면, 큰 값이 빠져야 이득..!
price_l.sort(reverse=True)
sum = 0
for i in range(N):
    if i % 3 != 2:
        sum += price_l[i]

print(sum)