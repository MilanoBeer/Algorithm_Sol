mat = [list(input()) for _ in range(5)]
read_list = []

max_len = 0
for line in mat:
    max_len = max(len(line), max_len)

for col in range(max_len):
    for row in range(5):
        if len(mat[row]) > col:
            read_list.append(mat[row][col])
        else:
            continue

print(''.join(map(str, read_list)))
