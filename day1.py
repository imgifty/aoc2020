def part_1(numbers):
    for g in range(0, len(numbers)):
        for i in range(0, len(numbers)):
            if g != i:
                if numbers[i] + numbers[g] == 2020:
                    return numbers[i] * numbers[g]


def part_2(numbers):
    for g in range(0, len(numbers)):
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if j != i and g != j:
                    if numbers[i] + numbers[j] + numbers[g] == 2020:
                        return numbers[i] * numbers[j] * numbers[g]


if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        input_string = f.read()
        numbers = [int(number) for number in input_string.split('\n')]
        print(f'Solution part 1: {part_1(numbers)}')
        print(f'Solution part 2: {part_2(numbers)}')
