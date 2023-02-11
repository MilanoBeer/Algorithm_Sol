# 흰점 : 0 / 검은 점 : 1
N = int(input())

# 영상정보, 공백없이
mat = [ list(map(int, input())) for _ in range(N)]
visited = [ [False]*N for _ in range(N)]

# 섞여있으면, 사등분해야함
def dnc(N, left, right, top, bottom):
    flag = True
    # terminal condition 
    if N == 1:
        print(mat[top][left], end='')
        visited[top][left] = True # 이때도 방문 표시 해야 한다!!!!!! 
        return
    # else > init pivot & traversal 
    pivot = mat[top][left] # pivot 값은 왼쪽 상단으로 고정
    for i in range(top, bottom):
        for j in range(left, right):
            # 현재 영역에서 pivot과 다른 값이 섞여잇으면 -> 4등분 하기
            if mat[i][j] != pivot and visited[i][j] is False:
                print("(", end='') # 새로 4등분이 시작
                flag = False
                dnc(N//2, left, left + N//2, top, top + N//2)
                dnc(N//2, left + N//2, right, top, top + N//2)
                dnc(N//2, left, left + N//2, top + N//2, bottom)
                dnc(N//2, left + N//2,right, top + N//2, bottom)
                print(")", end='') # 4등분 끝 괄호
            else:
                visited[i][j] = True
    if flag is True:
        print("{0}".format(pivot), end='')
        
dnc(N, 0, N, 0, N)
print()