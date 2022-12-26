def solution(n):
    print("n:", n)
    answer = 0
    res_list = []
    
    bigger = n + 1
    while n != 0:
        res_list.append(n % 2)
        n //= 2
    
    # n의 1갯수 count
    n_one_cnt = res_list.count(1)
    
    
    expon = len(res_list)
    pow_cnt = expon
    
    while True:
        if bigger == pow(2, expon):
            expon += 1
            
        bigger_res = bigger - pow(2, expon - 1)
        bigger_res_list = []
        while bigger_res != 0:
            bigger_res_list.append(bigger_res % 2)
            bigger_res //= 2
        bigger_res_one = bigger_res_list.count(1)
        bigger_res_one += 1
        
        if bigger_res_one == n_one_cnt:
            answer = bigger
            break 
        else:
            bigger += 1
    
    return answer
