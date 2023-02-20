T = int(input())
DP = [0] * 101

DP[0] = 1
DP[1] = 1
DP[2] = 1

for i in range(3, 101):
    DP[i] = DP[i-3] + DP[i-2]

for t in range(T):
    print(DP[int(input())-1])