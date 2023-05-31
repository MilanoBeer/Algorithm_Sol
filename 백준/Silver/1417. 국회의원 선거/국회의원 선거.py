# 2초 / 128MB
# 23.05.31
# 15:35 ~ 15:55 / 전혀모르겠음..

# 후보 N 명
# 마을주민 M 명
import heapq 
import sys
input = sys.stdin.readline

N = int(input())
das = int(input())

_list = []
for n in range(N-1):
    # 1이상, 100이하 
    num = int(input())
    heapq.heappush(_list, (-num, num))

# Sol
# 1번 다솜이 숫자 확인 
ans = 0

# 뽑은 값이 다솜보다 작으면 멈춤
if N == 1:
    print(0)
else:
    while True:
        cur = heapq.heappop(_list)[1]

        if das <= cur:
            cur -= 1
            ans += 1
            # dasom도 증가시키기! 
            das += 1

            # 다시 heap에 넣기
            heapq.heappush(_list, (-cur, cur))
        else:
            break 

    # OUTPUT : 매수해야하는 사람의 최솟값
    print(ans)



