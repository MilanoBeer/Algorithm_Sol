N = int(input())

mat = list(map(int, input().split()))
DP = mat[:]
# DP[i] => i번째 원소까지에서, i번째 원소를 포함하는 연속합중 최댓값이라는 의미 
# 매 i 마다 > 이번 i를 추가하는게 이득인가, 그만 추가하는게 나은가 / 연속합이 끊기는지 판단 /

for i in range(1, N):
    DP[i] = max(DP[i], DP[i-1] + DP[i])

print(max(DP))

