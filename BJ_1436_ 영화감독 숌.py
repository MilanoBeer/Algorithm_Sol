# BJ_1436_영화감독 숌

# 종말의 숫자 : 적어도 6이 3개이상 

# N 입력 
N = int(input())

cnt = 0; 
strt = 666

while True:
    if '666' in str(strt):
        cnt += 1
        if N == cnt:
            print(strt)
            break
        strt += 1
    else:
        strt += 1
# N이 1부터 10,000까지임! 후보가 될 수 있는 값이 아니라.. 문제 잘 읽기..
# 분기문에서 strt + 1 해주는 시점 주의! 