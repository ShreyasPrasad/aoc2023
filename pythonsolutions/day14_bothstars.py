def onestar_solution(line, index, total_rows, last_free_spot):
    weight = 0
    for i in range(len(line)):
        c = line[i]
        if c == "O":
            weight += total_rows - last_free_spot[i]
            last_free_spot[i] += 1
        elif c == "#":
            last_free_spot[i] = index + 1
    
    return weight

def get_grid_hash(grid):
    hash = ""
    for line in grid:
        for c in line:
            hash += c
    return hash

def hash_to_grid_support_weight(hash, m):
    # Build the grid from the hash
    grid = []
    for i in range(m):
        grid.append(hash[i*m:(i+1)*m])

    total = 0
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                total += (m-i)
    
    return total

def tilt_in_direction(grid, direction):
    m = len(grid)
    n = len(grid[0])
        
    match direction:
        case 'N':
            last_free_spot = [0 for i in range(n)]
            for i in range(m):
                for j in range(n):
                    c = grid[i][j]
                    if c == "O" and last_free_spot[j] != i:
                        grid[last_free_spot[j]][j] = "O"
                        last_free_spot[j] += 1
                        grid[i][j] = "."
                    elif c == "#" or (c == "O" and last_free_spot[j] == i):
                        last_free_spot[j] = i + 1
        case 'S':
            last_free_spot = [m-1 for i in range(n)]
            for i in range(m-1, -1, -1):
                for j in range(n):
                    c = grid[i][j]
                    if c == "O" and last_free_spot[j] != i:
                        grid[last_free_spot[j]][j] = "O"
                        last_free_spot[j] -= 1
                        grid[i][j] = "."
                    elif c == "#" or (c == "O" and last_free_spot[j] == i):
                        last_free_spot[j] = i - 1
        case 'W':
            last_free_spot = [0 for i in range(m)]
            for j in range(n):
                for i in range(m):
                    c = grid[i][j]
                    if c == "O" and last_free_spot[i] != j:
                        grid[i][last_free_spot[i]] = "O"
                        last_free_spot[i] += 1
                        grid[i][j] = "."
                    elif c == "#" or (c == "O" and last_free_spot[i] == j):
                        last_free_spot[i] = j + 1
        case _:
            last_free_spot = [n-1 for i in range(m)]
            for j in range(n-1, -1, -1):
                for i in range(m):
                    c = grid[i][j]
                    if c == "O" and last_free_spot[i] != j:
                        grid[i][last_free_spot[i]] = "O"
                        last_free_spot[i] -= 1
                        grid[i][j] = "."
                    elif c == "#" or (c == "O" and last_free_spot[i] == j):
                        last_free_spot[i] = j - 1
    
    return grid

def perform_cycle(grid):
    grid = tilt_in_direction(grid, 'N')
    grid = tilt_in_direction(grid, 'W')
    grid = tilt_in_direction(grid, 'S')
    grid = tilt_in_direction(grid, 'E')
    return grid

def twostar_solution(grid):
    hashes = {}
    one_billion = 1000000000
    for i in range(one_billion):
        grid = perform_cycle(grid)
        hash = get_grid_hash(grid)
        if hash in hashes:
            cycle_start = hashes[hash]
            cycle_end = i+1
            offset = (one_billion - cycle_start) % (cycle_end - cycle_start)
            for key in hashes.keys():
                if hashes[key] == cycle_start + offset:
                    return hash_to_grid_support_weight(key, len(grid))
        else:
            hashes[hash] = i+1
        
    return -1

def bothstars_solution():
    file = open('input', 'r')
    lines = file.readlines()
    grid = []

    for line in lines:
        line = [c for c in line.strip()]
        grid.append(line)
    
    print(twostar_solution(grid))

bothstars_solution()