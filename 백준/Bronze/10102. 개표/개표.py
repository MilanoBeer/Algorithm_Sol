# 1초 / 256MB

V = int(input()) # 심사위원 수 / 1~ 15 
data = list(input()) # 각 심사위원이 누구에게 투표했는가 

a_cnt = data.count('A')
b_cnt = data.count('B')

if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
else:
    print("Tie")