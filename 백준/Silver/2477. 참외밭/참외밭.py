# 1초 / 128MB
# 10시 25분 ~ 
# 1cm2 참외 갯수 -> 참외밭의 넓이를 구하면 -> 비례식을 이용해 참외의 총갯수를 구할 수 있음
from itertools import count
# K : 참외갯수 / 1이상 20이하 
K = int(input())

# 육강형 정보 
w_list = []
h_list = []
total_list = [] # 전체를 담는 정보도 필요하다! 순서가 포함되니까
for i in range(6):
    # 변의 방향 / 길이 
    # 동쪽 : 1 / 서쪽 : 2 / 남쪽 : 3 / 북쪽 : 4 
    dir, len = map(int, input().split())

    # 가로, 세로 따로 모으기
    if dir == 1 or dir == 2:
        w_list.append(len)
        total_list.append(len)
    else:
        h_list.append(len)
        total_list.append(len)

max_w = max(w_list)
max_h = max(h_list)

# 전체 사각형 구하기
total_area = max_w * max_h

# 작은 사각형의 가로 , 세로 구하기
max_h_idx = total_list.index(max_h)
max_w_idx = total_list.index(max_w)

small_h = abs(total_list[(max_h_idx + 1) % 6] - total_list[(max_h_idx - 1)% 6])
small_w = abs(total_list[(max_w_idx -1) % 6] - total_list[(max_w_idx + 1)%6])

print((total_area - (small_h * small_w)) * K)




# Output : 전체밭에서 자라는 참외 수 
# 참외갯수 K * 참외면적



