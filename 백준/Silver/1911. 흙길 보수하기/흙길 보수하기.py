# 23.08.25 / 16:19 ~ 

N, L = map(int, input().split())

_data = []
for n in range(N):
    # 웅덩이의 시작위치, 끝위치 / 0이상 10억이하 
    s, e = map(int, input().split())
    _data.append([s, e])

_data.sort(key = lambda x:(x[0]))

cnt = 0
last_e = 0
for s, e in _data:
    # 이전경우에서 초과한 널빤지위치가 s보다 크면 , 시작점을 더 앞으로 
    if last_e >= s:
        s = last_e + 1

    # 시작점이 마지막점보다 앞으로 와버리면 continue
    if s >= e:
        continue
    
    # 초과해서 놓이는 널빤지 마지막 위치 알기 
    mok = (e - s) // L
    namugi = (e - s) % L
    cnt += mok

    if namugi != 0:
        cnt += 1
        last_e = s + L
    last_e += L*mok - 1

print(cnt)