import sys
input = sys.stdin.readline
# 잘못된 수를 부르면 / 0을 외침 / 가장 최근에 쓴 수를 지우자

K = int(input())


num_list = []
for k in range(K):
    tmp = int(input())
    
    if tmp == 0:
        num_list.pop()
    else:
        num_list.append(tmp)
print(sum(num_list))    
    
