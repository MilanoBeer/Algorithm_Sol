# 한 세트 : 0 ~9 
# 다솜이 방번호 N
N = list(map(int, input()))

num_list = [False] * (10)

total_list = []
total_list.append(num_list)

for n in N:
    NFlag = False
    for t in range(len(total_list)):
        # 만약 n이 6이거나 9일 경우
        if n == 6 or n == 9:
            if total_list[t][6] is False:
                total_list[t][6] = True
                NFlag = True
                break # 다음 카드 판별하러
            elif total_list[t][9] is False:
                total_list[t][9] = True
                NFlag = True
                break 
            else:
                continue

        # n이 다른 숫자일때 
        else:
            # 아직 해당 자리가 False면(사용된 적이 없으면)
            if total_list[t][n] is False:
                total_list[t][n] = True
                NFlag = True
                break # 다음 카드 판별하러
    # 현재 목록에선 추가할 수 없으면
    if NFlag is False:
        num_list = [False] * (10)
        total_list.append(num_list)
        total_list[len(total_list) - 1][n] = True # 다음 리스트에 미리 사용하기 

         
print(len(total_list))

