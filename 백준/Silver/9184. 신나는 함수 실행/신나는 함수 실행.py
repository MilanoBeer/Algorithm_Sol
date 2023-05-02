'''
23.05.02
11:15 ~ 
'''
#  1초 / 128MB
# Error : 시간초과 / 틀림 

import sys
input = sys.stdin.readline

visited = [[[0] * (51) for _ in range(51)] for _ in range(51)]

def w(a, b, c):
    # 이미 있으면 # 근데 음수들이 존재해서, 단순 인덱스활용은 x
    # 근데 셋중 하나라도 음수면, 무조건 1을 리턴
    # 셋중 하나라도 20초과면 무조건 W(20, 20, 20)     
    if a <= 0 or b <= 0 or c <= 0:
#        visited[a][b][c] = 1
        return 1
    
    elif visited[a][b][c] != 0:
        return visited[a][b][c]

    elif a > 20 or b > 20 or c > 20:
        visited[a][b][c] = w(20, 20, 20)
        return visited[a][b][c]

    elif a < b and b < c:
        visited[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return visited[a][b][c]

    else:
        visited[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return visited[a][b][c]

# a, b, c: 각각 -50이상, 50이하 
while True:
    a, b, c = map(int, input().split())

    # terminal condition 
    if a == -1 and b == -1 and c == -1:
        break 

    # Solution 
    res = w(a, b, c) 

    # Output
    # a, b, c -> w(a, b, c)출력
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, res))


