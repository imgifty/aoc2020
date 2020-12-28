import re


def part_1(input):
    def dfs(state, found):
        successors = [key for key, value in input.items() if state in value]

        for succ in successors:
            found.add(succ)
            dfs(succ, found)

        return found

    found = dfs('shiny gold', set())

    return len(found)


def calculate_sum(input, state, found):
    summation = 0

    if state not in found:
        found.add(state)

    if state in input:
        children = [child for child in input[state]]

        for successor in children:
            color, value = successor
            summation += value + (value * calculate_sum(input, color, found))

    return summation


def part_2(input):
    found = set()

    state = 'shiny gold'
    return calculate_sum(input, state, found)


def parse(lines, with_numbers):
    PATTERN = re.compile(r'(?P<color>.*) bags contain (?P<rest>.*)')
    BAG_PATTERN = re.compile(r'(\d \w+ \w+) (?:bag|bags)')

    constraints = {}
    for line in lines:
        match = PATTERN.match(line)
        color = match.group('color')
        rest = match.group('rest')

        out = BAG_PATTERN.findall(rest)
        colors = []
        for o in out:
            splits = o.split(' ')
            number = int(splits[0])
            c = splits[1] + ' ' + splits[2]
            if with_numbers:
                colors.append((c, number))
            else:
                colors.append(c)
        constraints[color] = colors

    return constraints


if __name__ == '__main__':
    with open('day7.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')

        constraints = parse(lines, False)
        print(f'Solution part 1: {part_1(constraints)}')

        constraints = parse(lines, True)
        print(f'Solution part 2: {part_2(constraints)}')
