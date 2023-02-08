# Def > 표본을 "내림차순" 정렬하기 : 가장 큰 수가 왼쪽에 위치하도록

f = open("input.txt", "r")
n = int(f.readline())

# n만큼 array 입력받기 
data_list = list(map(int, f.readline().split()))

def swap(index_a, index_b):
    temp = data_list[index_a]
    data_list[index_a] = data_list[index_b]
    data_list[index_b] = temp

# quick sort 
def quick_sort(left, right):
    if left < right :
        # init pivot, index
        pivot = data_list[right]
        swap_pos = left; 

        for i in range(left, right + 1):
            if data_list[i] > pivot:
                # swap 
                swap(i, swap_pos)
                # 옮길 위치 조정
                swap_pos += 1
        pivot_point = swap_pos
        # swap(pivot, 마지막으로 옮겨진 swap point) 
        swap(right, pivot_point)

        # 왼쪽, 오른쪽 재호출
        quick_sort(left, pivot_point-1)
        quick_sort(pivot_point + 1, right)

quick_sort(0, n-1)

# 정렬된 결과 확인
for i in range(n):
    print(data_list[i], end = ' ')  
print()