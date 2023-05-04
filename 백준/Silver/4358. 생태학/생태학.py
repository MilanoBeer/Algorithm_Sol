# 1초 / 256MB
# 11:18 ~ 

# 각 나무종류가 , 전체에서 몇 프로 차지하는지 

# 나무종 이름 최대 30글자
import sys
from collections import Counter, defaultdict    
input = sys.stdin.readline

# Solution 
# Counter
data_list = []
dic = defaultdict(int)
tot_input = 0
while True:
    tree_data = input().rstrip()
    # terminal condition 
    if not tree_data:
        break 

    # dictoinary 추가 
    dic[tree_data] += 1
    tot_input += 1

# 정렬 
data_list = list(dic.keys())
data_list.sort()

# output
# 이름을 사전순으로 출력 / 종이 차지하는 비율 
for t in range(len(data_list)):
    print('%s %.4f' %(data_list[t], dic[data_list[t]] / tot_input *100))
