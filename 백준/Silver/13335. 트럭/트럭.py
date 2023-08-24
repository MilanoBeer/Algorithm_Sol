import sys

n, w, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
temp = [0] * w # 다리의 칸
cnt = 0

# 반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복
while temp:
    cnt += 1 # 카운트
    temp.pop(0) # 다리의 칸을 하나씩 줄인다.

    # 모든 트럭을 확인
    if a:
        # 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가
        # 다리의 하중보다 크다면 빈 공간을 추가
        if sum(temp) + a[0] > l:
            temp.append(0)

        # 다리의 하중보다 작다면 트럭을 다리에 추가
        else:
            temp.append(a.pop(0))

print(cnt)