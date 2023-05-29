# 1초 / 256MG
# 23.05.29
# 19:50 ~ 

# N개이ㅡ 수 
# M개의 구간 -> i번째부터 j번째 합 구하기
import sys
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
_list.insert(0, 0)

# traversal: _list / 각 index까지의 합
for i in range(1, N+1):
    _list[i] += _list[i-1]


M = int(input()) # 구간의 갯수 
for m in range(M):
    # 구간 i ~ j 
    i, j = map(int, input().split())

    # OUTPUT
    print(_list[j] - _list[i-1])

# Error : 주어지는 숫자 -> "1"부터시작 -> 범위는 N+1
