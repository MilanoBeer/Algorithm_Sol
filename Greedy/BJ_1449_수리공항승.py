# 물이 새는 위치 : 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 셈
# 길이가 L 인 테이프 무한개 
# 물막기 
    # 위치의 좌우 0.5만큼 간격줘야함
# Answer > 항승이가 필요한 테이프의 최소 갯수 
# Condition> 
    # 자를 수는 없음
    # 겹쳐붙이기 가능

# N : 물이 새는 곳의 수 / L : 테이프 길이 
N, L = map(int, input().split()) 
leak_l = list(map(int, input().split())) # 물이 새는 곳 위치

leak_l.sort() # ***** sorting ! ****** #
# sort를 안하면, 더 앞선 위치에서 붙여둔 테이프로 뒤에 위치를 덮을 수가 없음
    # 덮을 때, 앞쪽으로 나가면서 처리하기 때문에.. 
    
tape_cnt = 0
taping_pos = [False] * (1000 + L +1) 

for i in range(N):
    if taping_pos[leak_l[i]] == False:
        tape_cnt += 1
        # 테이프 길이만큼 테이핑 처리 
        for t in range(leak_l[i], leak_l[i] + L):
            if t > 1000:
                break
            taping_pos[t] = True
    else:
        continue

print(tape_cnt)
# *** index에러가 날 때는, 변수의 범위에서 양 끝값을 테케로 만들어서 넣어보자 