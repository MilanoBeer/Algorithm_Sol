# 2초/ 128MB

# 23.05.27 
# ~ 12:30 
import math
import decimal
# 게임기록
# 횟수 X
# Exception :  Z가 변하지 않으면 -1 출력

X, Y = map(int, input().split()) 
origin = (Y*100) // X
ans = 1000000000

# 처음에 origin이 99퍼면, 무조건 -1 을 리턴
    # 게임횟수가 늘때마다, 100프로가 되려면, 이긴게임 횟수 == 총ㅇ게임 같아야
    # 이미 y가 x보다 작은 경우, 아무리 게임횟수를 늘려도 안된다
def binSearch(left, right):
    global ans

    # terminal condition 
    if left > right:
        return 
    
    # recursive
    mid = (left + right) // 2
    # 만약 더해서 변했으면
    if (Y+mid)*100//(X+mid) != origin:
        # 더 작은범위 
        ans = min(ans, mid) # 변했을때만, 최솟값 갱신 
        binSearch(left, mid-1)
    # 아직 안변했으면
    else:
        # 다시 큰 범위 
        binSearch(mid+1, right)

if origin >= 99: # 같으면 같이 증가하므로 변할 수가 없음 
    print(-1)
else:
    binSearch(1, 1000000000)
    print(ans)

# n판을 더하면, 10 + N판 
# 10 + 1 / 8 + 1