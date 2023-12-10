# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
import sys

sys.setrecursionlimit(100000)
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

'''
https://chat.openai.com/share/43ff5c12-8e38-4008-b7b2-fe6e64e0d092

Assuming S is like the other pipes (implied by problem statement)
then it should only connect to two other pipes. Therefore only one
loop (where edges are repeated in the loop) exists in graph G that 
contains S. Starting from S and traversing, each node has two edges, 
one from where it came from, and one other one. Therefore, there are
only "two" paths that start at S and flow through the two nodes directly 
connected to it, until they meet one another.
So instead of having to worry about finding all cycles in 
G that contain S, we can instead just find the node furthest from S
using a BFS, since this node will necessarily have to be part of the loop 
''' 
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
    def dfs(x,y, visited, path_len, i):
        if grid[x][y] == "S" and visited:
            cycles.append(path_len)

        pipe = grid[x][y]
        for directions in PIPE_TO_D[pipe]:
            for d in directions:
                cords = D_TO_CORD[d]
                new_x, new_y = x+cords[0], y+cords[1]
                if new_x in range(M) and new_y in range(N) and f"{(x,y)}->{(new_x,new_y)}" not in visited and f"{(new_x,new_y)}->{(x,y)}" not in visited and grid[new_x][new_y] in PIPE_TO_D and D_TO_OPP[d] in PIPE_TO_D[grid[new_x][new_y]]:
                    path_len += 1
                    visited.add(f"{(x,y)}->{(new_x,new_y)}")
                    visited.add(f"{(new_x,new_y)}->{(x,y)}")
                    dfs(new_x,new_y,visited,path_len, i+1)
                    path_len -= 1
                    visited.remove(f"{(x,y)}->{(new_x,new_y)}")
                    visited.remove(f"{(new_x,new_y)}->{(x,y)}")

    x,y = starting_loc
    visited = set()
    dfs(x,y, visited, 0, 0)
    return max((c//2) for c in cycles)

def part2(lines):
    return 0