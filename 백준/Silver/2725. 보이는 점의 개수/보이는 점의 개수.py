# 1초 / 128MB
# 23.06.01 
# 17:50 ~ 18:55

T = int(input()) # T개수 

# N이 최대 1000
dp = [0] * 1001
dp[1] = 3

# 기울기가 유일한 점들을 카운트하기 *** 
def gcp(i, j):
    if j == 0:
        return i 
    return gcp(j, i % j)

for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        # 초기값 dp[1]때문에 무조건 continue
        if i == j:
            continue
        if gcp(i, j) == 1:
            cnt += 2
    dp[i] = dp[i-1] + cnt 

for t in range(T):
    N = int(input()) 
    
    # OUTPUT
    print(dp[N])
    