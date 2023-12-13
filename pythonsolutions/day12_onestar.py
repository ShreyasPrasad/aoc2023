acc = 0

def backtrack(line, numbers, index, current, count):
    global acc
    # Success
    if current == len(numbers) and index >= len(line):
        acc += 1
        return
    elif current == len(numbers) and (line[index] == "." or line[index] == "?"):
        backtrack(line, numbers, index + 1, current, count)
        return
    # Early Termination
    elif index >= len(line) or current == len(numbers):
        return
    
    if line[index] == ".":
        if count > 0:
            return
        backtrack(line, numbers, index+1, current, 0)
    elif line[index] == "?": # Consider a ?
        # Treat as . sometimes.
        if count == 0:
            backtrack(line, numbers, index+1, current, 0)
        # Treat as # always.
        count += 1
        if count < numbers[current]:
            backtrack(line, numbers, index+1, current, count)
        else:
            # This ? can complete a grouping, so we check if it is valid by looking at the next char.
            if index == len(line) - 1:
                backtrack(line, numbers, index+1, current+1, 0)
            elif line[index+1] == "?" or line[index+1] == ".":
                backtrack(line, numbers, index+2, current+1, 0)
            else:
                return
    else: 
        if count + line[index] < numbers[current]:
            backtrack(line, numbers, index+1, current, count + line[index])
        # Treat the next character as a . and skip it, regardless of it is a ?
        elif count + line[index] == numbers[current]:
            backtrack(line, numbers, index+2, current+1, 0)
        else:
            return

def one_star_solution():
    global acc
    file = open('input', 'r')
    total = 0
    lines = file.readlines()
    n = len(lines)
    linecount = 1

    for line in lines:
        line = line.strip()
        record = line.split()[0]
        numbers = line.split()[1].split(",")
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])

        converted = []
        count = 0
        for c in record:
            if c == "#":
                count += 1
            else:
                if count > 0:
                    converted.append(count)
                converted.append(c)
                count = 0
        
        if count > 0:
            converted.append(count)


        backtrack(converted, numbers, 0, 0, 0)
        total += acc
        acc = 0

        
    print(total)

one_star_solution()