def onestar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0
    grid = [['.' for i in range(2500)] for j in range(2500)]

    # Start at 1 column and 1row below.
    # Mark dug cubes with a #
    x = 500
    y = 500
    grid[x][y] = "#"

    for line in lines:
        line = line.strip().split(" ")
        dir = line[0]
        steps = int(line[1])
        for i in range(steps):
            match dir:
                case 'L':
                    y-=1
                case 'R':
                    y+=1
                case 'U':
                    x-=1
                case _:
                    x+=1
            grid[x][y] = '#'

    flood = [(0,0)]

    count = 0
    while flood:
        (i, j) = flood.pop()
        if grid[i][j] == '.':
            grid[i][j] = 'O'
        else:
            continue

        if i>0 and grid[i-1][j] == '.':
            flood.append((i-1, j))
        if i + 1 < len(grid) and grid[i+1][j] == '.':
            flood.append((i+1, j))
        if j>0 and grid[i][j-1] == '.':
            flood.append((i, j-1))
        if j + 1 < len(grid[0]) and grid[i][j+1] == '.':
            flood.append((i, j+1))

    lagoon_size = 0
    for i in range(2500):
        for j in range(2500):
            if grid[i][j] != 'O':
                lagoon_size+=1

    print(lagoon_size)
        
onestar_solution()