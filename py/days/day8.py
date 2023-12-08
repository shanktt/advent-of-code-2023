from collections import defaultdict
def part1(lines):
    steps = lines[0]
    return 0
    graph = {}
    for line in lines[2:]:
        start,dests = [l.strip() for l in line.split('=')]
        dests = dests.replace('(','').replace(')','')
        dests = [d.strip() for d in dests.split(',')]

        graph[start] = dests
    
    node = "AAA"
    total = 0
    cur_step = 0
    while node != "ZZZ":
        d = graph[node]
        if steps[cur_step] == "L":
            node = d[0]
        else:
            node = d[1]

        total += 1
        cur_step = ((cur_step + 1) % len(steps))

    return total

def part2(lines):
    steps = lines[0]

    graph = {}
    for line in lines[2:]:
        start,dests = [l.strip() for l in line.split('=')]
        dests = dests.replace('(','').replace(')','')
        dests = [d.strip() for d in dests.split(',')]

        graph[start] = dests

    nodes = [n for (n,_) in graph.items() if n[-1] == "A"]
    total = 0
    cur_step = 0

    while not all([node[-1] == "Z" for node in nodes]):
        for idx,node in enumerate(nodes):
            d = graph[node]
            if steps[cur_step] == "L":
                node = d[0]
            else:
                node = d[1]

            nodes[idx] = node
        total += 1
        cur_step = ((cur_step + 1) % len(steps))

    return total