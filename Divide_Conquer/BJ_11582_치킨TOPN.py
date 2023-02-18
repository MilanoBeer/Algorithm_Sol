# 치킨집 갯수 : 2의 거듭제곱
N = int(input()) 
# 치킨집 맛에 대한 수치들 정보 
taste_score = list(map(int, input().split()))
# 현재 정렬 진행중인 회원들의 수 : 
K = int(input())

def sorting(left, mid, right):
    # print("left : ", left, "mid: ", mid , " right : ", right)
    # print()
    a_left = left
    a_right = mid
    b_left = mid + 1
    b_right = right
    extra_list = []
    idx = 0
    
    while(a_left <= a_right and b_left <= b_right):
        if taste_score[a_left] < taste_score[b_left]:
            extra_list.append(taste_score[a_left])
            a_left += 1
        else:
            extra_list.append(taste_score[b_left])
            b_left += 1
    
    # 나머지 원소들 처리하기
    while a_left <= a_right:
        extra_list.append(taste_score[a_left])
        a_left += 1
    while b_left <= b_right:
        extra_list.append(taste_score[b_left])
        b_left += 1
    # copy to origin list
    for i in range(left, right+1):
        # print("i:" ,i)
        taste_score[i] = extra_list[idx]
        idx += 1

def dnc(n, k, left, right):

    if k == K:
        for i in taste_score:
            print(i, end=' ')
        print()
        exit(0)
    
    k = k//2 
    for i in range(k):
        size = i*(N//k)
        sorting(size, (size + (size + N//k -1))//2, size + N//k -1)
    
    dnc(n, k, left, right)

# N = 8 / 초기 등분수는 4 // N//(N//2)
min_size = N//2
for i in range(min_size):
    sorting(i*(N//min_size), i*(N//min_size), i*(N//min_size)+1)
# -- 최하위 2칸씩은 정렬이 된 상태 --
dnc(N, N//2, 0, N-1)
for i in taste_score:
    print(i, end=' ')
print()
