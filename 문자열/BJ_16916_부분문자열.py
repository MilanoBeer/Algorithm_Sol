# S P -> P가 S의 부분문자열인지 판단하기 

S = input()
P = input()

if P in S:
    print(1)
else:
    print(0)

# flag = True
# for i in range(len(S)):
#     if S[i] == P[0]:
#         for j in range(1, len(P)):
#             if i + j >= len(S):
#                  flag = False
#                  break 
#             if S[i + j] != P[j]:
#                     flag = False
#         if flag == True:
#             print("1")
#             exit(0)

# print("0")