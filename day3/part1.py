import re

s = []
numbers = []
while True:
    try:
        row = input()
        s.append(list(row))

        print(row)

        for n in re.findall(r'\d+', row):
            numbers.append(int(n))

    except EOFError:
        break
x = [0, 1, 1, 1, 0, -1, -1, -1]
y = [-1, -1, 0, 1, 1, 1, 0, -1]

print(numbers)

def rem(i, j):
    if i < 0 or j < 0 or i >= len(s) or j >= len(s[i]):
        return
    if s[i][j] == '.':
        return
    s[i][j] = '.'
    rem(i, j-1)
    rem(i, j+1)


for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] != '.' and not s[i][j].isdigit():
            for k in range(8):
                rem(i-x[k], j-y[k])
            s[i][j] = '.'

out_nums = []
for i in range(len(s)):
    print(''.join(s[i]))
    for n in re.findall(r'\d+', ''.join(s[i])):
        out_nums.append(int(n))

print(out_nums)
print(sum(numbers)-sum(out_nums))

