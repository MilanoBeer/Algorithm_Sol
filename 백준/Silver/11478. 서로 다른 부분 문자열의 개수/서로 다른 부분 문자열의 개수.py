# 1초 / 512MB
# 10:51 ~
from itertools import permutations

# 1000이하
str_data = input() # list(input())은 타입에러 발생
ans_list = set()

for i in range(len(str_data)):
    # a, b, c / ab, ba, bc / aba, bab, abc / abab, babc / ababc 
    for j in range(i, len(str_data)):
        ans_list.add(str_data[i:j+1])
print(len(ans_list))