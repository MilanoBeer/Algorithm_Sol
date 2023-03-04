# 단어 >
# 알파벳 소문자 & 숫자로 이루어진 부분 문자열
# 연속하는 두 단어는 공백 하나로 구분

# 태그 > 
# <, > 로 끝나는, 길이가 3 이상인 부분 문자열

# 태그는 단어가 아님 / 태그와 단어 사이에는 공백이 없음 

# *** 하나씩 읽으면서, 태그랑 단어를 구별하기 *** 
s = input() # 100,000이하 
res_s = []
stack = [] 
tag_flag = False

for idx in range(len(s)):
    # if 열린 태그 
    if s[idx] == '<':
        if len(stack) > 0:
            stack.reverse()
            res_s.append(stack)
            stack = []
        stack.append(s[idx])
        tag_flag = True
    elif s[idx] == '>':
        # 완성된 태그는 뒤집지 않고, res_S에 추가해두기 
        stack.append(s[idx])
        res_s.append(stack)
        stack = []
        tag_flag = False # ** 초기화 잊지말기 **
    # if 공백을 만나면 
    elif s[idx] == ' ':
        # 지금까지 담아둔 단어 거꾸로 해서 리스트에 추가하기 
        # 태그에 포함된 공백이 아니라면 
        if tag_flag is False:
            stack.reverse()
            res_s.append(stack)
            stack = []
            res_s.append(' ') # 공백은 따로 바로 추가해두기 
        else:
            stack.append(s[idx])
    # if 그냥 소문자 or 숫자 
    else:
        stack.append(s[idx])
        
# 마지막에 만들어진 stack 뒤집어서 추가
stack.reverse()
res_s.append(stack)

for word in res_s:
    print(''.join(map(str, word)), end='')
print()