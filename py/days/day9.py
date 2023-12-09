from functools import reduce

def get_next_value(nums):
    diffs = [nums]
    while not all([n == 0 for n in nums]):
        d = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        diffs.append(d)
        nums = d
    return sum([d[-1] for d in diffs])


def part1(lines):
    total = 0

    for l in lines:
        nums = [int(l) for l in l.split()]
        total += get_next_value(nums)
        
    return total


def get_previous_value(nums):
    diffs = [nums]
    while not all([n == 0 for n in nums]):
        d = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        diffs.append(d)
        nums = d

    # In ocaml we would return List.fold_right (fun x acc -> x - acc) [10;3;0;2;0] 0;;
    # Which is 10-(3-(0-(2-(0-0))))
    # We need to convert this to a fold left since python doesn't have built in fold right
    # So reverse the list and modify function as necessary, since substraction isn't communative
    # The function passed to functools.reduce has signature acc,next_val

    diffs = [d[0] for d in diffs]
    return reduce(lambda acc, x: x - acc, reversed(diffs))
    
def part2(lines):
    total = 0

    for l in lines:
        nums = [int(l) for l in l.split()]
        total += get_previous_value(nums)

    return total