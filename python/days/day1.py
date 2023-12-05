def part1(lines):
    total = 0
    for l in lines:
        ints = [int(c) for c in l if c.isdigit()]
        total += (ints[0]*10) + ints[-1]

    return total

def part2(lines):
    str_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    total = 0
    for l in lines:
        ints = []
        for idx,c in enumerate(l):
            if c.isnumeric():
                ints.append(int(c))
                continue
            for key,value in str_to_int.items():
                if l[idx:idx+len(key)] == key:
                    ints.append(value)
                    continue

        total += (ints[0]*10) + ints[-1]

    return total