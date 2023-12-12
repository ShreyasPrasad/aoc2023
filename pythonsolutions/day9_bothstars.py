import math

def one_star_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    def get_placeholders_sum(seq):
        new_seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
        if all(value == 0 for value in seq):
            return seq[0]
        else:
            return seq[0] - get_placeholders_sum(new_seq)

    total = 0
    for line in lines:
        seq = [int(value) for value in line.split()]
        total += get_placeholders_sum(seq)

    print(total)

one_star_solution()
