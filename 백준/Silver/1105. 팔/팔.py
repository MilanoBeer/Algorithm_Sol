# 23.08.09 / 10:27 ~ 
# L, R의 최댓값이 20억, 매우큼 , 단순순회 x
# 큰 값의 범위에 대해서 떠오르는 알고리즘 -> dp, 이진탐색, 투포인터, 슬라이딩 윈도우

# 1. 완탐? -> x
# 2. DP? -> 숫자 하나하나 검사하는것도 말 안됨 / 결국 8의 갯수에 대한 것이니까..
    # 자릿수마다 8의 갯수..? 
    # 그러기엔 개별 숫자들의 케이스 나누기도.. 
# 3. 구현
    # L에 들어있는 8의 갯수, R에 들어있는 8의 갯수
    # 하나라도 0개면, 답은 무조건 0개 
answer = 0
L, R = input().split()

if len(L) != len(R):
    answer = 0
else:
    L = list(L)
    R = list(R)
    # 자릿수가 같으면
    if L == R:
        answer = list(L).count('8')
    else:
        for i in range(len(L)):
            if L[i] == R[i] and L[i] == '8':
                answer +=1 
            elif L[i] != R[i]:
                break 

print(answer)
    
