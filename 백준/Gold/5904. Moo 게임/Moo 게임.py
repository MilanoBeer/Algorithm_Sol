
N = int(input())

init = ['m', 'o', 'o']
tot = 3
n = 0

while tot < N: # 아직 작을동안 증가시키기
    n += 1
    tot = 2 * tot + n + 3

# 수열의 총 갯수가 N이상이 됨 -> 탐색가능해짐
def dnc(tot, idx, target):
    global init

    # print(tot, idx, target)
    
    # terminal condition 
    if tot <= 3:
        # print("terminal")
        # print(init[target-1])
        return init[target-1]

    # 영역 나누기 : 왼쪽 / 가운데 / 오른쪽
    prev = (tot - (idx + 3)) // 2

    # 왼쪽인가
    if target <= prev:
        return dnc(prev, idx - 1, target)

    # 오른쪽인가
    elif target > tot - prev:
        return dnc(prev, idx - 1, target - (tot - prev))

    # 가운데인가
    if target - prev == 1:
        return 'm'
    else:
        return 'o'


print(dnc(tot, n, N))