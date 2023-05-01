# 2초 / 128MB

# 3:35 ~ 

# 임의의 두 부분 골라서 쪼개기 -> 3영역
# 각각 적어도 1이상이어야 한다 
# 각각 앞뒤 뒤집 -> 합치기 

# Output : 사전 순, 가장 앞서는 단어 출력
from itertools import combinations

# 3이상, 50이하 
S = input()

# 고를 수 있는 두 영역
# abc - 012 ->
# 1, 2 ==> [0:1] / [1:2] / [2:]
_list = list(range(1, len(S)))
ans_list = []
for case in combinations(_list,2):
    # 뽑아서, 세 구역 나누기 & 뒤집기 
    str_a = S[:case[0]][::-1]
    str_b = S[case[0]:case[1]][::-1]
    str_c = S[case[1]:][::-1]

    tmp_str = str_a + str_b + str_c    
    ans_list.append(tmp_str)

ans_list.sort()
print(ans_list[0])