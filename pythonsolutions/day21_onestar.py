import copy
"""

The idea is to perform DP to determine if a tile is reachable in an even or odd number
of steps from the start tile, or both. We iterate by the given number of steps so we
are only including possibly reachable tiles.

Let 'O' represent an odd-reachable tile and let 'E' represent an even-reachable tile.
Let 'EO' represent an even-odd-reachable tile.

After we perform DP, we observe the following rules for a tile at row i and column j:
1. If dp[i][j] = 'EO', then this tile can always be reached after the given number of steps.
Count it.
2. If dp[i][j] == 'O', then this tile can be reached if the step count is odd.
3. If dp[i][j] == 'E', then this tile can be reached if the step count is even.

Let 'N' denote a tile that is not reachable (all tiles at the beginning).

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
            
def onestar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    
    grid = []
    start_row = 0
    start_col = 0
    for (i, line) in enumerate(lines):
        line = line.strip()
        row = []
        for (j, c) in enumerate(line):
            row += c
            if c == 'S':
                start_row = i
                start_col = j
        grid.append(row)

    steps = 64
    dp = build_dp(grid, steps, start_row, start_col)
    print(get_num_tiles_reachable(dp, steps))

onestar_solution()