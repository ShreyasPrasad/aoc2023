def onestar_solution(grid, starting):
    m = len(grid)
    n = len(grid[0])
    # Use a queue based search to explore the grid.
    explore = []
    explore.append(starting)
    covered = [["" for j in range(n)] for i in range(m)]

    while explore:
        i, j, dir = explore.pop(0)
        # Check for out of bounds.
        if i < 0 or i > m-1 or j < 0 or j > n-1:
            continue
        # Check if we have already traversed the tile.
        if dir in covered[i][j]:
            continue
        
        covered[i][j] += dir
        match dir:
            case 'R':
                match grid[i][j]:
                    case '\\':
                        explore.append((i+1, j, 'D'))
                    case '/':
                        explore.append((i-1, j, 'U'))
                    case '|':
                        explore.append((i-1, j, 'U'))
                        explore.append((i+1, j, 'D'))
                    case _:
                        explore.append((i, j+1, 'R'))
            
            case 'L':
                match grid[i][j]:
                    case '\\':
                        explore.append((i-1, j, 'U'))
                    case '/':
                        explore.append((i+1, j, 'D'))
                    case '|':
                        explore.append((i-1, j, 'U'))
                        explore.append((i+1, j, 'D'))
                    case _:
                        explore.append((i, j-1, 'L'))
            case 'U':
                match grid[i][j]:
                    case '\\':
                        explore.append((i, j-1, 'L'))
                    case '/':
                        explore.append((i, j+1, 'R'))
                    case '-':
                        explore.append((i, j-1, 'L'))
                        explore.append((i, j+1, 'R'))
                    case _:
                        explore.append((i-1, j, 'U'))
            case _:
                match grid[i][j]:
                    case '\\':
                        explore.append((i, j+1, 'R'))
                    case '/':
                        explore.append((i, j-1, 'L'))
                    case '-':
                        explore.append((i, j-1, 'L'))
                        explore.append((i, j+1, 'R'))
                    case _:
                        explore.append((i+1, j, 'D'))

    energized = 0
    for row in covered:
        for c in row:
            if c:
                energized += 1
    
    return energized

def twostar_solution(grid):
    m = len(grid)
    n = len(grid[0])
    max_energized = -1
    # Left and right column beam entrances
    for i in range(m):
        # Left column
        max_energized = max(max_energized, onestar_solution(grid, (i, 0, 'R')))
        # Right column
        max_energized = max(max_energized, onestar_solution(grid, (i, n-1, 'L')))

    # Up and down row beam entrances
    for j in range(n):
        # Upward row
        max_energized = max(max_energized, onestar_solution(grid, (0, j, 'D')))
        # Downward row
        max_energized = max(max_energized, onestar_solution(grid, (m-1, j, 'U')))

    print(max_energized)

def bothstars_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    grid = []
    for line in lines:
        current = []
        line = line.strip()
        for c in line:
            current.append(c)
        grid.append(current)

    twostar_solution(grid)

bothstars_solution()