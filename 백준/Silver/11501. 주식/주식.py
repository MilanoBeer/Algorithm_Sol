# 5초 / 256MB

# 23.05.17
# 11:18 ~ 

T = int(input())

for t in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    idx = N-1 # 시작 인덱스는 여기
    for i in range(N-2, -1, -1):
        # i보다, 그 앞에가 더 작으면-> 차액 추가 
        if data[i] < data[idx]:
            ans += data[idx] - data[i]
        else: # 앞선 값이 더 크다면, 기준idx를 교체 
            idx = i 
    print(ans)

