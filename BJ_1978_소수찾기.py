# BJ_1978_소수찾기

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


N = int(input())
list = []
list = map(int, input().split())

cnt = 0
for i in list :
    # 각 원소 i에 대해 소수 여부 판별
    res = isPrime(i)
    if res :
        cnt += 1

print(cnt)
