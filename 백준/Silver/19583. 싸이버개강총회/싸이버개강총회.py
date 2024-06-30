# 14:05 ~ 

# 1트: dictionary 
from collections import defaultdict 
import sys
def input():
    return sys.stdin.readline().rstrip()

# 분으로 시간변환해서 다루기 
def cal_time(data):
    hour, minu = map(int, data.split(":"))
    return 60 * hour + minu

ans = 0
dd = defaultdict(int)
S, E, Q = input().split()

S = cal_time(S)
E = cal_time(E)
Q = cal_time(Q)

while True:
    try:
        data = input()
        time, nick = data.split()
        time = cal_time(time)

        if time <= S:
            dd[nick] = 1

        if E <= time <= Q and dd[nick] == 1:
            dd[nick] += 1
            ans += 1
    except:
        break
# print(dd)
print(ans)