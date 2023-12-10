
grid = []
visited = []

# get positions of pipes that are connected to given pipe
def next(i, j, visited):
    if grid[i][j] == '|' and not visited[i-1][j]: return i-1, j
    if grid[i][j] == '|' and not visited[i+1][j]: return i+1, j
    if grid[i][j] == '-' and not visited[i][j-1]: return i, j-1
    if grid[i][j] == '-' and not visited[i][j+1]: return i, j+1
    if grid[i][j] == 'L' and not visited[i-1][j]: return i-1, j
    if grid[i][j] == 'L' and not visited[i][j+1]: return i, j+1
    if grid[i][j] == 'J' and not visited[i-1][j]: return i-1, j
    if grid[i][j] == 'J' and not visited[i][j-1]: return i, j-1
    if grid[i][j] == '7' and not visited[i+1][j]: return i+1, j
    if grid[i][j] == '7' and not visited[i][j-1]: return i, j-1
    if grid[i][j] == 'F' and not visited[i+1][j]: return i+1, j
    if grid[i][j] == 'F' and not visited[i][j+1]: return i, j+1
    return -1, -1

def left_hand_side(i, j, visited):
    if grid[i][j] == '|' and visited[i-1][j]: return [(i, j+1)]
    if grid[i][j] == '|' and visited[i+1][j]: return [(i, j-1)]
    if grid[i][j] == '-' and visited[i][j-1]: return [(i-1, j)]
    if grid[i][j] == '-' and visited[i][j+1]: return [(i+1, j)]
    if grid[i][j] == 'L' and visited[i-1][j]: return []
    if grid[i][j] == 'L' and visited[i][j+1]: return [(i+1, j), (i, j-1)]
    if grid[i][j] == 'J' and visited[i-1][j]: return [(i, j+1), (i+1, j)]
    if grid[i][j] == 'J' and visited[i][j-1]: return []
    if grid[i][j] == '7' and visited[i+1][j]: return []
    if grid[i][j] == '7' and visited[i][j-1]: return [(i-1, j), (i, j+1)]
    if grid[i][j] == 'F' and visited[i+1][j]: return [(i, j+1), (i-1, j)]
    if grid[i][j] == 'F' and visited[i][j+1]: return []
    return []

def right_hand_side(i, j, visited):
    if grid[i][j] == '|' and visited[i-1][j]: return [(i, j-1)]
    if grid[i][j] == '|' and visited[i+1][j]: return [(i, j+1)]
    if grid[i][j] == '-' and visited[i][j-1]: return [(i+1, j)]
    if grid[i][j] == '-' and visited[i][j+1]: return [(i-1, j)]
    if grid[i][j] == 'L' and visited[i-1][j]: return [(i, j-1), (i+1, j)]
    if grid[i][j] == 'L' and visited[i][j+1]: return []
    if grid[i][j] == 'J' and visited[i-1][j]: return []
    if grid[i][j] == 'J' and visited[i][j-1]: return [(i+1, j), (i, j+1)]
    if grid[i][j] == '7' and visited[i+1][j]: return [(i, j+1), (i-1, j)]
    if grid[i][j] == '7' and visited[i][j-1]: return []
    if grid[i][j] == 'F' and visited[i+1][j]: return []
    if grid[i][j] == 'F' and visited[i][j+1]: return [(i-1, j), (i, j-1)]
    return []

def fill(i, j, ch='X'):
    if grid[i][j] != '.':
        return 0
    
    print(f'filling with {ch}: ', end='')
    count = 0
    queue = set()
    queue.add((i, j))
    while queue:
        i, j = queue.pop()
        grid[i][j] = ch
        count += 1
        print((i, j), end=' ')
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii]):
                if grid[ii][jj] == '.':
                    queue.add((ii, jj))
    print()
    return count

def dfs(i, j):
    left_hand_count = 0
    right_hand_count = 0

    path = [(i, j)]
    visited[i][j] = True
    i+=1
    while (i, j) != (-1, -1):
        visited[i][j] = True
        path.append((i, j))
        # print(i, j, grid[i][j])
        left = left_hand_side(i, j, visited)
        for ii, jj in left:
            if ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii]):
                left_hand_count += fill(ii, jj, ch='I')
    
        right = right_hand_side(i, j, visited)
        for ii, jj in right:
            if ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii]):
                right_hand_count += fill(ii, jj, ch='O')

        i, j = next(i, j, visited)

    return path, left_hand_count, right_hand_count

def print_grid():
    for line in grid:
        print(''.join(line))
    print()

def get_start():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return i, j
    return -1, -1

def remove_pipe_outside_path():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not visited[i][j]:
                grid[i][j] = '.'

############# MAIN #################

while True:
    try:
        line = input()
        print(line)
        grid.append(list(line))
    except EOFError:
        break
print()

start = get_start()

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
path, left_hand_count, right_hand_count = dfs(*start)

remove_pipe_outside_path()
print_grid()

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
path, left_hand_count, right_hand_count = dfs(*start)

print_grid()

# print(path)
print(len(path), left_hand_count, right_hand_count)
