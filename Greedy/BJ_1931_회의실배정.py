# Purpose 
    # 사용할 수 있는 회의의 최대 갯수 

N = int(input()) # 회의 수 
time_l = [] # 각 회의 정보 

for n in range(N):
    start, end = map(int, input().split())
    time_l.append([start, end])

# 정렬
time_l.sort()

# 회의배정할 리스트 
schedule_l = []

# 일단 맨 처음 꺼 뽑기 
schedule_l.append(time_l[0])

# 기존보다 더 빨리 끝나는게 있으면 삭제하고 교체  
for i in range(1, N):
    if time_l[i][1] < schedule_l[-1][1]:
        del schedule_l[-1]
        schedule_l.append(time_l[i])

    # 뒤에 이어서 할 수 있는 회의가 나오면 추가 
    elif time_l[i][0] >= schedule_l[-1][1]:
        schedule_l.append(time_l[i])
    
print(len(schedule_l))


