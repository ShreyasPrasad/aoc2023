def one_star_solution():
    file = open('input', 'r')
    total = 0
    line_num = 1
    for line in file.readlines():
        hands_in_game = line[(line.find(":") + 1):].split(";")
        bad_pair_found = False
        for hand in hands_in_game:
            pairs = hand.split(",")
            for pair in pairs:
                pair = pair.strip()
                if pair.endswith("green") and int(pair[0:-5]) > 13 \
                    or pair.endswith("blue") and int(pair[0:-4]) > 14 \
                    or pair.endswith("red") and int(pair[0:-3]) > 12:
                        bad_pair_found = True
        if not bad_pair_found:
            total += line_num
        line_num += 1
    print(total)

def two_star_solution():
    file = open('input', 'r')
    total = 0
    line_num = 1
    for line in file.readlines():
        hands_in_game = line[(line.find(":") + 1):].split(";")
        max_green = 0
        max_blue = 0
        max_red = 0
        for hand in hands_in_game:
            pairs = hand.split(",")
            for pair in pairs:
                pair = pair.strip()
                if pair.endswith("green"):
                    max_green = max(max_green, int(pair[0:-5]))
                elif pair.endswith("blue"):
                    max_blue = max(max_blue, int(pair[0:-4]))
                else:
                    max_red = max(max_red, int(pair[0:-3]))

        total += (max_blue * max_green * max_red)
    
    print(total)

two_star_solution()
    
           