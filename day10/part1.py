
grid = []
visited = []

# get positions of pipes that are connected to given pipe
def connections(i, j):
    match grid[i][j]:
        case '|': return [(i-1, j), (i+1, j)]
        case '-': return [(i, j-1), (i, j+1)]
        case 'L': return [(i, j+1), (i-1, j)]
        case 'J': return [(i, j-1), (i-1, j)]
        case '7': return [(i, j-1), (i+1, j)]
        case 'F': return [(i+1, j), (i, j+1)]
        case '.': return []
        case 'S': 
            _neighbor = []
            for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (i, j) in connections(ii, jj):
                    _neighbor.append((ii, jj))
            return _neighbor
        case _  : return []


def dfs(i, j):
    path = []
    while grid[i][j] != 'S' or len(path)==0:
        visited[i][j] = True
        path.append((i, j))
        _neighbor = connections(i, j)
        print(f'pipe: {grid[i][j]}  x: {i}, y: {j}, neighbor: {_neighbor}')
        for ii,jj in _neighbor:
            if grid[ii][jj] == 'S' and len(path) > 2:
                return path
            if not visited[ii][jj]:
                i, j = ii, jj
                break
        
    return path
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            path = dfs(i, j)
            break
print(path)
print(len(path))
print(len(path)//2)