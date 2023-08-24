# 23.08.24 / 17:05 ~

from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

# 차선변경 불가, 추월불가 => 순서 지키지
    # -> 큐, 스택? 

# 입구, 출구 => deque
# 대근 : 입구, 들어가는 순서대로 기록
# 영식 : 출구, 나오는 순서대로 기록

N = int(input()) # 1000이하 
in_q = deque()
out_q = deque()
ans = 0
# 들어가는
for n in range(N):
    in_q.append(input())
    
# 나오는
for n in range(N):
    out_q.append(input())

while True:
    inout = in_q.popleft()

    if inout not in out_q:
        continue

    while out_q and inout != out_q[0]:
        out_q.popleft()
        ans += 1
    out_q.popleft()

    if not out_q:
        break 

 # output> 추월한 차량? 
print(ans)