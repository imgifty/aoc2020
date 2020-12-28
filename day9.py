def part_1(input):
    preamble = 25
    numbers = [int(number) for number in input]

    for i in range(preamble, len(numbers)):
        subset = numbers[i-preamble:i]

        sets = {sum([a, b]) for a in subset for b in subset if a != b}
        if numbers[i] not in sets:
            return numbers[i]


def part_2(input):
    preamble = 25
    numbers = [int(number) for number in input]

    for i in range(preamble, len(numbers)):
        subset = numbers[i-preamble:i]

        sets = {sum([a, b]) for a in subset for b in subset if a != b}
        if numbers[i] not in sets:
            found = numbers[i]
            break

    for i in range(len(numbers)):
        r = []
        for j in range(i, len(numbers)):
            r.append(numbers[j])

            if sum(r) == found and len(r) > 2:
                return min(r) + max(r)
            elif sum(r) > found:
                break


if __name__ == '__main__':
    with open('day9.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
