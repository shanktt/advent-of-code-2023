from typing import List
from collections import defaultdict

def get_pairs(lines) -> List[List[List[str]]]:
    numbers_only = [l.split(":")[1] for l in lines]
    pairs = [n.split("|") for n in numbers_only]
    pairs = [[pair[0].split(), pair[1].split()] for pair in pairs]

    return pairs

def part1(lines):
    total = 0

    """
    pairs is a list of lists where each sublist is a pair of lists that contain ints.
    pairs: List[List[List[str]]]. We would have a flatter structure with List[List[str]]
    but the converted the string of space separated numbers into lists

    So below *pairs would unpack pairs into List[List[str]], so we are zipping
    `n` List[List[str]] where each instance is a pair, and that's how we group together
    the winning and the actual numbers into their respective lists
    """
    # winning,actual = list(zip(*pairs))
    # print(all([len(set(w)) == len(w) for w in winning])) -> True
    # print(all([len(set(a)) == len(a) for a in actual])) -> True


    pairs = get_pairs(lines)
    for winning,actual in pairs:
        num_matches = len(set(winning) & set(actual))
        total += (2 ** (num_matches-1)) if num_matches else 0

    return total    

def part2(lines):
    pairs = get_pairs(lines)
    card_counts = defaultdict(int)

    for idx,(winning,actual) in enumerate(pairs, start=1):
        num_matches = len(set(winning) & set(actual))
        # You always have one of each card regardless of matches
        card_counts[idx] += 1
        for i in range(1,num_matches+1):
            card_counts[idx+i] += card_counts[idx]

    return sum(card_counts.values())