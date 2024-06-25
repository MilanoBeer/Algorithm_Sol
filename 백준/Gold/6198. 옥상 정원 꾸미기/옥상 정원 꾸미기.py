
N = int(input())
_data = [] 

for n in range(N):
    _data.append(int(input()))

ans = 0
st = []

for i in range(N):
    while st and st[-1] <= _data[i]:
        st.pop()
    st.append(_data[i])

    ans += len(st) - 1

print(ans)



