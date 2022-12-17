n = int(input())

fibo = [0] * 91

# init fibo
fibo[0] = 0
fibo[1] = 1

for i in range(2, 91):
    fibo[i] = fibo[i-1] + fibo[i-2]
    # if i==n:
    #     print(fibo[i])
    #     break

print(fibo[n])