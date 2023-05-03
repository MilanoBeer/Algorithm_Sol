# 1초 / 128MB

# 3:50 ~ 

# 주어지는 문자열 -> 숫자로 변환 / 2이상, 15이하 
code = list(input().strip())

# Solution 
# 각 알파벳마다 맞는 숫자 대응해두기
dic = dict()
# dic['A'] = dic['B'] = dic['C'] = 1
# dic['D'] = dic['E'] = dic['F'] = 2
# dic['G'] = dic['H'] = dic['I'] = 3
# dic['J'] = dic['K'] = dic['L'] = 4
# dic['M']

dic['ABC'] = 2
dic['DEF'] = 3
dic['GHI'] = 4
dic['JKL'] = 5
dic['MNO'] = 6
dic['PQRS'] =7
dic['TUV'] = 8
dic['WXYZ'] = 9

# code하나씩 읽어서 시간계산하기 
tot_time = 0
for c in code:
    for k in dic.keys():
        if c in k:
            tot_time += dic[k] + 1
# 시간 구하기 
print(tot_time)