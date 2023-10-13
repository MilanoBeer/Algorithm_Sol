# 23.10.13 / 15:48 ~ 
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]
# minus, zero, one = 0, 0, 0

# def : d&c
def dnc(left, top, size): # 범위, 사이즈
    # print(left, top, size)
    pivot = mat[top][left]
    isDivide = False

    if size == 1:
        ans[pivot] += 1
        return 

    for i in range(top, top + size):
        for j in range(left, left + size):
            if mat[i][j] != pivot:
                isDivide = True
                break 
    
    if isDivide:
        size = size // 3
        
        # 해당 구역 9등분
        dnc(left, top, size)
        dnc(left + size, top, size)
        dnc(left + 2*size, top, size)

        dnc(left, top + size, size)
        dnc(left + size, top + size, size)
        dnc(left + 2*size, top + size, size)


        dnc(left, top + 2*size, size)
        dnc(left + size, top + 2*size, size)
        dnc(left + 2*size, top + 2*size, size)
    else:
        # pivot으로만 채워진 영역임
        ans[pivot] += 1

    return 

dnc(0, 0, N)
print(ans[-1])
print(ans[0])
print(ans[1])
# print(minus)
# print(one)
# print(zero)