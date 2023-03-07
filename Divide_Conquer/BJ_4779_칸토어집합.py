# 칸토어 집합 > 0과 1사이의 "실수"들로 이루어진 집합 
import sys
sys.setrecursionlimit(10**6)

def divide_and_cut(start, end):
    # terminal condition #
    if start == end:
        print("-", end='')
        return 

    # recursive, divide # 
    else:
        unit_size = (end - start) // 3
        divide_and_cut(start, start + unit_size)
        # do > 공백영역 출력 
        for i in range(start + unit_size +1, end-unit_size):
            print(" ", end='')

        divide_and_cut(end-unit_size, end)
        return

# condition > 파일의 끝에서 입력 멈추기
while True:
    try:
        N = int(input())
        size = pow(3, N)

        divide_and_cut(0, size-1)
        print()
    # 파일의 끝 처리 
    except EOFError:
        break 