# 1초 / 256MB
# 23.05.22
# 16:12 ~ 5:15 / 구글링 참조

# 키로거 : 명령 모두 기록 / 화살표, 등 포함
# 목적 : 비밀번호 알아내기 
# 화살표 : 커서의 위치를 움직일 수 있다면!
# 백스페이스 : 앞에 글자 잇으면 지움

# DS / Algorithm : 문자열 다루기 

import sys

T = int(input())

for t in range(T):
    # ***** 길이가 L인 문자열 : 1이상, 100만이하  *****
    data = list(input())
    left, right = [], []

    for i in data:
        # 백스페이스일 경우
        if i == '-':
            # 앞에 데이터가 있다면
            if len(left) > 0:
                left.pop()
        # 왼쪽화살표
        elif i == '<':
            # 앞에 데이터가 잇어야 한다 
            if len(left) > 0:
                right.append(left.pop())

        # 오른쪽화살표 : ">"
        elif i == '>':
            if len(right) > 0:
                left.append(right.pop())
        # 알파벳일 경우
        else:
            left.append(i)
    # 예외처리
    left.extend(reversed(right))
    
    print(''.join(left))