def part_1(input):
    adapters = sorted([int(line) for line in input])
    adapters.insert(0, 0)

    out = [adapters[a+1] - adapters[a] for a in range(len(adapters)-1)]
    ones = len([a for a in out if a == 1])
    threes = len([a for a in out if a == 3]) + 1

    return ones * threes


def get_sequences(adapters, start_position):
    cache = {}
    neighbors = {j: [i for i in adapters if 1 <= j - i <= 3] for j in adapters}

    def helper(adapters, start_position):
        if start_position in cache:
            return cache[start_position]

        if start_position == 0:
            return 1

        found = 0
        for i in neighbors[start_position]:
            found += helper(adapters, i)

        cache[start_position] = found

        return found

    return helper(adapters, start_position)


def part_2(input):
    adapters = [0] + sorted([int(line) for line in input])
    adapters = adapters + [max(adapters) + 3]
    return get_sequences(adapters, max(adapters))


if __name__ == '__main__':
    with open('day10.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
