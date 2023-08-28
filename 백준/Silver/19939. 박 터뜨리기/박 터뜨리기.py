# 15:04 ~ 

N, K = map(int, input().split())
ANS = -1

# 1번바구니부터 K번 바구니까지 다 나눠줫을 대ㅑ 
tot = K*(K+1) // 2

if N >= tot:
    N -= tot
    rest = N % K
    
    if rest == 0:
        ANS = K - 1
    else:
        ANS = K

# output / Exception -> -1
print(ANS)