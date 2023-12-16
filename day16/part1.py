
def continue_direc(x, y, dir):
    if dir == 'T':
        return x, y - 1
    elif dir == 'D':
        return x, y + 1
    elif dir == 'L':
        return x - 1, y
    elif dir == 'R':
        return x + 1, y

def continue_mirror(x, y, dir, mirror):
    if mirror == '/':
        if dir == 'T':
            return x + 1, y, 'R'
        elif dir == 'D':
            return x - 1, y, 'L'
        elif dir == 'L':
            return x, y + 1, 'D'
        elif dir == 'R':
            return x, y - 1, 'T'
    elif mirror == '\\':
        if dir == 'T':
            return x - 1, y, 'L'
        elif dir == 'D':
            return x + 1, y, 'R'
        elif dir == 'L':
            return x, y - 1, 'T'
        elif dir == 'R':
            return x, y + 1, 'D'

def print_debug(x, y, dir):
    for i in range(len(contraption)):
        for j in range(len(contraption[i])):
            if i == y and j == x:
                print(f'\033[95m{contraption[i][j]}\033[0m', end='')
            else:
                print(contraption[i][j], end='')
        print()

def beam_moviment():
    queue = [(0, 0, 'R')]
    while queue:
        x, y, direc = queue.pop()
        if x < 0 or y < 0 or y >= len(contraption) or x >= len(contraption[0]):
            continue
        if direc in visited[y][x]:
            continue
        visited[y][x].append(direc)
        print(x,y,direc, contraption[y][x])
        # print_debug(x, y, direc)
        # breakpoint()
        if contraption[y][x] == '.':
            x, y = continue_direc(x, y, direc)
            queue.append((x, y, direc))
        elif contraption[y][x] == '-' and (direc=='T' or direc=='D'):
            queue.append((x-1, y, 'L'))
            queue.append((x+1, y, 'R'))
        elif contraption[y][x] == '|' and (direc=='L' or direc=='R'):
            queue.append((x, y-1, 'T'))
            queue.append((x, y+1, 'D'))
        elif contraption[y][x] == '/' or contraption[y][x] == '\\':
            x, y, direc = continue_mirror(x, y, direc, contraption[y][x])
            queue.append((x, y, direc))
        else:
            x, y = continue_direc(x, y, direc)
            queue.append((x, y, direc))
################ MAIN ################

contraption = []
visited = []

with open('in', 'r') as f:
    for line in f:
        contraption.append(list(line.strip()))
        visited.append([[] for _ in range(len(line.strip()))])
print(visited)
beam_moviment()

acm = 0
for line in visited:
    for v in line:
        if v:
            acm += 1

for line in visited:
    for v in line:
        if v:
            print('#', end='')
        else:
            print('.', end='')  
    print()
print(acm)