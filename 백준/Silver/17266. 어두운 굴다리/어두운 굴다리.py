# 12:41 ~ 13:00 틀림 / 

# 최소한의 높이로, 모든 길을 밝히기 
# 가로등의 모든 높이는 같다 , 정수 
# 높이 H -> 왼, 오H

N = int(input())
M = int(input())
_pos = list(map(int, input().split()))

max_val = 0

for i in range(1, M):
    max_val = max(max_val, _pos[i] - _pos[i-1])

# max_val = max(_pos[0], N - _pos[-1])
if max_val % 2 == 0:
    max_val //= 2
else:
    max_val = (max_val//2) + 1
ans = max_val 

if _pos[0] > ans:
    ans = _pos[0]
if (N-_pos[-1]) > ans:
    ans = N - _pos[-1]

print(ans)