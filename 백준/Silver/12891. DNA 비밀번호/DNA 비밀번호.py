
S, P = map(int,input().split())
_data= list(input())
A, C, G, T = map(int, input().split())
cnt_dd = {'A':A, 'C':C, 'G':G, 'T':T}
ans = 0

def check_dd(dd, cnt_dd):
    global ans 

    flag = True
    for k, v in dd.items():
        if v < cnt_dd[k]:
            flag = False
    if flag:
        ans += 1

# 초기 데이터 저장
dd = {'A':0, 'C':0, 'G':0, 'T':0}
for i in range(P):
    dd[_data[i]] += 1
s, e = 0, P - 1
check_dd(dd, cnt_dd)

while e < S - 1:
    dd[_data[s]] -=  1
    s += 1

    e += 1
    dd[_data[e]] += 1

    check_dd(dd, cnt_dd)     # 현재 dicionary 확인

print(ans)