from bisect import bisect_left,bisect_right

def get_answer(grid,expansion_size=1):
    M = len(grid)
    N = len(grid[0])

    expanded_rows = []
    expanded_cols = []

    for r in range(M):
        if all([c == "." for c in grid[r]]):
            expanded_rows.append(r)
    for c in range(N):
        if all([grid[r][c] == "." for r in range(N)]):
            expanded_cols.append(c)

    galaxies = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == "#":
                galaxies.append((r,c))
   
    total = 0
    for i in range(len(galaxies)):
        for j in range(i,len(galaxies)):
            s = galaxies[i]
            t = galaxies[j]
            start_r,end_r = min(s[0],t[0]),max(s[0],t[0])
            start_c,end_c = min(s[1],t[1]),max(s[1],t[1])

            a = bisect_right(expanded_rows,end_r) -  bisect_left(expanded_rows,start_r) 
            b = bisect_right(expanded_cols,end_c) - bisect_left(expanded_cols,start_c)

            total += abs(s[0]-t[0]) + abs(s[1]-t[1]) + (a*expansion_size) + (b*expansion_size)

    return total

def part1(grid):
    return get_answer(grid)

def part2(grid):
    return get_answer(grid,expansion_size=999999)
