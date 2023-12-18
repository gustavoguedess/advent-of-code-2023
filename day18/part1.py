import sys

def print_terrain(terrain):
    for row in terrain:
        print(''.join(row))
    print()

def fill_trench(terrain, direcs):
    area = 0
    c,r = SIZE//2, SIZE//2
    terrain[r][c] = '#'

    direc_dest = {'R': (0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    for direc, trench in direcs:
        for i in range(trench):
            area += 1
            dr, dc = direc_dest[direc]
            c,r = c+dc, r+dr
            try:
                terrain[r][c] = '#'
            except IndexError:
                print('Out of bounds at', r, c)
    return area

def calc_area(terrain, r, c):
    area = 0
    queue = [(r,c)]
    while queue:
        r,c = queue.pop()
        if terrain[r][c] == '.':
            terrain[r][c] = '#'
            area += 1
            queue.extend([(r-1,c), (r+1,c), (r,c-1), (r,c+1)])
    return area
################# MAIN #################
SIZE = 1000
terrain = [list('.'*SIZE) for _ in range(SIZE)]

sys.setrecursionlimit(100000)
lines = sys.stdin.readlines()

direcs = []
for line in lines:
    direc, trench, _ = line.split()
    trench = int(trench)
    direcs.append((direc, trench))

# print_terrain(terrain)
area_trench = fill_trench(terrain, direcs)
# print_terrain(terrain)

area_inside = calc_area(terrain, SIZE//2+1, SIZE//2+1)
# print_terrain(terrain)
print('Area of trench:', area_trench)
print('Area inside:', area_inside)
print('Total area:', area_trench + area_inside)