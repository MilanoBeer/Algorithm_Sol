# 1초 / 256MB
# 22:10 ~ 
# ps카드 : 아이디 - 얼굴이 적혀있는 카드 
    # 등급을 나타내는 색 / 8가지 

# 카드팩 -> 1개포함된 카드팩 .. N 개가 포함된 카드팩 -> N가지 

# 돈 많이 지불해서, 카드N 개를 구매하고자 함. 
# -> 카드가 i개 포함된 카드팩의 가격은 Pi 원 

N = int(input()) # 1이상, 1000이하 
price = list(map(int, input().split()))
price.insert(0, 0) # * dp배열에 맞게 맞춰주기 

# Condition : 딱 N개 사야함!!!
# DP init
# 1차원? 2차원?
    # if 1차원 -> 변하는 거 : index랑 가격 / 카드의 총 갯수 
    # 카드를 1개, 2개, 3개,.. .N개까지 살 때, 최대 지불할 수 있는 가격은?!
    # 카드1개짜리 팩으로 , 1개 살떄 가격, 2개살때, ,... N 개 살 때 가격
    # 행-> 카드 1개, 2개, .. / 열 : 1개살때, 2개살 때 .. 
dp = [[0] * (N+1) for _ in range(N+1)]

# init 1 row
for i in range(1, N+1):
    dp[1][i] = price[1] * i
    # dp[i][1] = price[0] * i

# input dp array
for i in range(2, N+1): # row
    for j in range(1, N+1): # col
        # 같은 col, 이전 row의 값 
        # i = 2, j = 1, 2, 3, 
        if i < j: # 다른 카드랑 섞여서 채워야함 
            # 이전 값
            # tmp = j % i
            dp[i][j] = max(dp[i-1][j], dp[i][j-i] + price[i])
        else:
            dp[i][j] = max(dp[i-1][j], price[i] * (j//i))

# for line in dp:
#     print(line)

print(dp[N][N])