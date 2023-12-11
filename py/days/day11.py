def part1(grid):
    # grid = [list(l) for l in lines]
    M = len(grid)
    N = len(grid[0])

    expanded_rows = []
    expanded_cols = []


    for r in range(M):
        if all([c == "." for c in grid[r]]):
            expanded_rows.append(r)
    for c in range(N):
        expand = True
        for r in range(M):
            if grid[r][c] != ".":
                expand = False
                break
        if expand:
            expanded_cols.append(c)

    for i,r in enumerate(expanded_rows):
        r += i
        grid.insert(r, "." * N)

    N = len(grid)
    for i,c in enumerate(expanded_cols):
        c += i
        for r in range(N):
            grid[r] = grid[r][:c+1] + "." + grid[r][c+1:]
    M = len(grid[0])

    for g in grid:
        print(g)

    return 0

def part2(lines):
    return 0

