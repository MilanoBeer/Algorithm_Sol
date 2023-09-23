# 23.09.23 / 18:24 ~ 
# 소문자
# 양수!!!! k

from collections import Counter
import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for t in range(T):
    W = input()
    K = int(input())
    
    # 생각해..  # 투포인터? 
    # 문자열W안에서 알파벳별로 빈도수 도출
    _cc = Counter(W)
    min_val = sys.maxsize
    max_val = -1

    for i in range(len(W)):
        if _cc[W[i]] < K:
            continue
        else:
            s, e = i, i + 1
            cnt = 1
            while cnt < K and e < len(W):
                # e자리 확인
                if W[e] == W[i]:
                    cnt += 1
                e += 1
            e -= 1
            if cnt == K:
                min_val = min(min_val, e - s + 1)
                max_val = max(max_val, e - s + 1)
    if min_val == sys.maxsize or max_val == -1:
        print(-1)
    else:
        print(min_val, max_val)
    
    # W순회
        # K보다 낮은 빈도수면 continue

        # K이상이면
            # while 
            # 해당알파벳을 시작점으로 해서, end지점 1씩 증가
            # 시작점 알파벳과 같으면, cnt + 1
            # cnt가 K가 되면, 
                # s - e 길이 계산
                # min, max값에 갱신하기 
            
