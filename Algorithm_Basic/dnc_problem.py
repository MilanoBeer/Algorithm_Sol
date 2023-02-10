import sys
sys.setrecursionlimit(1000)

'''
input > 
9
0 0 0 1 1 1 2 2 2
0 0 0 1 1 1 2 2 2
0 0 0 1 1 1 2 2 2
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 2 0 1 2 0 1 2
0 2 1 0 2 1 0 2 1
1 1 1 0 1 1 2 2 2
'''

f = open("problem_input.txt", "r")
n = int(f.readline()) # 동물원 크기

# n만큼 array 입력받기 
mat = [ list(map(int, f.readline().split())) for _ in range(n)]
visited = [ [False] * n for _ in range(n)]

count = 0
def fence(size, left, right, top, bottom):
    global count
    flag = False
    # terminal condition 
    if size == 1:
        return 
    # else     
    # init pivot, index
    pivot = mat[top][left]
    # print("/// left :", left, "right: ", right, "top: ", top, "bottom: ", bottom)
    for i in range(top, bottom):
        for j in range(left, right):
            # pivot과 다르고, 해당 영역을 아직 검사 안했을 때만
            if mat[i][j] != pivot and visited[i][j] is False: 
                # 현재 size에서, 아직 count안했을때만 count하기 
                if flag is False:
                    flag = True
                    count += 1
                visited[i][j]= True
                # call recursive # left, right, top, bottom 
                # 원소들의 i, j값에 따라 정해진 영역안에서 호출 : [6][1] -> row : 6 - 9 / col : 0 - 3
                new_left = (size//3 * (j//3)) 
                new_right = (size//3 * (j//3 + 1)) 
                new_top = (size//3 * (i//3))
                new_bottom = (size//3 * (i//3 + 1))
                fence(size//3, new_left, new_right, new_top, new_bottom)
            else:
                visited[i][j] = True

fence(n, 0, n, 0, n) # n: 9
print(count)