# 2초 / 128MB
# 18:50 ~ 

# 행렬A -> B로 바꾸는데 필요한, "연산의 횟수"
# 같은 크기

N, M = map(int, input().split())

n_mat = [list(map(int, input())) for _ in range(N)]
m_mat = [list(map(int, input())) for _ in range(N)]

# Solution 
def reverse(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if n_mat[i][j] == 0:
                n_mat[i][j] = 1
            else:
                n_mat[i][j] = 0

reverse_cnt = 0
# n_mat Traversal : n_mat을 바꾸고, 비교하기 
# for : 디폴트가 3x3 경계값 주의 
for r in range(0, N-2):
    for c in range(0, M-2):
    # if r,c == m의 r, c
        if n_mat[r][c] != m_mat[r][c]:
        # 뒤집기 -> 함수 만들어서 호출하기 
        # 뒤집기 필요한거 -> 뒤집을 영역 -> 
            reverse(r, c)
            reverse_cnt += 1
# output 
# EXCEPTION : 바꿀 수 없으면 - 1 -> 바꿀 수 없다고 판단하느 기준은?
# 모두 바뀌었는지 전체 확인
for r in range(N):
    for c in range(M):
        if n_mat[r][c] != m_mat[r][c]:
            print(-1)
            exit(0)
print(reverse_cnt)



