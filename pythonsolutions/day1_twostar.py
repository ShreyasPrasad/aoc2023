mapping = {
    # Digit strings
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    # Digits
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def two_star_solution():
    file = open('input', 'r')
    total = 0
    for line in file.readlines():
        lowest_str_index = -1
        highest_str_index = -1
        lowest_digit = 0 
        highest_digit = 0
        for (digit, value) in mapping.items():
            current_lowest_str_index = line.find(digit)
            if current_lowest_str_index != -1 and (lowest_str_index == -1 or current_lowest_str_index < lowest_str_index):
                lowest_str_index = current_lowest_str_index
                lowest_digit = value
            
            current_highest_str_index = line.rfind(digit)
            if current_highest_str_index != -1 and (highest_str_index == -1 or current_highest_str_index > highest_str_index):
                highest_str_index = current_highest_str_index
                highest_digit = value

        total += (lowest_digit * 10 + highest_digit)
        
    print(total)

two_star_solution()
            
