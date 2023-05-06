# 1초 / 512MB 

# 자연수가 적힌 카드n장 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

card = list(map(int, input().split()))

for _ in range(m):
    # 정렬
    card.sort()

    # [0], [1] 의 값 더해서, 덮기
    tmp = card[0] + card[1]
    card[0] = tmp
    card[1] = tmp

print(sum(card))

