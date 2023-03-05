# N 명, 짝수 / 4이상 20이하 
# N/2 나누기 
# purpos > 두 팀의 능력치 합의 차이를 최소화 
# answer > 최솟값을 출력

from itertools import combinations, permutations
from math import factorial

N = int(input())
mat = [ list(map(int, input().split())) for _ in range(N)]

n_l = list(range(N))
size = N//2

# 조합 경우의 수 계산
combi_num = factorial(N) // (factorial(N-size) * factorial(size))
combi_num //= 2
num_idx = 0
answer = 20001 # 최댓값으로 초기화 

# Def > visited배열을 확인해서 링크팀 생성 후 반환 
def find_link_team(visited):
    link_l = []
    for i in range(N):
        if visited[i] is False:
            link_l.append(i)
    return link_l

for case in combinations(n_l, size):
    # 매 case마다 갱신 
    visited = [False] * N
    link_team_score = 0
    start_team_score = 0

    # start 팀으로 처리 
    for i in case: 
        visited[i] = True

    # 스타트팀 능력치 계산
    for permu_case in permutations(case, 2):
        start_team_score += mat[permu_case[0]][permu_case[1]]

    # 링크팀 만들어서, 능력치 계산 
    link_team = find_link_team(visited)
    for permu_case in permutations(link_team, 2):
        link_team_score += mat[permu_case[0]][permu_case[1]]
    answer = min(answer, abs(start_team_score - link_team_score))  
    
    # 반만 계산하면 모든 경우가 고려됨,
    num_idx += 1
    if num_idx == combi_num:
        break 

print(answer)