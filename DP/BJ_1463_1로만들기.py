N = int(input())
if N == 1:
    print(0)
    exit(0)

DP = [0] * (N+1)
next_list = []

# init
if N % 3 == 0:
    DP[N//3] = 1
    next_list.append(N//3)
if N % 2 == 0:
    DP[N//2] = 1
    next_list.append(N//2)
DP[N-1] = 1
next_list.append(N-1)

while next_list:
    cur_pos = next_list.pop(0)

    if cur_pos == 1:
        break 
    
    if cur_pos % 3 == 0 and DP[cur_pos//3] == 0:
        DP[cur_pos//3] = DP[cur_pos] + 1
        next_list.append(cur_pos//3)
    if cur_pos % 2 == 0 and DP[cur_pos//2] == 0:
        DP[cur_pos//2] = DP[cur_pos] + 1
        next_list.append(cur_pos//2)
    if DP[cur_pos -1] == 0:
        DP[cur_pos -1] = DP[cur_pos] + 1
        next_list.append(cur_pos-1)
    
print(DP[1])