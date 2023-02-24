import sys
input = sys.stdin.readline

# N개의 수 / M개의 횟수 더해야하는 명령 
N, M = map(int, input().split())
# N개의 숫자 리스트 
n_l = list(map(int, input().split()))

# init > 각 자리까지의 합을 구해두기
for i in range(1, len(n_l)):
    n_l[i] = n_l[i-1] + n_l[i]
    # => [5, 9, 12, 14, 15]

for _ in range(M):
    i, j = map(int, input().split())
    if i-1 == 0:
        sum = n_l[j-1]
    else:
        sum = n_l[j-1] - n_l[i-2]
    print(sum)