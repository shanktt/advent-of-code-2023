from collections import defaultdict
from bisect import bisect_left, bisect

def part1(lines):
    # Remove empty lines
    lines = [l for l in lines if l]

    seeds = [int(s) for s in lines[0].split(":")[1].split()]

    num_maps = len([l for l in lines if "map" in l])
    maps = [[] for _ in range(num_maps)]

    map_idx = -1
    for l in lines[1:]:
        if "map" in l:
            map_idx += 1
            continue
    
        dest_start, source_start, range_ = [int(s) for s in l.split()]
        map_ = maps[map_idx]
        map_.append([dest_start, source_start, range_])


    min_location = float('inf')
    for val in seeds:
        for map_ in maps:
            for dest_start, source_start, range_  in map_:
                if source_start <= val < (source_start + range_):
                    val = dest_start + (val - source_start)
                    break
        min_location = min(min_location, val)

    return min_location

def part2(lines):
    # Remove empty lines
    lines = [l for l in lines if l]

    seeds = [int(s) for s in lines[0].split(":")[1].split()]
    new_seeds = []
    for i in range(0, len(seeds), 2):
        new_seeds += [i for i in range(seeds[i], seeds[i]+seeds[i+1])]
    seeds = new_seeds

    num_maps = len([l for l in lines if "map" in l])
    source_to_dest = [defaultdict(int) for _ in range(num_maps)]
    ranges = [[] for _ in range(num_maps)]

    map_idx = -1
    for l in lines[1:]:
        if "map" in l:
            map_idx += 1
            continue
    
        dest_start, source_start, range_ = [int(s) for s in l.split()]
        map_, r = source_to_dest[map_idx], ranges[map_idx]

        map_[source_start] = dest_start
        r.append(source_start)
        r.append(source_start + (range_ - 1))


    ranges = [sorted(r) for r in ranges]

    min_location = float('inf')
    for val in seeds:
        for r,p in zip(ranges, source_to_dest):
            
            # print(f"{r} {p}")
            # print(f"start: {val}")
            # https://stackoverflow.com/a/8458993/6609793
            if (idx := bisect(r, val)) % 2 == 1:
                # print(idx)
                source_start = r[idx-1]
                dest_start = p[source_start]
                val = dest_start + (val - source_start)
            # Edge case when bisect_left returns an 
            # even index when val is e
            elif idx <= len(r) and r[idx-1] == val:
                source_start = r[idx-2]
                dest_start = p[source_start]
                val = dest_start + (val - source_start)
            # print(f"end: {val}")
        # print("------------")
        min_location = min(min_location, val)

    return min_location