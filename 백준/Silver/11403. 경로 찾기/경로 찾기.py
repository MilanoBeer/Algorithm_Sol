# 1초 / 256MB

# 방향 / 가중치는 X / 
# 경로 있는지 구하기 

N = int(input()) # 정점 갯수 / 1이상, 100이하 

# 인접행렬
mat = [list(map(int, input().split())) for _ in range(N)]

# 다른 점을 거쳐서, 도착할 수 있는지 ! 
# 현재문제는 가중치 계산은 X. "도착할 수 있는지 없는지 여부만! "
# 시작 -> 다른 여러개의 vertex -> 도착 
# 플로이드 워셜 ->100^3 -> 1,000,000 -> 시간복잡도 O 

# 결과배열 init : 현재 배열을 기준으로 한다
copy_mat = mat[:]

# 다른 지점 거쳐가기
for k in range(N):
    for r in range(N):
        for c in range(N):
            # k를 거쳐서 갈 때, 경로가 존재하면 1로 갱신
            if copy_mat[r][c] == 0:
                if copy_mat[r][k] == 1 and copy_mat[k][c] == 1:
                    copy_mat[r][c] = 1

for line in copy_mat:
    print(*line)



