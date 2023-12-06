from functools import reduce
from operator import mul

def part1(lines):
    color_to_num = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    total = 0
    for idx,line in enumerate(lines):
        game = line.split(":")[1].strip()
        flag = True

        for sub_game in game.split(";"):
            cubes = sub_game.split(",")

            for cube in cubes:
                num,color = cube.split()
                num = int(num)
                if color_to_num[color] < num:
                    flag = False
                    break

        if flag:
            total += (idx+1)

    return total

def part2(lines):
    total = 0
    for game in lines:
        sets = game.split(":")[1].strip()
        color_to_num = {
            "red": float('-inf'),
            "green": float('-inf'),
            "blue": float('-inf')
        }

        for set in sets.split(";"):
            cubes = set.split(",")

            for cube in cubes:
                num,color = cube.split()
                num = int(num)

                color_to_num[color] = max(color_to_num[color], num)
        total += reduce(mul, color_to_num.values(), 1)

    return total