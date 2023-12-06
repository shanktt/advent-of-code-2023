def part1(lines):
    times = list(map(int,lines[0].split(":")[1].strip().split()))
    distances = list(map(int,lines[1].split(":")[1].strip().split()))
    total = 1

    for t,d_needed in zip(times,distances):
        cur_total = 0
        for i in range(1,t+1):
            d_acutal = i * (t-i)
            if d_acutal > d_needed:
                cur_total += 1
        total *= cur_total

    return total

def part2(lines):
    time = int(''.join(lines[0].split(":")[1].strip().split()))
    distance = int(''.join(lines[1].split(":")[1].strip().split()))
    total = 1


    cur_total = 0
    for i in range(1,time+1):
        d_acutal = i * (time-i)
        if d_acutal > distance:
            cur_total += 1
    total *= cur_total

    return total


