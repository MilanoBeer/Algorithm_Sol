# 11:45 ~ 
from collections import Counter

N, K = map(int, input().split())
cnt_dic = []
ctrs = []
for n in range(N):
    n, gold, sil, bron = map(int, input().split())
    cnt_dic.append([gold, sil, bron])
    ctrs.append([n, gold, sil, bron])

ctrs.sort(key = lambda x:(x[1], x[2], x[3]), reverse=True)

# print(cnt_dic)
# print(cnt_dic.count(cnt_dic[2]))
# 동급자.. 

for i in range(N):
    if ctrs[i][0] == K:
        same_cnt = cnt_dic.count(ctrs[i][1:])
        # i = 2 -> 3등
        # same = 2 -> 3 - (same - 1)

        print((i+1) - (same_cnt - 1))