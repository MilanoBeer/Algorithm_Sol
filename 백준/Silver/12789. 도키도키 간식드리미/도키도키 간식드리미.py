N = int(input())
_data = list(map(int, input().split()))

_result = [1]
stack = []
turn = 1

for i in range(len(_data)):
    stack.append(_data[i])
    while stack and turn == stack[-1]:
        stack.pop()
        turn += 1

if stack:
    print("Sad")
else:
    print("Nice")

# stack = stack[::-1]
# isCorrect = True
# for e in stack:
#     if _result[-1] + 1 == e:
#         _result.append(e)
#     else:
#         isCorrect = False
#         break 
# if isCorrect:
#     print("Nice")
# else:
#     print("Sad")
