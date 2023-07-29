# 23.07.29 / 20:38 ~ 21:04
from collections import defaultdict 
def solution(nums):
    answer = 0
    #  총 N 마리의 폰켓몬 중에서 N/2마리를 가져가
    dd = defaultdict(int)
    size = len(nums)//2
    
    for i in nums:
        dd[i] += 1
        
    dic = sorted(dd.items(), key = lambda x: x[1])
    cnt = 0
    
    if len(dic) > size:
        answer = size
    else:
        answer = len(dic)
    
    return answer

 #  같은 종류의 폰켓몬은 같은 번호
    
    # 가장 많은 종류
    # 완탐
    # ? Counter를 통해, 총 포켓몬 종류를 알아내면?
    # ? 딕셔너리로 각 값의 나오는 빈도수를 카운트하고, 
    # 작은 값을 가진 순서대로 정렬하고
    # 앞에서부터 len(nums)의 반틈만큼 카운트 될 때 까지 ..?
    # 1 : 1, 2:1, 3:2 