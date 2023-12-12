def both_stars_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()
    n = len(lines)

    for i in range(n):
        lines[i] = lines[i].strip()

    m = len(lines[0])

    rows = [0 for i in range(n)]
    for (i, line) in enumerate(lines):
        space = 0
        for c in line:
            if c != "#":
                space += 1

        if space == m:
            if i == 0:
                rows[i] = 999999
            else:
                rows[i] = 999999 + rows[i-1]
        else:
            rows[i] = rows[i-1]

    cols = [0 for i in range(m)]
    for i in range(m):
        space = 0
        for j in range(n):
            if lines[j][i] != "#":
                space += 1

        if space == m:
            if i == 0:
                cols[i] = 999999
            else:
                cols[i] = 999999 + cols[i-1]
        else:
            cols[i] = cols[i-1]

    coords = []
    for (i, line) in enumerate(lines):
        for (j, c) in enumerate(line):
            if c == "#":
                coords.append([i + rows[i], j + cols[j]])
            
    k = len(coords)
    total = 0
    for i in range(k):
        for j in range(i+1, k):
            total += abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1]) 
    
    print(total)

both_stars_solution()