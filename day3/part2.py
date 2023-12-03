from numpy import prod

s = []
while True:
    try:
        row = input()
        s.append(list(row))

        print(row)

    except EOFError:
        break
x = [0, 1, 1, 1, 0, -1, -1, -1]
y = [-1, -1, 0, 1, 1, 1, 0, -1]


def check(i, j, m):
    if not m[i][j].isdigit():
        return 0
    while j-1 >= 0 and m[i][j-1].isdigit():
        j -= 1

    num=0
    while j < len(m[i]) and m[i][j].isdigit():
        num = num*10 + int(m[i][j])
        m[i][j] = '.'
        j += 1
    return num

def get_gear(i, j, m):
    nums = []
    for k in range(8):
        n = check(i-x[k], j-y[k], m)
        if n != 0:
            nums.append(n)
    return nums

gears = []
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] == '*':
            gears.append(get_gear(i, j, s.copy()))

print(gears)

ratio = []
for g in gears:
    if len(g) == 2:
        ratio.append(prod(g))

print(ratio)

print(sum(ratio))