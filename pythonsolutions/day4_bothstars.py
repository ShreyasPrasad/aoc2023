def one_star_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    for line in lines:
        all = line[(line.find(":") + 1):]
        winning = all.split("|")[0].split()
        numbers = all.split("|")[1].split()
        total += int(2 ** (len(list(set(winning).intersection(numbers))) - 1))

    print(total)

def two_star_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    cards_table = [1 for i in range(len(lines))]
    for i in range(0, len(lines)):
        line = lines[i]
        all = line[(line.find(":") + 1):]
        winning = all.split("|")[0].split()
        numbers = all.split("|")[1].split()
        matches = len(list(set(winning).intersection(numbers)))
        for j in range(matches):
            cards_table[i+j+1] += cards_table[i]

    total = sum(cards_table)
    print(total)


two_star_solution()