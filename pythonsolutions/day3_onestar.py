def one_star_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    for i in range(len(lines)):
        current = ""  
        lines[i] = lines[i].strip()
        lines[i] += "."  
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                current += lines[i][j]
            else:
                if current and check_surroundings_for_part(
                    lines[i-1] if i > 0 else None, 
                    lines[i], 
                    lines[i+1] if i < (len(lines) - 1) else None,
                    j - len(current),
                    len(current)):
                    total += int(current)
                current = ""

    print(total)

def check_surroundings_for_part(before, on, after, start, length):
    for i in range(length):
        if before and (before[start+i] != "." and not before[start+i].isdigit()):
            return True
        if after and (after[start+i] != "." and not after[start+i].isdigit()):
            return True
    
    if start > 0:
        if before and (before[start-1] != "." and not before[start-1].isdigit()):
            return True
        if on and (on[start-1] != "." and not on[start-1].isdigit()):
            return True
        if after and (after[start-1] != "." and not after[start-1].isdigit()):
            return True
    
    last = start + length
    if last < (len(on) - 1):
        if before and (before[last] != "." and not before[last].isdigit()):
            return True
        if on and (on[last] != "." and not on[last].isdigit()):
            return True
        if after and (after[last] != "." and not after[last].isdigit()):
            return True

    return False

one_star_solution()



