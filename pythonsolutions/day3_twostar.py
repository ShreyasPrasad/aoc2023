def one_star_solution():
    file = open('input', 'r')
    lines = file.readlines()
    record = [[[] for i in range(len(lines[0]) + 1)] for j in range(len(lines))]

    for i in range(len(lines)):
        current = ""  
        lines[i] = lines[i].strip()
        lines[i] += "."  
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                current += lines[i][j]
            else:
                if current:
                    check_surroundings_for_gear(
                        lines,
                        i,
                        j - len(current),
                        len(current),
                        record,
                        int(current)
                    )
                current = ""

    total = 0
    for row in record:
        for counts in row:
            if len(counts) == 2:
                total += counts[0] * counts[1]

    print(total)

def check_surroundings_for_gear(lines, row, start, length, record, value):
    for i in range(length):
        if row > 0 and (lines[row-1][start+i] == "*"):
            record[row-1][start+i].append(value)
        if row < len(lines) - 1 and (lines[row+1][start+i] == "*"):
            record[row+1][start+i].append(value)
    
    if row > 0 and start > 0 and (lines[row-1][start-1] == "*"):
        record[row-1][start-1].append(value)
    
    if start > 0 and (lines[row][start-1] == "*"):
        record[row][start-1].append(value)
    
    if row < len(lines) - 1 and start > 0 and (lines[row+1][start-1] == "*"):
        record[row+1][start-1].append(value)

    last = start + length
    if row > 0 and last < len(lines[row]) and (lines[row-1][last] == "*"):
        record[row-1][last].append(value)

    if last < len(lines[row]) and (lines[row][last] == "*"):
        record[row][last].append(value)

    if row < len(lines) - 1 and last < len(lines[row]) and (lines[row+1][last] == "*"):
        record[row+1][last].append(value) 

one_star_solution()



