# 2초 : 4천만회 / 256MB

# 하루 동안 본 정수들 > 모두  수첩1에 기록
# M개의 질문  : 오늘 X봤어?
# 봤다고 하는 수 -> 수첩2에 기록
# Purpose
    # 수첩2에 적힌 순서대로, 각각의 수에 대해, 
    # 수첩1에 있으면 1, 없으면 0 을 출력

import sys
input = sys.stdin.readline

# 테스트 케이스 갯수 
T = int(input())

def binary_search(left, right, key):
    # terminal conditon 
    if left <= right:
        # print("left :", left, ", right :", right)
        mid = (left + right) // 2

        if _n_list[mid] == key:
            # print("found!")
            # print()
            return True
        # key값이 중간값보다 작으면 : 더 왼쪽에서 찾기 
        elif key < _n_list[mid]:
            return binary_search(left, mid-1, key)
        else:
            return binary_search(mid+1, right, key)
    # 범위를 벗어날 때 까지 못찾은 경우 : 존재하지 않으므로 False
    else:
        return False

# 테스트 케이스 갯수만큼 실행 
for t in range(T):
    # 수첩1에 적어둔 정수 정보
    N = int(input()) # 1이상, 1,000,000 (백만)이하 
    _n_list = list(map(int, input().split())) # 하루동안 실제로 본 숫자들
    
    # 수첩2에 대한 정보
    M = int(input()) # 1이상, 백만 이하 
    _m_list = list(map(int, input().split())) # 봤다고 하는 숫자들

    # Output > 수첩2의 숫자대로, 수첩1에 있으면 1, 없으면 0 
    # Sol> _m_list의 각 원소에 대해, 이진탐색을 실행

    # 먼저 n_list를 정렬
    _n_list.sort()

    for i in _m_list:
        # left : 정렬된 n_list의 첫 번째 원소인덱스 / right : 마지막 원소인덱스 
        res = binary_search(0, N-1, i)
        if res is True:
            print("1")
        else:
            print("0")
    