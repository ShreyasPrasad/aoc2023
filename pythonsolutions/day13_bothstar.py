def count_row_diffs(grid, row1, row2):
    count = 0
    n = len(grid[0])
    for j in range(n):
        if grid[row1][j] != grid[row2][j]:
            count += 1
    return count

def count_column_diffs(grid, col1, col2):
    count = 0
    m = len(grid)
    for i in range(m):
        if grid[i][col1] != grid[i][col2]:
            count += 1
    return count

def onestar_solution(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(1,m):
        bottom = i - 1
        top = i
        while bottom >= 0 and top < m:
            if not count_row_diffs(grid, bottom, top):
                bottom -= 1
                top += 1
            else:
                break
        if bottom == -1:
            return int((top-bottom)/2)*100
        elif top == m:
            return int(bottom + (top - bottom + 1)/2)*100

    for j in range(1,n):
        bottom = j - 1
        top = j
        while bottom >= 0 and top < n:
            if not count_column_diffs(grid, bottom, top):
                bottom -= 1
                top += 1
            else:
                break
        if bottom == -1:
            return int((top-bottom)/2)
        elif top == n:
            return int(bottom + (top - bottom + 1)/2)
    
    return 0

def twostar_solution(grid):
    # Try to insert a horizontal line at every possible point
    m = len(grid)
    n = len(grid[0])
    solution = onestar_solution(grid)

    for i in range(1,m):
        one_diff_found = False
        bottom = i - 1
        top = i
        while bottom >= 0 and top < m:
            if not count_row_diffs(grid, bottom, top):
                bottom -= 1
                top += 1
            elif count_row_diffs(grid, bottom, top) == 1 and not one_diff_found:
                bottom -= 1
                top += 1
                one_diff_found = True
            else:
                break
        
        if one_diff_found:
            if bottom == -1 and int(solution/100) != int((top-bottom)/2):
                return int((top-bottom)/2)*100
            elif top == m and int(solution/100) != int(bottom + (top - bottom + 1)/2):
                return int(bottom + (top - bottom + 1)/2)*100

    for j in range(1,n):
        one_diff_found = False
        bottom = j - 1
        top = j
        while bottom >= 0 and top < n:
            if not count_column_diffs(grid, bottom, top):
                bottom -= 1
                top += 1
            elif count_column_diffs(grid, bottom, top) == 1 and not one_diff_found:
                bottom -= 1
                top += 1
                one_diff_found = True
            else:
                break

        if one_diff_found:
            if bottom == -1 and solution != int((top-bottom)/2):
                return int((top-bottom)/2)
            elif top == n and solution != int(bottom + (top - bottom + 1)/2):
                return int(bottom + (top - bottom + 1)/2)
    
    return -1


def bothstar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    grid = []
    total = 0
    
    for line in lines:
        line = line.strip()
        # Process the current pattern
        if not line:
            total += twostar_solution(grid)
            grid.clear()
        else:
            grid.append(line)
    
    if line:
        total += twostar_solution(grid)

    print(total)

bothstar_solution()