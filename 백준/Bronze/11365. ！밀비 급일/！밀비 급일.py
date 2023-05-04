# 1초 / 256MB
'''
23.05.04 @MilanoBeer
14:06 ~
'''

# 한줄에 하나의 암호/ 최대500자 / 마지막에 END, 해독 X
while True:
    code = input()

    # terminal condition 
    if code == 'END':
        break 

    # 해독
    print(code[::-1])