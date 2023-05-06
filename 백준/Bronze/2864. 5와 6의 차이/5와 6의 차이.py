

# 두 수 더한다 -> 두 수의 가능한 합중, 최솟값과 최댓값 출력

A, B = input().split()

min_val = 2000002
max_val = 0


# 최솟값 구하기
# if 6이 포함되어 있으면 -> 5로 보기 
A = A.replace('6', '5')
B = B.replace('6', '5')
min_val = int(A) + int(B)

# 최댓값 구하기 
# if 5가 포함되어 있으면 -> 6으로 보기 
A = A.replace('5', '6')
B = B.replace('5', '6')
max_val = int(A) + int(B)

print(min_val, max_val)