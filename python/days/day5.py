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
    # O(N) search over N ranges vs O(logn) search from before
    # Its cleaner this way...
    for val in seeds:
        for map_ in maps:
            for dest_start, source_start, range_  in map_:
                if source_start <= val < (source_start + range_):
                    val = dest_start + (val - source_start)
                    break
        min_location = min(min_location, val)

    return min_location

def find_location(seeds, step_size, maps) -> (int,int):
    min_location = float('inf')
    seed = None
    for (start,range_) in seeds:
        for val in range(start,start+range_,step_size):
            og_val = val
            for map_ in maps:
                for dest_start, source_start, range_  in map_:
                    if source_start <= val < (source_start + range_):
                        val = dest_start + (val - source_start) 
                        break
            if val < min_location:
                min_location = val
                seed = og_val
    
    return seed,min_location

def find_location2(start, step_size, range_, maps) -> (int,int):
    min_location = float('inf')
    seed = None
    for val in range(start,start+range_,step_size):
        og_val = val
        for map_ in maps:
            for dest_start, source_start, range_  in map_:
                if source_start <= val < (source_start + range_):
                    val = dest_start + (val - source_start) 
                    break
        if val < min_location:
            min_location = val
            seed = og_val
    
    return seed,min_location

def part2(lines):
    # Remove empty lines
    lines = [l for l in lines if l]

    seeds = [int(s) for s in lines[0].split(":")[1].split()]
    # Numbers of pairs of N length list where N, is even, is N/2
    # and each i in range(N//2) maps to the i-th pair
    seeds = [[seeds[i*2], seeds[i * 2 + 1]] for i in range(len(seeds)//2)]
    step_size = 10**6

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

    seed,location = find_location(seeds, step_size, maps)
    while step_size:
        left_seed = seed - step_size
        right_seed = seed + step_size

        left_seed,left_loc = find_location2(left_seed, (step_size // 10), step_size, maps)
        right_seed,right_loc = find_location2(right_seed, (step_size // 10), step_size, maps)
        


        seed = left_seed if left_loc < right_loc else right_seed
        location = left_loc if left_loc < right_loc else right_loc

    return f"{seed} {location}"