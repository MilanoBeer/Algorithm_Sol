# 2초 / 512MB
# 23.06.09
# 10:00 ~ 

# 1이상, 20이하 
S = int(input()) 
_list = list(map(int, input().split()))
# _list.insert(0, 0)

visited = [0] * (S+1)
_sum_list = [0] * (20000001)

def dfs(idx, _sum, cnt):
    # TERMINAL
    if cnt == S:
        return 
    
    for i in range(idx, S):
        if visited[i] == 0: # 아직 방문한 숫자가 아니면, + 
            visited[i] = 1
            tmp = _sum + _list[i]

            _sum_list[tmp] = 1

            dfs(i, _sum + _list[i], cnt + 1)
            visited[i] = 0

dfs(0, 0, 0)

for i in range(1, 20000001):
    if _sum_list[i] == 0:
        print(i)
        break 