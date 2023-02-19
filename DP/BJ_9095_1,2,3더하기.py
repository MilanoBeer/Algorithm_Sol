T = int(input())

D = [0] * 11

D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4, 11):
    D[i] = D[i-3] + D[i-2] + D[i-1]

for t in range(T):
    print(D[int(input())])
          
    