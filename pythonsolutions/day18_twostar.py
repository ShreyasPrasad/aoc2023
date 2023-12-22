"""
Use pick's theorem and the shoelace algorihtm to compute the number of interior points
in the polygon formed by the digging.
Pick's theorem states that A = I + B/2 - 1, where I is the number of interior points,
B is the number of boundary points, and A is the internal area.
Rearranging gives I = A - B/2 + 1, but we really want the I + B (we count both the interior
and border in our sum).

So we finally obtain I + B = A + B/2 + 1. 

1. B/2 is easy to calculate by summing the given distances.
2. A can be obtained by using the shoelace method, which finds the area of a polygon described
   by its coordinates.
"""

def find_border_length(points):
    border = 0
    for (_, dis) in points:
        border += dis
    return border

def find_area(points):
    area = 0
    x = 0
    y = 0
    for (dir, dis) in points:
        prevx, prevy = x,y
        if dir == 0:
            x += dis
        elif dir == 1:
            y += dis
        elif dir == 2:
            x -= dis
        else:
            y -= dis
        area += ((prevx * y) - (prevy * x))
    return area/2

def get_num_interior_points(points):
    area = find_area(points)
    border_len = find_border_length(points)

    return int(area + border_len/2 + 1)

def twostar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    points = []

    for line in lines:
        line = line.strip()
        hex = line.split(" ")[-1]
        distance = int(hex[2:-2], 16)
        dir = int(hex[-2])
        points.append([dir, distance])    

    print(get_num_interior_points(points))

twostar_solution()
