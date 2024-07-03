N = int(input())

# 현재 총 길이, 가운데 길이, 구하려는 순서
def recursive(total_length, mid_length, N):
    if N <= 3:
        return "moo"[N-1]

    # 왼쪽 수열 길이 = 가운데를 제외한 반
    left_length = (total_length - mid_length) // 2

    # 찾으려는 순서가 왼쪽 수열에 있으면 -> 그 전 수열로 ㄱ
    if N <= left_length:
        return recursive(left_length, mid_length - 1, N)

    # 찾으려는 순서가 오른쪽 수열에 있으면 -> 왼쪽 수열의 순서로 바꾸고 그 전 수열로 ㄱ
    if N > left_length + mid_length:
        return recursive(left_length, mid_length - 1, N - left_length - mid_length)

    # 찾으려는 순서가 가운데에 위치할 때
    # 찾으려는 순서가 가운데의 첫번째면 m, 아니면 o
    if N - left_length == 1:
        return "m"
    else:
        return "o"


total_length = 3  # 처음에는 moo 세글자
n = 0  # 몇번째 수열인지 -> 가운데 길이 구하기 위함
while total_length < N:
    # 기존 수열 * 2 + o 개수 + m 개수
    n += 1
    total_length = 2 * total_length + n + 3

# 가운데 길이 = 수열 순서 + 3
print(recursive(total_length, n+3, N))
