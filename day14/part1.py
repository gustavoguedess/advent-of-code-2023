

def count_loads(platform):
    floor = [0] * len(platform[0])

    loads = 0
    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == 'O':
                loads += (len(platform) - floor[j])
                floor[j] += 1
            if platform[i][j] == '#':
                floor[j] = i+1
    return loads

############# MAIN FUNCTION #############

platform = []
while True:
    try:
        line = list(input())
        platform.append(line)
    except EOFError:
        break

print(count_loads(platform))