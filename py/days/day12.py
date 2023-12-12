import re

# def is_valid(guess,constraint):
#     contigous_blocks = []
#     l = 0
#     r = 1
#     while r < len(guess):
#         if guess[l] != "#":
#             l += 1
#         if guess[l] == "#" and guess[r] != "#":
#             contigous_blocks.append(r-l)
#             while l != r:
#                 l += 1
#         r += 1

#     if guess[l] == guess[r-1] == "#":
#         contigous_blocks.append(r-l)
#     return contigous_blocks == constraint

def is_valid(guess,constraint):
    contigous_blocks = re.findall("#+", ''.join(guess))
    contigous_blocks = [len(c) for c in contigous_blocks]
    return contigous_blocks == constraint

def dfs(i: int, springs: list[str], constraint: list[int]):
    # print(f"{i} {springs}")
    if i >= len(springs):
        return int(is_valid(springs, constraint))
    if springs[i] == "?":
        springs[i] = "#"
        valid1 = dfs(i+1, springs, constraint)
        springs[i] = "."
        valid2 = dfs(i+1, springs, constraint)
        springs[i] = "?"
        return valid1+valid2
    else:
        return dfs(i+1, springs, constraint)

def part1(lines):
    total = 0
    for l in lines:
        springs, constraint = l.split(" ")
        constraint = [int(c) for c in constraint.split(",")]
        springs = list(springs)
        total += (dfs(0,springs,constraint))
        # total += int(is_valid(guess, constraint))
    
    return total

def part2(lines):
    return 0