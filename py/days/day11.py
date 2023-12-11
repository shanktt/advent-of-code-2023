from itertools import combinations
from collections import deque

def part1(grid):
    grid = grid.copy() #bruh!!!
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

    grid = [list(g) for g in grid]

    num_galaxies = 0
    galaxy_cords = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == "#":
                galaxy_cords.append((r,c))
                # grid[r][c] = num_galaxies + 1
                # num_galaxies += 1
    unique_pairs = list(combinations(galaxy_cords, 2))

    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    def bfs(x,y,s,t):
        deq = deque([(x,y)])
        visited = set()
        dist = 0
        while deq:
            for _ in range(len(deq)):
                x,y = deq.popleft()
                for d in directions:
                    new_x,new_y = x+d[0],y+d[1]
                    if new_x in range(N) and new_y in range(M) and (new_x,new_y) not in visited:
                        visited.add((new_x,new_y))
                        deq.append((new_x,new_y))
                        if (new_x,new_y) == (s,t):
                            return (dist+1)
            dist += 1
    
    # print(grid[10][9])
    # return sum([bfs(*a[0],*a[1]) for a in unique_pairs])
    return sum([abs(a[0]-b[0])+abs(a[1]-b[1]) for (a,b) in unique_pairs])

def part2(grid):
    grid = [list(g) for g in grid]

    N = len(grid)
    M = len(grid[0])

    num_galaxies = 0
    galaxy_cords = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == "#":
                galaxy_cords.append((r,c))

    unique_pairs = list(combinations(galaxy_cords, 2))
    total = 0
    for s,t in unique_pairs:
        empty_rows = 0
        empty_cols = 0

        start_x,end_x = 0,0
        start_y,end_y = 0,0

        if s[0] <= t[0]:
            start_x = s[0]
            end_x = t[0]
        else:
            start_x = t[0]
            end_x = t[0]
        
        if s[1] <= t[1]:
            start_y = s[1]
            end_y = t[1]
        else:
            start_y = t[1]
            end_y = s[1]

        for r in range(start_x,end_x):
            if all([c == "." for c in grid[r]]):
                empty_rows += 1
        for c in range(start_y,end_y):
            expand = True
            for r in range(M):
                if grid[r][c] != ".":
                    expand = False
                    break
            if expand:
                empty_cols += 1

        total += abs(s[0]-t[0]) + abs(s[1]-t[1]) + (empty_rows * 999999) + (empty_cols * 999999)

    return total
