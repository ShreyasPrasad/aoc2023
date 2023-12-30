import copy
"""

Some BS quadratic formula stuff since the input is shaped like a diamond and
there is a empty row and column passing through the S. All the reachable tiles
can be determined from the first grid, allowing this quadratic formula to work.

Use the first 3 points (65, y1), (196, y2) and (327, y3) to determine the coefficients
of this quadratic. We increment by 131 steps each time for the x coordinates because
that is the length of the grid. We use the onestar solution to calculate the y
coordinates in each case.
"""

def in_bounds(i, j, m, n):
    return i >= 0 and j >= 0 and i < m and j < n 

def get_new_dp_value(dp, i, j, m, n):
    if dp[i][j] == 'EO':
        return
    
    is_odd = False
    is_even = False
    for (ic, jc) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if in_bounds(ic, jc, m, n):
            if 'O' in dp[ic][jc]:
                is_even = True
            if 'E' in dp[ic][jc]:
                is_odd = True
    
    if is_odd and is_even:
        return 'EO'
    elif is_odd:
        return 'O'
    elif is_even:
        return 'E'
    else:
        return 'N'

def get_num_tiles_reachable(dp, steps):
    count = 0
    for row in dp:
        for val in row:
            if 'E' in val and steps%2 == 0:
                count+=1
            elif 'O' in val and steps%2 == 1:
                count+=1
    return count

def build_dp(grid, steps, start_row, start_col):
    m = len(grid)
    n = len(grid[0])

    dp = [['N' for j in range(n)] for i in range(m)]
    dp[start_row][start_col] = 'E'

    for k in range(steps):
        new_dp = copy.deepcopy(dp)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    new_dp[i][j] = get_new_dp_value(dp, i, j, m, n)
        dp = new_dp

    return dp
            
def twostar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    
    grid = []
    start_row = 327
    start_col = 327
    for (i, line) in enumerate(lines):
        line = line.strip()
        row = []
        for (j, c) in enumerate(line):
            if c == 'S':
                row += '.'
            else:
                row += c
        grid.append(row + copy.deepcopy(row) + copy.deepcopy(row) + copy.deepcopy(row) + copy.deepcopy(row))

    steps = 327
    grid += (copy.deepcopy(grid) + copy.deepcopy(grid) + copy.deepcopy(grid) + copy.deepcopy(grid))
    grid[start_row][start_col] = 'S'
    dp = build_dp(grid, steps, start_row, start_col)
    print(get_num_tiles_reachable(dp, steps))

twostar_solution()