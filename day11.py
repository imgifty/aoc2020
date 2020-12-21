def part_1(input):
    ...


def part_2(input):
    ...


if __name__ == '__main__':
    with open('day11_part1.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        print(f'Solution part 1: {part_1(lines)}')

    # with open('input.txt', 'r') as f:
    #     ingoing = f.read()
    #     lines = ingoing.split('\n')
    #     print(f'Solution part 2: {part_2(lines)}')