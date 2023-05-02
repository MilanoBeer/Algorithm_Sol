'''
23.05.02
12:20 ~ 
'''
# Error : 58% 에서 틀림 / 
# 1초 / 256MB

# N : 수열A의 크기 / 1이상, 1000이하 
N = int(input())
_list = list(map(int, input().split()))

# Solution 
# DP[i] : [i]까지 포함해서, 가장 길게 감소하는 수열의 갯수 
    # [i]까지 오면서 감소하기 -> [i]앞에, 더 큰값들이 있어야함
DP = [1] * (N)

# for i in range(N):
#     for j in range(i, N):
#         if _list[i] > _list[j]:
#             DP[j] = DP[i] + 1 

# 뒤에서부터 
# i의 앞에 더 큰 값들의 갯수를 카운트 
for i in range(N-1, 0, -1):
    for j in range(i-1, -1, -1):
        if _list[j] > _list[i]:
            DP[j] = max(DP[j], DP[i] + 1)
    # print(DP)
# Output : 수열의 가장 "긴" 감소하는 부분 수열 구하기 
print(max(DP))


