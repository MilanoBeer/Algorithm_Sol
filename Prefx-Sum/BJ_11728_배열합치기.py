import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 1이상, 백만이하 

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
result_list = [0] * (N+M)

def merge_sorting():
    a_left = 0; a_right = N-1
    b_left = 0; b_right = M-1
    res_idx = 0

    while a_left <= a_right and b_left <= b_right:
        if A_list[a_left] < B_list[b_left]:
            result_list[res_idx] = A_list[a_left]
            a_left += 1
            res_idx += 1
        else:
            result_list[res_idx] = B_list[b_left]
            b_left += 1
            res_idx += 1
    # Do > remain element
    while a_left <= a_right:
        result_list[res_idx] = A_list[a_left]
        a_left += 1
        res_idx += 1
    while b_left <= b_right:
        result_list[res_idx] = B_list[b_left]
        b_left += 1
        res_idx +=1 

merge_sorting()
print(' '.join(map(str, result_list)))


    