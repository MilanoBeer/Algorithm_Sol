N = int(input())

str_list = []

for i in range(N):
    str_list.append(input())

# do : 중복 제거
str_list = list(set(str_list))

# do : 정렬하기 
str_list.sort()
# str_list.sort(key=len) => 이거써도 통과
str_list.sort(key=lambda x : len(x))

for i in str_list:
    print(i)
