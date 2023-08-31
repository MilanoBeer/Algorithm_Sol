# 13:08 ~

# 식탁길이 N / 햄버거 선택할 수 있는 거리 K 
N, K = map(int, input().split())
_data = list(input())
ans = 0
# Solution
    # 탐색하다가 P가 나오면
        # +K거리의 왼쪽부터 오른쪽까지 확인
            # 아직 먹지 않은 H가 나오면 체크하기
            # ans + 1
visited = [0] * (N)
for i in range(N):
    if _data[i] == 'P':
        isFind = False
        # 왼쪽
        for j in range(K, 0, -1):
            if 0 <= i - j < N:
                if _data[i-j] == 'H' and visited[i-j] == 0:
                    visited[i-j] = 1
                    ans += 1
                    isFind = True
                    break 
        # 오른쪽 
        if not isFind:
            for j in range(1, K+1):
                if 0 <= i + j < N:
                    if _data[i+j] == 'H' and visited[i+j] == 0:
                        visited[i+j] = 1
                        ans += 1
                        isFind = True
                        break 

# output : 햄버거를 먹을 수 있는 최대 사람 숫자 
print(ans)