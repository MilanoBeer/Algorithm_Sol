n = int(input())
sugar_bag = 0

# 5의 배수일 경우, 5로 나눈 몫이 가장 최솟값이 됨 
if n % 5 == 0:
    sugar_bag = n // 5
    n -= sugar_bag * 5
else:
    while n > 0 :
        # n이 아직 양수일 동안, 3을 빼면서, 5로 나눠지는지 확인
        n -= 3
        sugar_bag += 1
        # 5의 배수가 되는 시점에는, 5로 바로 나누는게 최솟값 
        if n % 5 == 0:
            sugar_bag += n // 5
            n = 0
            break

# n이 0이 되서 끝났는지 확인
if n == 0:
    print(sugar_bag)
else:
    print(-1)