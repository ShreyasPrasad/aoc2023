import heapq

UP = (-1,0)
DOWN = (1, 0)
LEFT = (0,-1)
RIGHT = (0,1)

"""
When we choose a direction to move in, we explore it as much as we possibly can.
This reduces the number of available movements to a maximum of 2 for each cell,
because the forward direction will already have been explored, and the reverse
direction is invalid. This means, the seen set in our algorithm only needs to 
keep track of cells and the direction used to reach them.
"""

def get_dirs(dir):
    match dir:
        case (0,0):
            return (DOWN, RIGHT)
        case (-1,0):
            return (LEFT, RIGHT)
        case (1,0):
            return (LEFT, RIGHT)
        case _:
            return (UP, DOWN)

def in_bounds(p, m, n):
    return p[0]>=0 and p[0]<=m-1 and p[1]>=0 and p[1]<=n-1

def twostar_solution_better_djikstra(grid, smin, smax):
    m = len(grid)
    n = len(grid[0])
    seen = set()
    core = [(0, (0,0), (0,0))]

    while core:
        c, p, d = heapq.heappop(core)
        if p == (m-1, n-1):
            return c

        if (p, d) in seen:
            continue
        
        seen.add((p, d))
        (px, py) = p
        for nd in get_dirs(d):
            (dx, dy) = nd
            nc = c
            for i in range(1, smax+1):
                np = (px + i*dx, py+i*dy)
                if not in_bounds(np, m, n):
                    continue
                nc += grid[np[0]][np[1]]
                if i >= smin:
                    heapq.heappush(core, (nc, np, nd))
                
def twostar_solution():
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

    print(twostar_solution_better_djikstra(grid, 4, 10))

twostar_solution()