import numpy as np
import copy

def tilt_top(platform):
    platform = copy.deepcopy(platform)
    floor = [0] * len(platform[0])

    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == 'O':
                platform[i][j] = '.'
                platform[floor[j]][j] = 'O'
                floor[j] += 1
            if platform[i][j] == '#':
                floor[j] = i+1
    return platform

def calc_loads(platform):
    loads = 0
    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == 'O':
                loads += (len(platform) - i)
    return loads

def print_platform(platform):
    platform = copy.deepcopy(platform)

    for i in range(len(platform)):
        print(''.join(platform[i]))

    top = tilt_top(platform.copy())
    
    print(f'Loads: {calc_loads(platform)}')

    print()

def cycle(platform):
    platform = np.array(platform)
    hist = []
    loads = []
    while not platform.tolist() in hist:
        hist.append(platform.tolist())
        loads.append(calc_loads(platform))
        platform = tilt_top(platform)

        platform = np.rot90(platform, -1)
        platform = tilt_top(platform)
        platform = np.rot90(platform, -1)
        platform = tilt_top(platform)
        platform = np.rot90(platform, -1)
        platform = tilt_top(platform)
        platform = np.rot90(platform, -1)

    # for i in range(len(hist)):
    #     print(f'Cycle {i}: ')
    #     print_platform(hist[i].copy())
    # print(loads)

    cycles = 1000000000
    start_cycle = hist.index(platform.tolist())
    index = ((cycles - start_cycle) % (len(hist)-start_cycle))  + start_cycle
    print(index)
    return loads[index]

############# MAIN FUNCTION #############

platform = []
while True:
    try:
        line = list(input())
        platform.append(line)
    except EOFError:
        break

print(cycle(platform))
