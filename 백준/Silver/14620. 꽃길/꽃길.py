# 2초 / 256MB
# 4:35 ~ 
# 씨앗이 3개 -> 세개 꽃 모두 1년후 만개

# NxN
# 세개 모두 피면서 & 가장 싼 가격

# 대여가격 : 꽃 하나당 -> 5칸(평)

# Output : 꽃을 심기 위해 필요한 최소비용
from itertools import product, combinations
# N : 6이상 10이하 
N = int(input())
# 화단 지점당 가격
mat = [list(map(int, input().split())) for _ in range(N)]

# Solution 
# mat에서 3개 고르기 
# 중복조합으로, 행/열 뽑기 
row_col = list(product(list(range(1, N-1)), repeat=2))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
min_price = 999999999
def check(case):
    global min_price
    visited = [[0] * N for _ in range(N)]
    tmp_price = 0
    # case : 1, 2, 3돌면서 visited
    for r, c in case:
        # print(r, c)
        visited[r][c]= 1
        tmp_price += mat[r][c] 

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]  

            # 방문체크
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                tmp_price += mat[nr][nc]
            # 이미 방문되어있으면, 겹치는 경우 -> return 
            else:
                return 
        
    # return 되지 않았으면, 안 겹치는 경우 
    # 비용 갱신하기
    min_price = min(min_price, tmp_price)

for case in combinations(row_col, 3):
    # 해당 case에 대해 확인하기
    check(case)

print(min_price)
