from collections import Counter
from functools import cmp_to_key

TYPES_OF_HANDS = 7

def insert_hand(buckets, hand_n_bid, modified_hand = None):
    hand,_ = hand_n_bid
    if modified_hand:
        hand = modified_hand
    unique_cards = len(set(hand))

    # high card : 5
    # one pair: 4
    # two pair: 3
    # three of a kind: 3
    # full house: 2
    # four of a kind: 2
    # five of a kind: 1
    if unique_cards == 1:
        buckets[-1].append(hand_n_bid)
    elif unique_cards == 4:
        buckets[1].append(hand_n_bid)
    elif unique_cards == 5:
        buckets[0].append(hand_n_bid)
    elif unique_cards == 3:
        if max(Counter(hand).values()) == 3:
            buckets[3].append(hand_n_bid)
        else:
            buckets[2].append(hand_n_bid)
    elif unique_cards == 2:
        if max(Counter(hand).values()) == 4:
            buckets[5].append(hand_n_bid)
        else:
            buckets[4].append(hand_n_bid)

def create_comparator(card_rank):
    def compare_hands(hand_n_bid1, hand_n_bid2):
        hand1 = hand_n_bid1[0]
        hand2 = hand_n_bid2[0]

        for c1,c2 in zip(hand1,hand2):
            if card_rank[c1] < card_rank[c2]:
                return 1
            elif card_rank[c1] > card_rank[c2]:
                return -1
    return compare_hands

def part1(lines: str):
    # buckets for each type of hand.
    # starting from high card, one pair, ... , five of a kind
    buckets = [[] for _ in range(TYPES_OF_HANDS)]
    card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    card_rank = {c:idx for idx,c in enumerate(card_order)}

    for l in lines:
        hand_n_bid = l.split()
        hand_n_bid[1] = int(hand_n_bid[1])

        insert_hand(buckets, hand_n_bid)

    total = 0
    cur_rank = 1
    for b in buckets:
        b.sort(key=cmp_to_key(create_comparator(card_rank)))
        for _,bid in b:
            total += (cur_rank * bid)
            cur_rank += 1
    

    return total

def part2(lines):
    buckets = [[] for _ in range(TYPES_OF_HANDS)]
    card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    card_rank = {c:idx for idx,c in enumerate(card_order)}

    for l in lines:
        hand_n_bid = l.split()
        hand_n_bid[1] = int(hand_n_bid[1])
        hand_count = Counter(hand_n_bid[0])
        modified_hand = None
        if 'J' in hand_count:
            hand_count = sorted(hand_count.items(), key=lambda x: x[1], reverse=True)
            highest_non_J = (None,0)
            for char,count in hand_count:
                if char != "J":
                    highest_non_J = (char,count)
                    break

            if highest_non_J[0]:
                modified_hand = hand_n_bid[0].replace("J", char)


        insert_hand(buckets, hand_n_bid, modified_hand=modified_hand if modified_hand else None)

    total = 0
    cur_rank = 1
    for b in buckets:
        b.sort(key=cmp_to_key(create_comparator(card_rank)))
        for _,bid in b:
            total += (cur_rank * bid)
            cur_rank += 1
    

    return total