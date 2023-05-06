# 2초 / 128MB

# 23.05.06
# 11:45 ~ 12:15

# 사람 : 1번 ~ N번

# 주어진 체력내에서 -> 최대의 기쁨
# 체력 : 100 

import sys
input = sys.stdin.readline

# N : 사람 수 / 20이하 
N = int(input())

# 인사할 때 잃는 체력
hp_list = list(map(int, input().split()))

# 얻는 기쁨
joy_list = list(map(int, input().split()))

# Solution 
# DS : 리스트 
# 체력이 더 작고, 기쁨은 더 많도록 

# GLOBAL : 최대 기쁨 변수 
max_joy = 0

# 재귀에서 바뀌는 값: 체력, 기쁨, 끝까지 갈 경우 카우느 
def recursive(idx, hp, joy, cnt): 
    global max_joy

    
    # terminal conditoin 
    if cnt == N:
        max_joy = max(max_joy, joy)
        return 

    # call 
    # 체력이 한도 안이면
    if hp + hp_list[idx] < 100:
        recursive(idx+1, hp + hp_list[idx], joy + joy_list[idx], cnt + 1)
    recursive(idx+1, hp, joy, cnt + 1)
        # 한도 밖이면, 현재 값으로 max_joy갱신
        # max_joy = max(max_joy, joy)

recursive(0, 0, 0, 0)
print(max_joy)