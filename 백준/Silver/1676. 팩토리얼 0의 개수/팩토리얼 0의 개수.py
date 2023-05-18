# 2초 / 128MB
# 23.05.18 
# 10:00 ~ 

N = int(input())
_list = [0] * (N+1)
_list[0] = 1


def facto(v):
    # terminal 
    if v == 0:
        return _list[v]

    # 메모이제이션 된 값이 있으면, 찾아서 넘김
    if _list[v] != 0:
        return _list[v]
    else:
        return v * facto(v-1)
result = str(facto(N))

# find ans
cnt = 0
for i in range(len(result)-1, -1, -1): 
    if result[i] != '0':
        print(cnt)
        break 
    else:
        cnt += 1