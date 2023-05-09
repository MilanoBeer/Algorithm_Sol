# 1초/ 128MB
# 23.05.09
# 23:19 ~ 

# 깊이가 K / 모든 자식은 왼쪽, 오른쪽 자식
# Left -> Right -> Root 

K = int(input()) # k는 1 ~ 10 
building = list(map(int, input().split()))

# 순회방식 : 중위순회 
# - 리스트에서 가운데 index가 root임은 확실함
# - root를 기준으로 나뉜 양쪽이, 서브트리가 된다!

# root출력
# root기준으로 나누기 시작.. => 반복.. 
# _list = []
_list = [[] for _ in range(K)]
sz = pow(2, K) -2 # (3, K) 라고 했음..

def divide(left , right, level):
    # terminal condition : r_idx하위가 leaf면 ?
    if left > right or left < 0 or right > sz:
        return 

    # divide
    mid = (left + right) // 2
    # print(buildingmid], end=' ')
    _list[level].append(building[mid])

    divide(left, mid-1, level+1)
    divide(mid+1, right, level+1)
    
divide(0, sz, 0) # Root index 

for i in range(K):
    print(*(_list[i]))