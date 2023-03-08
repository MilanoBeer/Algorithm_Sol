# 구하려는 값 ? 
    # 현재 계단 위치에서(밟거나 or 밟지 않거나 ), 최대가 되는 누적합 
    # DP 테이블 : 현재 계단위치에서 최대가 되는 누적합값 

# 특정상황에서 선택 가능한 경우는 무엇이 있나? 
    # 현재 계단위치를 밟거나 밝지 않거나 
    # 단, 밝을 수 없을 경우는 고려대상에서 제외 

N = int(input()) # 계단의 갯수 
DP = [0] * (N)
n_l = []

# input data 
for i in range(N):
    n_l.append(int(input()))

if len(n_l) <= 2:
    print(sum(n_l))
else:
    # 도출할 수 있는 현재 값
    DP[0] = n_l[0]
    DP[1] = n_l[0] + n_l[1]
    # DP[2] = max(DP[0] + n_l[2], n_l[1] + n_l[2], DP[0] + n_l[1])
    DP[2] = max(DP[0] + n_l[2], n_l[1] + n_l[2])
    for i in range(3, N):
        DP[i] = max(DP[i-2] + n_l[i], DP[i-3] + n_l[i-1] + n_l[i])

    print(DP[-1])