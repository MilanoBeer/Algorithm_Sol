# 5초 / 256MB
# 23.05.18
# 10:35 ~ 10:43

# 비밀번호 찾는 프로그램
import sys
input = sys.stdin.readline

# N : 1 ~ 10만 / 저장된 사이트 주소의 숫자 
# M : 1 ~ 10만 / 찾으려는 사이트 주소의 수 
N, M = map(int, input().split())

# DS: 딕셔너리 
dic = dict()
for n in range(N):
    # 사이트 주소, 비밀번호 
    site, pw = input().split() # 둘다 최대길이 20 
    dic[site] = pw

# 찾을 사이트 M개
for m in range(M):
    name = input().rstrip()
    print(dic[name])
