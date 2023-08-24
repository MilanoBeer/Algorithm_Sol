# 23.08.24 / 17:42

S1 = input()
S2 = input()

# A
    # C
    # CA
    # CAP .. 
mat = [[0] * (len(S2)+1) for _ in range(len(S1) + 1)]
# for S1
    # for S2
        # 비교, 최장길이 갱신 
# 2차원 배열

# for 
    # for
        # 추가된 끝자리 확인
            # 같으면

            # 다르면

for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        if S1[i-1] == S2[j-1]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            mat[i][j] = max(mat[i][j-1], mat[i-1][j])

print(mat[-1][-1])