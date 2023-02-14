from typing import Tuple

N = int(input())
# N x N 크기
mat = [list(map(int, input().split())) for _ in range(N)]
# 원소 : -1 or 0 or 1
cnt_dict = {-1:0, 0:0, 1:0}

def dnc(N, fr, to):
    # terminal condition 
    if N == 1:
        cnt_dict[mat[fr[0]][fr[1]]] += 1
        return 

    # 만약 종이가 모두 같은 수로 되어 있으면, 분할하지 않음
    pivot = mat[fr[0]][fr[1]]
    unit_size = N//3 
    # traversal
    for i in range(fr[0], to[0] + 1):
        for j in range(fr[1], to[1] + 1):
            if mat[i][j] != pivot:
                # 9등분하기 
                dnc(N//3, (fr[0], fr[1]), (fr[0] + unit_size - 1, fr[1] + unit_size -1)) 
                dnc(N//3, (fr[0], fr[1] + unit_size), (fr[0] + unit_size -1, fr[1] + unit_size*2 -1)) 
                dnc(N//3, (fr[0], fr[1] + unit_size * 2), (fr[0] + unit_size -1, fr[1] + unit_size*3 -1))

                dnc(N//3, (fr[0] + unit_size, fr[1]), (fr[0] + unit_size *2 - 1, fr[1] + unit_size -1)) 
                dnc(N//3, (fr[0] + unit_size, fr[1] + unit_size), (fr[0] + unit_size *2 - 1, fr[1] + unit_size*2 -1)) 
                dnc(N//3, (fr[0] + unit_size, fr[1] + unit_size*2), (fr[0] + unit_size *2 - 1, fr[1] + unit_size*3-1)) 
                    
                dnc(N//3, (fr[0] + unit_size*2, fr[1]), (fr[0] + unit_size*3 -1, fr[1] + unit_size -1))
                dnc(N//3, (fr[0] + unit_size*2, fr[1] + unit_size), (fr[0] + unit_size*3 -1, fr[1] + unit_size*2 -1))
                dnc(N//3, (fr[0] + unit_size*2, fr[1] + unit_size * 2), (fr[0] + unit_size*3 -1, fr[1] + unit_size*3 -1))

                return

    # if문에 들어가서 나눠지지 않았다면, pivot값을 그대로 증가시키기 
    cnt_dict[pivot] += 1

dnc(N+1, (0, 0), (N-1, N-1))
print(cnt_dict[-1])
print(cnt_dict[0])
print(cnt_dict[1])