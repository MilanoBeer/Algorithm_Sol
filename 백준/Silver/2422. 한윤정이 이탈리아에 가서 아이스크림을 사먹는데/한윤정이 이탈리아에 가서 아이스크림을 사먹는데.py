 # 1초 / 128MB 
# 7: 20 ~ 
# N종류의 아이스크림 / 1번 ~ 

# 특정 조합을 피해서 먹으려고 함
# 3가지 선택
from itertools import combinations

# N종류 : 1이상, 200이하 / M : 먹으면 안되는 조합의 갯수 : 0이상, 10,000이하 
N, M = map(int, input().split())

# M종류 
visited = [[0] * (N+1) for _ in range(N+1)]
for m in range(M):
    v, u = map(int, input().split())
    visited[v][u] = 1
    visited[u][v] = 1

# Solution 
    # -> dic활용
glo_ans_cnt = 0
# 선택하고 나서 -> M개의 리스트에 있는지 확인하자
def check(case):
    global glo_ans_cnt
    a, b, c = case
    # case의 각 아이스크림 번호에 대해
    if visited[a][b] == 0 and visited[a][c] == 0 and visited[b][c] == 0:
        glo_ans_cnt += 1
            
ice = list(range(1, N+1))
for case in combinations(ice, 3):
    # IDEA : N에서 3개 뽑기 -> 200_C_3 -> 200.199.198 // 6 -> 8백만
    check(case)

# Output > 선택할 수 있는 방법의 수 
print(glo_ans_cnt)

