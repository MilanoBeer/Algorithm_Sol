N, K = map(int, input().split())

day_l = list(map(int, input().split()))

cur_sum = 0
start = 0 
# 각 원소의 최솟값이 -100이므로, 그 원소들의 합을 담을 값은 훨씬 작은 안정적인 값으로 설정해야함!!
max_sum = float('-inf')

for e, val in enumerate(day_l):
    cur_sum += val
    # 3개의 합
    if e - start + 1 == K:
        max_sum = max(max_sum, cur_sum)
        cur_sum -= day_l[start]
        start += 1

print(max_sum)



    