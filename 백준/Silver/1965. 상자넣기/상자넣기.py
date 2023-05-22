# 2초 / 128MB
# 23.05.22 
# 18:02 ~ 18:40 

# 상자의 크기가 주어질 때, 한번에 넣을 수 있는 최대상자의 갯수

# 상자의 갯수 / 1이상, 1000이하 
n = int(input())

_list = list(map(int, input().split())) # 크기는 1000이하 자연수 

dp = [1] * (n)

for i in range(1, n):
    # [i]이전 값들에 대해, [i]보다 작으면 비교대상
    for j in range(i):
        if _list[j] < _list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))