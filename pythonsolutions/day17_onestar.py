import heapq

def onestar_solution_djikstra(grid):
    m = len(grid)
    n = len(grid[0])
    # Djiktras algorithm for a directed cyclic graph (TLE)
    # The core set
    
    # Elements are of the form: (total_heat, i, j, dir, steps, history)
    edges = [(grid[1][0], 1, 0, 'D', 1), (grid[0][1], 0, 1, 'R', 1)]
    heapq.heapify(edges)
    core = {}
    
    # Loop until we reach the destination tile, at the bottom right
    while True:
        # Select the edge with the least total weight and expand our core set to include it.
        (heat, i, j, dir, steps) = heapq.heappop(edges)
        # Termination condition
        if i == m-1 and j == n-1:
            return heat

        key = "r" + str(i) + "c" + str(j)+ "#" + dir + "#" + str(steps)
        if key in core:
            continue
        
        core[key] = True

        if dir == 'D':
            if j > 0:
                heapq.heappush(edges, (heat + grid[i][j-1], i, j-1, 'L', 1))
            if j < n-1:
                heapq.heappush(edges, (heat + grid[i][j+1], i, j+1, 'R', 1))
            if steps < 3 and i < m-1:
                heapq.heappush(edges, (heat + grid[i+1][j], i+1, j, 'D', steps + 1))

        elif dir == 'U':
            if j > 0:
                heapq.heappush(edges, (heat + grid[i][j-1], i, j-1, 'L', 1))
            if j < n-1:
                heapq.heappush(edges, (heat + grid[i][j+1], i, j+1, 'R', 1))
            if steps < 3 and i > 0:
                heapq.heappush(edges, (heat + grid[i-1][j], i-1, j, 'U', steps + 1))

        elif dir == 'L':
            if i > 0:
                heapq.heappush(edges, (heat + grid[i-1][j], i-1, j, 'U', 1))
            if i < m-1:
                heapq.heappush(edges, (heat + grid[i+1][j], i+1, j, 'D', 1))
            if steps < 3 and j > 0:
                heapq.heappush(edges, (heat + grid[i][j-1], i, j-1, 'L', steps + 1))

        elif dir == 'R':
            if i > 0:
                heapq.heappush(edges, (heat + grid[i-1][j], i-1, j, 'U', 1))
            if i < m-1:
                heapq.heappush(edges, (heat + grid[i+1][j], i+1, j, 'D', 1))
            if steps < 3 and j<n-1:
                heapq.heappush(edges, (heat + grid[i][j+1], i, j+1, 'R', steps + 1))

def onestar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    grid = []
    for line in lines:
        current = []
        line = line.strip()
        for c in line:
            current.append(int(c))
        grid.append(current)

    print(onestar_solution_djikstra(grid))

onestar_solution()