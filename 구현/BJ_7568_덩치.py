import sys
input = sys.stdin.readline

N = int(input())

weigth_list = []
heigth_list = []
answer_list = []

# 몸무게, 키에 대한 리스트를 따로 담기
for n in range(N):
    w, h = map(int, input().split())
    weigth_list.append(w)
    heigth_list.append(h)

# 한명씩 등수 매기기  
for i in range(N):
    # 현재 사람의 몸무게, 키 정보
    cur_w = weigth_list[i]
    cur_h = heigth_list[i]

    # i보다 더 몸무게 많이 나가는 사람의 idx, 더 키큰 사람의 idx담기 
    w_idx =[]
    h_idx = []

    for w in range(N):
        if weigth_list[w] > cur_w:
            w_idx.append(w)
    
    for h in range(N):
        if heigth_list[h] > cur_h:
            h_idx.append(h)

    # 더 후보군이 적은 리스트를 기준으로 삼기
    less_flag = False

    if len(w_idx) <= len(h_idx):
        less_flag = True
    else:
        less_flag = False
        
    res = 0
    # w_idx를 기준으로 생각하기 
    if less_flag: 
        for j in w_idx:        
            if j in h_idx:
                res += 1
    # h_idx를 기준으로 생각하기 
    else:   
        for j in h_idx: # h_idx에 속한 사람의 idx가 w_idx에도 포함되어있으면 더 덩치크다고 판단가능! 
            if j in w_idx:
                res += 1
    # +1해서 등수 추가하기
    answer_list.append(res+1)


for a in answer_list:
    print(a, end=' ')
