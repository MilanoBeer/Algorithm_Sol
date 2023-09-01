# 14:39 ~
# 생각하기..
    # 완탐? -> 
    # 그리디?
from collections import deque
import sys

data = list(input())
start = 0
idx = 0
# data의 모든 숫자를 처리할 때 까지
while idx < len(data):
    # start를 1씩 증가시키기
    start += 1
    temp = str(start)

    # 증가시킨 start에서, data의 숫자들이 있는지 하나씩 확인하기
    for i in range(len(temp)):
        # 일치하는게 있으면 -> data의 포인터 앞으로
        if temp[i] == data[idx]:
            idx += 1
        if idx == len(data):
            break 
print(start)