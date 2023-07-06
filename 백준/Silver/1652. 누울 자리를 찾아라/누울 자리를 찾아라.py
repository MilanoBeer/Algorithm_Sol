# 2초 / 128MB
# 10: 24 ~ 

# N * N

N = int(input())

mat = [list(input()) for _ in range(N)]

h_cnt = 0
v_list = [0] * (N)
hori, verti = 0, 0

for r in range(N):
    h_cnt = 0
    for c in range(N):
        if mat[r][c] == '.':
            h_cnt += 1
            v_list[c] += 1

        elif mat[r][c] == 'X':
            # x로 끊겼을 때, 현재까지 h_cnt가 2이상이면, 
            if h_cnt >= 2:
                hori += 1
            h_cnt = 0

            if v_list[c] >= 2:
                verti += 1
            v_list[c] = 0
    if h_cnt >= 2:
        hori += 1
for v in v_list:
    if v >= 2:
        verti += 1
print(hori, verti)
