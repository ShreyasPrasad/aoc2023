def both_stars_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    def get_max_occurrence(hand):
        occurrences = [0] * 5
        sorted_hand = sorted(hand)

        card_count = 1
        current_card = sorted_hand[0]
        num_js = 0

        for card in sorted_hand[1:]:
            if card == current_card:
                card_count += 1
            else:
                occurrences[card_count-1] += 1
                card_count = 1
                current_card = card

        for card in sorted_hand:
            if card == "J":
                num_js += 1
        
        occurrences[card_count-1] += 1
        
        # Scoring system is [7,6,5,4,3,2,1] 
        # where 7 is 5 a kind, 6 is a 4 of a kind, 5 is a full house, 4 is 3 of a kind, 3 is 2 pair, 2 is 1 pair, 1 is high card
        for i in range(4, -1, -1):
            if occurrences[i] > 0:
                if i == 4:
                    return 7
                elif i == 3:
                    if num_js == 1 or num_js == 4:
                        return 7
                    else:
                        return 6
                elif i == 2 and occurrences[i-1] > 0:
                    if num_js == 3 or num_js == 2:
                        return 7
                    elif num_js == 1:
                        return 6
                    else:
                        return 5
                elif i == 2:
                    if num_js == 1 or num_js == 3:
                        return 6
                    else:
                        return 4
                elif i == 1 and occurrences[i] > 1:
                    if num_js == 2:
                        return 6
                    elif num_js == 1:
                        return 5
                    else:
                        return 3
                elif i == 1:
                    if num_js == 1 or num_js == 2:
                        return 4
                    else:
                        return 2
                else:
                    if num_js == 1:
                        return 2
                    else:
                        return 1
            
        return -1

    def convert_hand_to_key(hand):
        card_map = {"J": "A", "2": 'B', "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", "T": "J", "Q": "K", "K": "L", "A": "M"}
        convert = ""
        for c in hand:
            convert += card_map[c]
        return convert

    def comparator(item):
        # A char element at index i represents that there are i+1 occurrences of that card in the hand
        return item[1]

    hands = []
    for line in lines:
        hand = line.split()[0]
        bet = int(line.split()[1])
        hands.append([hand, str(get_max_occurrence(hand)) + convert_hand_to_key(hand), bet])

    hands.sort(key = comparator)
        
    result = 0
    for i in range(len(hands)):
        rank = i + 1
        bet = hands[i][2]
        result += rank * bet
    
    print(result)

both_stars_solution()
