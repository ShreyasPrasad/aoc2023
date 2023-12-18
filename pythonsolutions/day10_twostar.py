
def get_loop_neighbors(grid, row, col):
    m = len(grid)
    n = len(grid[0])
    neighbors = []
    pipe = grid[row][col]

    if row + 1 < m \
        and (pipe == '|' or pipe == 'F' or pipe == '7' or pipe == 'S') \
        and (grid[row+1][col] == '|' or grid[row+1][col] == 'J' or grid[row+1][col] == 'L' or grid[row+1][col] == 'S'):
        neighbors.append([row+1, col])

    if row > 0 \
        and (pipe == '|' or pipe == 'J' or pipe == 'L' or pipe == 'S') \
        and (grid[row-1][col] == '|' or grid[row-1][col] == 'F' or grid[row-1][col] == '7' or grid[row-1][col] == 'S'):
        neighbors.append([row-1, col])

    if col + 1 < n \
        and (pipe == '-' or pipe == 'F' or pipe == 'L' or pipe == 'S') \
        and (grid[row][col+1] == '-' or grid[row][col+1] == 'J' or grid[row][col+1] == '7' or grid[row][col+1] == 'S'):
        neighbors.append([row, col+1])

    if col > 0 \
        and (pipe == '-' or pipe == 'J' or pipe == '7' or pipe == 'S') \
        and (grid[row][col-1] == '-' or grid[row][col-1] == 'F' or grid[row][col-1] == 'L' or grid[row][col-1] == 'S'):
        neighbors.append([row, col-1])

    return neighbors


def get_loop_map(grid, s_row, s_col):
    dict_map = {}
    key = "r" + str(s_row) + "c" + str(s_col)
    dict_map[key] = True

    starting_pipes = get_loop_neighbors(grid, s_row, s_col)
    previous_pipe = [s_row, s_col]
    current_pipe = starting_pipes[0]
    
    while grid[current_pipe[0]][current_pipe[1]] != 'S':
        key = "r" + str(current_pipe[0]) + "c" + str(current_pipe[1])
        dict_map[key] = True

        next_pipes = get_loop_neighbors(grid, current_pipe[0], current_pipe[1])
        if next_pipes[0][0] == previous_pipe[0] and next_pipes[0][1] == previous_pipe[1]:
            previous_pipe = current_pipe
            current_pipe = next_pipes[1]
        else:
            previous_pipe = current_pipe
            current_pipe = next_pipes[0]

    return dict_map

def find_enclosed_squares(grid, loop_map):
    m = len(grid)
    n = len(grid[0])
    count = 0

    # Create a new grid with expanded squares so we can detect paths inside the loop
    new_grid = [['#' for j in range(3*n)] for i in range(3*m)]

    for i in range(m):
       for j in range(n):
            key = "r" + str(i) + "c" + str(j)
            if key in loop_map:
                if grid[i][j] == "-":
                    new_grid[i*3+1][j*3] = '-'
                    new_grid[i*3+1][j*3+1] = '-'
                    new_grid[i*3+1][j*3+2] = '-'
                elif grid[i][j] == '|':
                    new_grid[i*3][j*3+1] = '|'
                    new_grid[i*3+1][j*3+1] = '|'
                    new_grid[i*3+2][j*3+1] = '|'
                elif grid[i][j] == '7':
                    new_grid[i*3+1][j*3] = '-'
                    new_grid[i*3+1][j*3+1] = '7'
                    new_grid[i*3+2][j*3+1] = '|'
                elif grid[i][j] == 'J':
                    new_grid[i*3+1][j*3] = '-'
                    new_grid[i*3+1][j*3+1] = 'J'
                    new_grid[i*3][j*3+1] = '|'
                elif grid[i][j] == 'L':
                    new_grid[i*3][j*3+1] = '|'
                    new_grid[i*3+1][j*3+1] = 'L'
                    new_grid[i*3+1][j*3+2] = '-'
                elif grid[i][j] == 'F':
                    new_grid[i*3+2][j*3+1] = '|'
                    new_grid[i*3+1][j*3+1] = 'F'
                    new_grid[i*3+1][j*3+2] = '-'
                elif grid[i][j] == 'S':
                    new_grid[i*3+1][j*3+1] = 'S'
                    key_up = key = "r" + str(i-1) + "c" + str(j)
                    if key_up in loop_map:
                        new_grid[i*3][j*3+1] = '|'
                    key_down = key = "r" + str(i+1) + "c" + str(j)
                    if key_down in loop_map:
                        new_grid[i*3+2][j*3+1] = '|'
                    key_left = key = "r" + str(i) + "c" + str(j-1)
                    if key_left in loop_map:
                        new_grid[i*3+1][j*3] = '-'
                    key_right = key = "r" + str(i) + "c" + str(j+1)
                    if key_right in loop_map:
                        new_grid[i*3+1][j*3+2] = '-'
            else:
                new_grid[i*3+1][j*3+1] = '.'
    
    # Fill non-enclosed squares with 'O'
    dfs_stack = []
    dfs_stack.append((0,0))

    while dfs_stack:
        i,j = dfs_stack.pop()
        if new_grid[i][j] not in "#.":
            continue
            
        new_grid[i][j] = 'O'
        # Check the 4 directions
        # Up
        if i > 0:
            dfs_stack.append((i-1, j))
        
        # Down
        if i < (len(new_grid) - 1):
            dfs_stack.append((i+1, j))

        # Left
        if j > 0:
            dfs_stack.append((i, j-1))

        # Right
        if j < (len(new_grid[0]) - 1):
            dfs_stack.append((i, j+1))

    # The remaining '.' characters are enclosed squares.
    enclosed_squares = sum([line.count('.') for line in new_grid])
    print(enclosed_squares)
    
def twostar_solution():
    file = open('input', 'r')

    grid = []
    lines = file.readlines()

    s_row = 0
    s_col = 0

    for (i, line) in enumerate(lines):
        line = line.strip()
        row = []
        for (j, c) in enumerate(line):
            if c == 'S':
                s_row = i
                s_col = j
            row.append(c)
        grid.append(row)

    # Find the loop and store it in a map
    loop_map = get_loop_map(grid, s_row, s_col)
    find_enclosed_squares(grid, loop_map)

twostar_solution()