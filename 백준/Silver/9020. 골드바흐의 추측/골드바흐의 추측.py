# 2초 / 256MB
# 23.05.18
# 15:33 ~ 15: 45 / 16:00 ~ 
# 소수 / 5 -> 1, 5
# 골드바흐수 정의 
    # 2보다 큰 모든 짝수 <- 두 소수의 합
# 골드바흐 파티션
#input
T = int(input()) # 

def check(num):
    for i in range(2, num//2 + 1):  # num//2까지 검사
        if num % i == 0:
            return False
    return True

_list = []
for i in range(2, 10001):
    # 소수 판정
    if check(i):
        _list.append(i)

for t in range(T):
    n = int(input()) # 2보다 큰 짝수 / 
    # 10,000보다 작은 모든 소수를 미리 수집? 
    #     2, 3, 5, 7, /  11, 13, 17,/  23, 29, / 31, 37, / 41, 43, 47, ..  ... 

    # 8 <- 8보다 작은 두개의 소수로 이루어짐
    # 10 <- 10보다 작은 두개의 소수로 ... 
    # 일단 1~10,000까지 순회하면서 소수리스트 생성하기 
    s = 0
    e = 0
    for i in range(len(_list)):
        if _list[s] + _list[e] == n:
            print(_list[s], _list[e])
            break 
        elif _list[s] + _list[e] < n:
            s += 1
            e += 1
        else:
            s -= 1

    # 리스트에서, 8의 후보가 될 수 있는 범위 좁히기.. 
    #     이진탐색 -> if 8이 더 크면, 종료 
    #     거기서 2개 뽑기? 
    # 2, 3 ->

    # output: 골드바흐 파티션 출력
    # a, b 두개 출력 / 작은것부터 출력 