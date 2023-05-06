# 16:55 ~ 

# input: 거스름돈의 액수 

# Condition 
# 동전갯수를 최소로 하도록. -> 최대한 높은 동전을 많이 내야한다 

# output: 0.25 / 0.10 / 0.05 / 0.01dml rottn 

T = int(input())

for t in range(T):
    cnt = 0
    C = int(input())
    
    # 0.25 -> 25로 치환해서 생각하기
    q_cnt = (C//25)
    d_cnt = (C - 25*q_cnt) // 10
    n_cnt = (C - 25*q_cnt - 10*d_cnt ) // 5
    p_cnt = (C - 25*q_cnt - 10*d_cnt - 5*n_cnt) // 1

    print(q_cnt, d_cnt, n_cnt, p_cnt)
