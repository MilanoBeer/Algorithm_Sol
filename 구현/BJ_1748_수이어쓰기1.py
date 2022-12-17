
N = input()

# 자릿수 
N_len = len(N) 
N = int(N)

answer = 0

for i in range(1, N_len):
    answer += 9 * (10**(i-1)) * i

# 마지막 자릿수에 대해 계산하기
leave_N = N - (10**(N_len-1)) + 1
answer += leave_N * N_len

print(answer)
