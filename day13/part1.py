import numpy as np

def print_pattern(pattern, left, right):
    middle = (left+right)//2
    print(middle, left, right)
    for i in range(len(pattern)):
        if i == left:
            print('\033[34m', end='')
        if i > right:
            print('\033[00m', end='')
        print(pattern[i])
    print('\033[00m')

def left_points(pattern):
    for i in range(len(pattern)-1):
        for j in range(len(pattern)):
            # print_pattern(pattern, i-j, i+j+1)
            if i-j < 0 or i+j+1 >= len(pattern):
                return (i+1)*100
            if pattern[i-j] != pattern[i+j+1]:
                break

    # transpose pattern
    pattern = np.transpose(pattern).tolist()
    for i in range(len(pattern)-1):
        for j in range(len(pattern)):
            # print_pattern(pattern, i-j, i+j+1)
            if i-j < 0 or i+j+1 >= len(pattern):
                return i+1
            if pattern[i-j] != pattern[i+j+1]:
                break
    return 0
            


########### MAIN ###########
acm = 0

pattern = []
while True:
    try:
        line = list(input())
        if line == []:
            p = left_points(pattern)
            print('response', p)
            acm += p
            pattern = []
        else:
            pattern.append(line)
    except EOFError:
        p = left_points(pattern)
        print('response', p)
        acm += p
        break

print(acm)
