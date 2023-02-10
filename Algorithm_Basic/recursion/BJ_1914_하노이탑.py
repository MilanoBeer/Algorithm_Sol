# 첫번재 장대에 쌓인 원판의 갯수 ( 1 <= N <= 100) 
N = int(input())

move_list = []
cnt = 0

def hanoi(n, fr, to, other): 
    # terminal condition 
    if n == 1: 
        if N <= 20:
            print(fr, to)
    else:
        # n-1개의 기둥을 other로 옮기기 
        hanoi(n-1, fr, other, to) 
        if N <= 20:
            print(fr, to)
        hanoi(n-1, other, to, fr)

if N > 20:
    print(pow(2, N)-1)
    exit(0)
else:
    print(pow(2, N)-1)
    hanoi(N, 1, 3, 2)

