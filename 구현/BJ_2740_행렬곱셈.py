

N, M = map(int, input().split())
mat_A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
mat_B = [list(map(int, input().split())) for _ in range(M)]

mat_C = [[0]*K for _ in range(N)]

for k in range(0, N):
    for i in range(0, M):
        for j in range(0, K):
            mat_C[k][j] += mat_A[k][i] * mat_B[i][j]

for i in range(N):
    for j in range(K):
        print(mat_C[i][j], end=" ")
    print()