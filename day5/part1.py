def next_step(values, maps):
    for i in range(len(values)):
        for dest, source, length in maps:
            if source <= values[i] < source + length:
                values[i] = dest + (values[i] - source)
                break
        else:
            while True:
                for dest, source, length in sorted(maps):
                    if dest <= values[i] < dest + length:
                        values[i] = dest+length + (values[i] - dest)
                        break
                else:
                    break

    return values


maps = []
while True:
    try:
        line = input()
        if line.startswith('seeds: '):
            seeds = line[7:]
            seeds = seeds.split()
            values = [int(i) for i in seeds]

            d_cat = 'seed'
            maps = []
            continue
        elif line.endswith('map:'):
            s_cat, d_cat = line[:-5].split('-to-')
            maps = []

        elif line == '':
            values = next_step(values, maps)
            print(f"{d_cat}: {values}")
        else:
            dest, source, length = map(int, line.split())
            maps.append((dest, source, length))
    except EOFError:
        values = next_step(values, maps)
        break
print(f"location: {values}")

print(f"min: {min(values)}")