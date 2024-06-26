# 수소: 1
# 탄소: 12
# 산소: 16

ans = 0
st = []
tmp_st = []

_data = list(input())
H = 1
C = 12
O = 16

dd = {'H':1, 'C':12, 'O':16}

for i in range(len(_data)):
    e = _data[i]

    if e.isdigit():
        st.append(st.pop() * int(e))
    elif e == ')':
        tmp_ans = 0

        while st:
            tmp = st.pop()
            if tmp == '(':
                break
            tmp_ans += tmp
        st.append(tmp_ans)
    elif e == '(':
        st.append(e)
    else:  # H, C, O 
        st.append(dd[e])
print(sum(st))