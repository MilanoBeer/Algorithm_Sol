import heapq

# input > 지름길 갯수 N, 고속도로 전체길이 D
N, D = map(int, input().split())

MAX = 10001

# D size의 list만들기 
# 1번 방법
# dist_list = list()
# for i in range(D+1):
#     dist_list.append(i)
heap = []
# 2번 방법
dist_list = list(range(0, MAX)) # 일정 범위안에 연속된 숫자 리스트 만들기 
arr = [[] for _ in range(10001)]

# 지름길 정보 N개 입력받기 > 시작점, 도착점, 거리
for k in range(0, N):
    start, end, dist = map(int, input().split())
    arr[start].append([dist, end])
    heapq.heappush(heap,(start,end,dist))



while heap:
    start, end, dist = heapq.heappop(heap)

    # end가 더 크면 패스
    if dist > (dist_list[end] - dist_list[start]) or end > D:
        continue

    # 크기 비교 및 갱신
    if dist_list[end] > dist_list[start] + dist:
        dist_list[end] = dist_list[start] + dist
        
        # end 이후의 원소들 갱신
        for i in range(end+1, MAX):
            dist_list[i] = min(dist_list[i], dist_list[i-1] + 1)
        # if dist_list[i] > dist_list[end] + (i -end):
        #     dist_list[i] = dist_list[end] + (i - end)


# dist_list[D]의 값 최종 출력
print(dist_list[D])  
    