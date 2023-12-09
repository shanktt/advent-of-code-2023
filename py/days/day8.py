from math import lcm

def part1(lines):
    steps = lines[0]

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
    totals = []

    # each A maps on to the same Z

    # A1 gets to Z1 in x steps
    # A2 gets to Z2 in y steps
    # A3 gets to Z3 in z steps

    for idx,_ in enumerate(nodes):
        node = nodes[idx]
        total = 0
        while node[-1] != "Z":
            d = graph[node]
            if steps[cur_step] == "L":
                node = d[0]
            else:
                node = d[1]

            cur_step = ((cur_step + 1) % len(steps))
            total += 1
        totals.append(total)
    return lcm(*totals)