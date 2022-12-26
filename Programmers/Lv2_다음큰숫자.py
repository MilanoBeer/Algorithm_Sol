def solution(n):
    answer = 0
    res_list = []
    
    next_big = n + 1 # n을 0까지 나누기전에 미리! 
    
    while n != 0:
        res_list.append(n % 2)
        n //= 2
    
    # n 이진변환의 1 갯수 저장
    n_one_cnt = res_list.count(1)
    
    expon = len(res_list) # n의 자릿수
    
    while True:
        # 다음 자릿수로 넘어가는 숫자라면
        if next_big == pow(2, expon):
            expon += 1
            
        # expon을 활용해서, 나눠야할 계산 줄이기
        next_big_res = next_big - pow(2, expon-1)
        next_big_res_list = []
        
        while next_big_res != 0:
            next_big_res_list.append(next_big_res % 2)
            next_big_res //= 2
        next_big_res_one = next_big_res_list.count(1)
        next_big_res_one += 1 # 1: 2의 expon-1 에서 1은 한개로 고정, 마지막에 추가해줌
        
        if next_big_res_one == n_one_cnt:
            answer = next_big
            break 
        else:
            next_big += 1
    
    return answer

