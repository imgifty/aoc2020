import re


def part_1(input):
    accumulator = 0
    position = 0
    visited = set()

    for line in input:
        cmd, sign, value = input[position]
        sign = -1 if sign == '-' else 1

        if position in visited:
            return accumulator
        else:
            visited.add(position)

        if cmd == 'acc':
            accumulator += sign * value
            position += 1
        elif cmd == 'nop':
            position += 1
        elif cmd == 'jmp':
            position += sign * value


def part_2(input):
    indices_of_nop_jmps = [i for i in range(len(input))
                           if input[i][0] == 'jmp' or input[i][0] == 'nop']

    for i in indices_of_nop_jmps:
        new_input = input.copy()
        old_cmd = new_input[i][0]
        switched = 'jmp' if old_cmd == 'nop' else 'nop'
        new_cmd = (switched, new_input[i][1], new_input[i][2])
        new_input[i] = new_cmd

        accumulator = 0
        position = 0
        visited = set()

        while True:
            if position == len(new_input):
                return accumulator

            if position in visited:
                break
            else:
                visited.add(position)

            cmd, sign, value = new_input[position]
            sign = -1 if sign == '-' else 1

            if cmd == 'acc':
                accumulator += sign * value
                position += 1
            elif cmd == 'nop':
                position += 1
            elif cmd == 'jmp':
                position += sign * value


if __name__ == '__main__':
    with open('day8.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        pattern = re.compile(r'(acc|jmp|nop) (\+|-)(\d+)')

        matches = [pattern.match(line) for line in lines]
        matches = [(m.group(1), m.group(2), int(m.group(3))) for m in matches]

        print(f'Solution part 1: {part_1(matches)}')
        print(f'Solution part 2: {part_2(matches)}')
