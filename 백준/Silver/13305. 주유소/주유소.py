# N개의 도시 , 일직선 수평 위 
# 제일 왼쪽 도시 -> 제일 오른쪽 도시로 이동

# Condition 
    # 출발할 때 기름 넣고 출발
    # 1km당 1리터 
    # 각 도시에는 단 하나의 주유소 
        # 도시마다 주유소의 리터당 가격은 다를 수 있음 
# Answer
    # 이동하는 최소비용 

N = int(input())
dist_l = list(map(int, input().split())) # N-1개 
cost_l = list(map(int, input().split())) # N개

cost = dist_l[0] * cost_l[0] # 출발을 위한 최소비용 
min_cost = cost_l[0]

for i in range(1, N-1):
    if cost_l[i] < min_cost:
        min_cost = cost_l[i]
    
    cost += min_cost * dist_l[i]

print(cost)