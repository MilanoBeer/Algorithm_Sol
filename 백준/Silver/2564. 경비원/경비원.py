# 23.08.20 , 12:17 ~ 

hori, vert = map(int, input().split())
num = int(input())

def check(a, b):
    global x, y, hori, vert
    ans = 0

    if a == x:
        ans = abs(b - y)

    if (x == 1 and a == 2) or (x == 2 and a == 1):
        ans = min(vert + b + y, vert + (hori - y) + (hori - b))
    
    if (x == 1 and a == 3) or (x == 3 and a == 1):
        ans = b + y

    if (x == 1 and a == 4):
        ans = b + (hori - y)
    
    if ( x == 4 and a == 1):
        ans = y + (hori - b)

    if (x == 2 and a == 3):
        ans = (vert - b) + y
    if ( x == 3 and a == 2):
        ans = (vert - y) + b
    
    if (x == 2 and a == 4):
        ans = (vert - b) + (hori - y)
    if ( x == 4 and a == 2):
        ans = (vert - y) + (hori - b)
    
    if (x == 3 and a == 4):
        ans = min(hori + b + y, hori + (vert - y) + (vert - b))
    if (x == 4 and a == 3):
        ans = min(hori + b + y, hori + (vert - b) + (vert - y))
        

    return ans

_list = []
for i in range(num):
    a, b = map(int, input().split())
    _list.append([a, b])

# 2, 3 
x, y = map(int, input().split())

answer = 0
for a, b in _list:
    answer += check(a, b)
    
print(answer)
