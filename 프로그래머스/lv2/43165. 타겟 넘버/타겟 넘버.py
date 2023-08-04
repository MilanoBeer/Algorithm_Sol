# 23.08.04  19:29 ~ 

answer = 0
def dfs(_len, numbers, cnt, tot, target):
    global answer
    # terminal
    if cnt == _len - 1:
        if tot == target:
            answer += 1
        return 

    # recursive
    # 할 수 있는거 + , - 
    dfs(_len, numbers, cnt + 1, tot + numbers[cnt+1], target)
    dfs(_len, numbers, cnt + 1, tot - numbers[cnt+1], target)

def solution(numbers, target):
    global answer
    
    # +로 출발
    dfs(len(numbers), numbers, 0, numbers[0], target) # 현재까지 사용한 numbers의 index, 계산된 값, target    
    # -로 출발
    dfs(len(numbers), numbers, 0, -numbers[0], target)
    
    return answer