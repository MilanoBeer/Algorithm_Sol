# 2초 / 128MB

# 23.05.30
# 22:30 ~ 

import sys
input = sys.stdin.readline

# N: 1이상, 20만이하 / K : 20억 이하 
N, K = map(int, input().split())

# N개의 정수 
_list = list(map(int, input().split()))

# 가능한 모든 합 
# **** O(n^2) 은 초과 => 줄이는 방법 **** => 딕셔너리
dic = dict()
# dic[0] = 1
sum_val = 0
ans_cnt = 0

dic[0] = 1

for i in range(N):
    sum_val += _list[i]

    # key확인
    if sum_val - K in dic.keys():
        # 있으면 
        # print("i :", _list[i], "i : ", i)
        ans_cnt += dic[sum_val-K]
    if sum_val in dic.keys():
        dic[sum_val] += 1
    else:
        dic[sum_val] = 1

# OUTPUT: 합이 K인 부분합의 갯수 
print(ans_cnt)

