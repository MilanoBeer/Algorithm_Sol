
N = int(input())
_data = list(map(int, input().split()))

st = []
ans = [0] * (N)
for i in range(N-1, -1, -1):
    e = _data[i]
    while st and st[-1][0] <= e:
        v, idx = st.pop()
        ans[idx] = i + 1
    st.append((e, i))

while st:
    v, idx = st.pop()
    ans[idx] = 0

print(*ans)