import re
from collections import defaultdict
from typing import List

def lines_to_grid(lines) -> List[List[str]]:
    return [[*line] for line in lines]

def get_bounding_box(start, end, row_num) -> List[List[int]]:
    """
    Get the coords of the "bounding" box for the string on row `row_num`
    that spans `start` and `end`

    Example for `35` marked by `*`

    ..........
    .****.....
    .*35*.....
    .****.....
    """

    coords = []
    
    # leftmost, rightmost boundary
    coords.append([row_num, start-1])
    coords.append([row_num, end+1])

    # diagonals
    coords.append([row_num-1, start-1])
    coords.append([row_num+1, start-1])
    coords.append([row_num-1, end+1])
    coords.append([row_num+1, end+1])


    # upper and lower boundary
    for i in range(start, end+1):
        coords.append([row_num-1, i])
        coords.append([row_num+1, i])

    return coords

def part1(lines):
    grid = lines_to_grid(lines)

    total = 0
    M = len(grid)
    N = len(grid[0])

    def is_part_number(start, end, row_num) -> bool:
        bounding_box_coords = get_bounding_box(start, end, row_num)

        for r,c in bounding_box_coords:
            if r in range(M) and c in range(N) and grid[r][c] != "." and (not grid[r][c].isnumeric()):
                return True
        return False

    for r in range(M):
        matches = re.finditer("\d+", lines[r])
        for m in matches:
            if is_part_number(m.start(), m.end()-1, r):
                total += int(lines[r][m.start():m.end()])

    return total    

def part2(lines):
    grid = lines_to_grid(lines)

    gears_to_parts = defaultdict(list)
    total = 0
    M = len(grid)
    N = len(grid[0])

    def add_to_gear_list(start, end, row_num) -> None:
        bounding_box_coords = get_bounding_box(start, end, row_num)

        for r,c in bounding_box_coords:
            if r in range(M) and c in range(N) and grid[r][c] == "*":
                gears_to_parts[(r,c)].append(int(lines[row_num][start:end+1]))

    for r in range(M):
        matches = re.finditer("\d+", lines[r])
        for m in matches:
            add_to_gear_list(m.start(), m.end()-1, r)

    for parts in gears_to_parts.values():
        if len(parts) == 2:
            total += (parts[0] * parts[1])

    return total