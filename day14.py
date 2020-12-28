import re

PATTERN = re.compile(r'mem\[(\d+)\] = (\d+)')


def part_1(input):
    def mask(mask, number):
        copied = [a for a in number]
        for a, value in mask:
            copied[a] = value

        return ''.join(copied)

    memory = {}
    masked = []
    for i in range(0, len(input)):
        line = input[i]
        match = PATTERN.match(line)
        if match is None:
            _, _, bit_mask = line.partition('mask = ')
            masked = [(i, bit_mask[i])
                      for i in range(len(bit_mask)) if bit_mask[i] != 'X']
        else:
            location, value = match.group(1), int(match.group(2))
            bits = f'{value:036b}'
            memory[location] = int(mask(masked, bits), 2)

    return sum(memory.values())


def part_2(input):
    def mask(mask, number):
        copied = [a for a in number]
        for a, value in mask:
            copied[a] = value

        return [''.join(s) for s in expand(len(copied)-1, copied)]

    def expand(current, sequence):
        if current == 0:
            if sequence[current] == 'X':
                a = sequence.copy()
                a[current] = '1'
                yield a

                a = sequence.copy()
                a[current] = '0'
                yield a
                return
            else:
                yield sequence
                return

        else:
            if sequence[current] == 'X':
                a = sequence.copy()
                a[current] = '1'
                yield from expand(current-1, a)

                a = sequence.copy()
                a[current] = '0'
                yield from expand(current-1, a)
            else:
                yield from expand(current-1, sequence)

    memory = {}
    masked = []
    for i in range(0, len(input)):
        line = input[i]
        match = PATTERN.match(line)
        if match is None:
            _, _, bit_mask = line.partition('mask = ')
            masked = [(i, bit_mask[i])
                      for i in range(len(bit_mask)) if bit_mask[i] != '0']
        else:
            location, value = int(match.group(1)), int(match.group(2))
            bits = f'{location:036b}'
            locations = mask(masked, bits)
            for location in locations:
                memory[int(location, 2)] = value

    return sum(memory.values())


if __name__ == '__main__':
    with open('day14.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')[0:-1]
        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
