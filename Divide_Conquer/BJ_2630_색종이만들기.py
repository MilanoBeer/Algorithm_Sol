N = int(input())

mat = [ list(map(int, input().split())) for _ in range(N)]

# 흰색, 파란색 카운트 
white_cnt = 0
blue_cnt = 0

# Function > 
def dnc(N, fr, to):
    global white_cnt
    global blue_cnt
    # terminal condition 
    if N == 1:
        if mat[fr[0]][fr[1]] == 1:
            blue_cnt += 1
        else:
            white_cnt += 1
        return 
    
    # 영역안에 한가지 색깔로 이루어졌는지 확인하기
    pivot = mat[fr[0]][fr[1]]

    for i in range(fr[0], to[0] + 1):
        for j in range(fr[1], to[1] + 1):
            if pivot != mat[i][j]:
                unit_size = N//2
                # 4등분하기 
                dnc(N//2, fr, (fr[0] + unit_size -1, fr[1] + unit_size-1))
                dnc(N//2, (fr[0], fr[1] + unit_size), (fr[0] + unit_size -1, to[1]))

                dnc(N//2, (fr[0] + unit_size, fr[1]), (to[0], fr[1] + unit_size -1))
                dnc(N//2, (fr[0] + unit_size, fr[1] + unit_size), to)
                return 2
            
    if pivot == 1:
        blue_cnt += 1
    else:
        white_cnt += 1

dnc(N,(0, 0), (N-1, N-1))
print(white_cnt)
print(blue_cnt)