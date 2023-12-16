
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

def beam_moviment(x, y, direc):
    visited = []
    for _ in range(len(contraption)):
        visited.append([[] for _ in range(len(contraption[0]))])

    queue = [(x, y, direc)]
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

    
    acm = 0
    for line in visited:
        for v in line:
            if v:
                acm += 1
    print(acm)
    return acm
################ MAIN ################

contraption = []
visited = []

with open('in', 'r') as f:
    for line in f:
        contraption.append(list(line.strip()))
print(visited)

max_acm = 0
for x in range(len(contraption[0])):
    max_acm = max(max_acm, beam_moviment(x, 0, 'D'))
    max_acm = max(max_acm, beam_moviment(x, len(contraption)-1, 'T'))
for y in range(len(contraption)):
    max_acm = max(max_acm, beam_moviment(0, y, 'R'))
    max_acm = max(max_acm, beam_moviment(len(contraption[0])-1, y, 'L'))
print(max_acm)