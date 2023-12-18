import sys
import numpy as np
import re

def get_input():
    direc_letter = {0:'R', 1:'D', 2:'L', 3:'U'}

    direcs = []
    for line in sys.stdin.readlines():
        hex = re.search(r'#(\w+)', line).group()
        trench, direc = int(hex[:-1].replace('#', '0x'), 16), direc_letter[int(hex[-1])]
        direcs.append((direc, trench))
    return direcs
def to_coords(direcs):
    dest = {'R': (0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    coord = np.array([0,0])
    points = [coord.copy()]
    for direc, trench in direcs:
        coord += trench * np.array(dest[direc])
        points.append(coord.copy())
    return points

def calc_area(coords):
    ROW, COL = 0, 1
    area = 0
    for i in range(len(coords)-1):
        r1, c1 = coords[i]
        r2, c2 = coords[i+1]
        if r2 > r1:
            subarea = r2-r1+1
        elif c2 < c1:
            subarea = (c1-c2)*(r1+1)
        elif c1 < c2:
            subarea = -(c2-c1)*r1
        else:
            subarea = 0
        print(f'> {r1},{c1} {r2},{c2} {subarea}')
        area += subarea
    return area

direcs = get_input()
print(direcs)

coords = to_coords(direcs)
print(coords)

area = calc_area(coords)
print(area)