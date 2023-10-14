# 23.10.13 / 16:40 ~ 

_list = list(map(int, input()))
val = 1
i = 0

while i < len(_list):
    # 현재 _list[i]에 val가 포함되어 있지 않으면
    if str(_list[i]) not in str(val):
        val += 1
    else: # 포함되어 있으면 
        # 
        for j in str(val):
            if i >= len(_list):
                break
            # print("j:", j, "i :", i)
            if j == str(_list[i]): i += 1
            # else: break
        val += 1
    # print()
print(val - 1)