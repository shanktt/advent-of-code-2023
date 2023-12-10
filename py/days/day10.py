# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

PIPE_TO_D = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
    "S": ["N","W","S","E"]
}

D_TO_OPP = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

D_TO_CORD = {
    "N": [-1,0],
    "S": [1,0],
    "E": [0,1],
    "W": [0,-1],
}

def part1(lines):
    grid = [list(l) for l in lines]
    M = len(grid)
    N = len(grid[0])

    starting_loc = (0,0)
    for r in range(M):
        for c in range(N):
            if grid[r][c] == "S":
                starting_loc = (r,c)
                break
    cycles = []
    def dfs(x,y, visited, path_len):
        print(f"{x} {y}")
        if grid[x][y] == "S" and visited:
            cycles.append(path_len[::])
        pipe = grid[x][y]
        for directions in PIPE_TO_D[pipe]:
            for d in directions:
                cords = D_TO_CORD[d]
                new_x, new_y = x+cords[0], y+cords[1]

                if new_x in range(M) and new_y in range(N) and f"{(x,y)}->{(new_x,new_y)}" not in visited and f"{(new_x,new_y)}->{(x,y)}" not in visited and grid[new_x][new_y] in PIPE_TO_D and D_TO_OPP[d] in PIPE_TO_D[grid[new_x][new_y]]:
                    path_len.append(grid[new_x][new_y])
                    visited.add(f"{(x,y)}->{(new_x,new_y)}")
                    visited.add(f"{(new_x,new_y)}->{(x,y)}")
                    dfs(new_x,new_y,visited,path_len)
                    path_len.pop()
                    visited.remove(f"{(x,y)}->{(new_x,new_y)}")
                    visited.remove(f"{(new_x,new_y)}->{(x,y)}")

    x,y = starting_loc
    visited = set()
    # visited.add((x,y))
    dfs(x,y, visited, ["S"])
    
    return max(((len(c)-1)//2) for c in cycles)

def part2(lines):
    return 0