import sys
from collections import Counter
from itertools import product

def hand_val(hand):
    count_cnt = Counter(Counter(hand).values())

    if 5 in count_cnt:
        return 7 # 5 of a kind
    elif 4 in count_cnt:
        return 6 # 4 of a kind
    elif 3 in count_cnt:
        if 2 in count_cnt:
            return 5 # full house
        else:
            return 4 # three of a kind
    elif 2 in count_cnt:
        if count_cnt[2] == 2:
            return 3 # two pair
        else:
            return 2 # one pair
    else:
        return 1 # high card

def jokerhand_vals(hand, jokers):
    my_hand = hand.copy()
    for it in product(range(2, 15), repeat=len(jokers)):
        for i in range(len(jokers)):
            my_hand[jokers[i]] = it[i]
        yield hand_val(my_hand)

def main():
    card_value = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    card_value2 = card_value.copy()
    card_value2['J'] = 1

    cards = []
    cards2 = []
    with open(sys.argv[1]) as f:
        for line in f:
            toks = line.rstrip().split(' ')
            hand = [card_value[c] for c in toks[0]]
            hand2 = [card_value2[c] for c in toks[0]]
            val = hand_val(toks[0])
            bid = int(toks[1])
            cards.append((val, hand, bid))
            cards2.append((val, hand2, bid))

    ranking = sorted(cards)
    part1 = sum([ranking[i][2] * (i+1) for i in range(len(ranking))])
    print('Part 1:', part1)

    joker_cards = []
    for val, hand, bid in cards2:
        jokers = [i for i in range(len(hand)) if hand[i] == 1]
        if jokers:
            val = max(jokerhand_vals(hand, jokers))
        joker_cards.append((val, hand, bid))

    ranking2 = sorted(joker_cards)
    part2 = sum([ranking2[i][2] * (i+1) for i in range(len(ranking2))])
    print('Part 2:', part2)

main()
