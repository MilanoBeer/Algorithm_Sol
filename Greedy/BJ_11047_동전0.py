# N : 가지고 있는 동전의 종류 
# K : 동전을 활용해서 -> 합을 K로 
# Answer : 동전 갯수의 최솟값 

N, K = map(int, input().split())
cost_l = []
for i in range(N):
    cost_l.append(int(input()))

# 오름차순 보장 > 맨 뒤의 원소부터 
cost = 0
for i in range(N-1, -1, -1):
    if cost_l[i] > K:
        continue
    else:
        div = K // cost_l[i]
        K -= cost_l[i] * div
        cost += div

print(cost)