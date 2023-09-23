# 23.09.23 / 17:24 
import sys

def input():
    return sys.stdin.readline().rstrip()


# 전투력에 따라 다른 칭호

# 칭호의 갯수 : 100,000, ㅐ릭터들 수 : 
N, M = map(int, input().split())
_data = []
for n in range(N):
    # 칭호이름, 상한값
    name, high = input().split()
    _data.append([name, int(high)])

# 캐릭터들 전투력 / 음 아님
_score = []
for m in range(M):
    tmp  = int(input())

    s, e = 0, N-1
    while s <= e:
        mid = (s + e)//2

        # [mid]자리보다 tmp가 크면
        if _data[mid][1] < tmp:
            s = mid + 1
        # [mid]자리보다 tmp가 작으면
        else:
            e = mid - 1
    # print("s :", s, ", e :", e)
    # s에 해당하는 게 정답
    print(_data[s][0])

# 생각해...
    # x : 전부 if문? 안됨. 각 원소에 대해서 10만개의 if문 확인..
    # 숫자로 판단하고, 그 숫자에 맞는 칭호를 할당 or 바로출력하기
    #  

# 완탐
# 규칙, dp 
# 그리디
# 스택, 큐
# 그래프관계 ? 아닌거같은데
