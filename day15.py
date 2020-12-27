def part_1(input):
    memory = {}
    last_number = 0
    iteration = 0

    for i in input:
        last_number = i
        iteration += 1
        if last_number not in memory:
            memory[last_number] = [iteration]
        else:
            memory[last_number].append(iteration)

    while iteration < 2020:
        iteration += 1
        if last_number in memory:
            if len(memory[last_number]) == 1:
                last_number = 0
            else:
                last_number = memory[last_number][-1] - memory[last_number][-2]

        if last_number in memory:
            memory[last_number].append(iteration)
        else:
            memory[last_number] = [iteration]

    return last_number


def part_2(input):
    memory = {}
    last_number = 0
    iteration = 0

    for i in input:
        last_number = i
        iteration += 1
        if last_number not in memory:
            memory[last_number] = [iteration]
        else:
            memory[last_number].append(iteration)

    while iteration < 30000000:
        iteration += 1
        if last_number in memory:
            if len(memory[last_number]) == 1:
                last_number = 0
            else:
                last_number = memory[last_number][-1] - memory[last_number][-2]

        if last_number in memory:
            memory[last_number].append(iteration)
        else:
            memory[last_number] = [iteration]

    return last_number


if __name__ == '__main__':
    #ingoing = '''0
#3
#6'''
    ingoing = '''0,13,1,8,6,15'''
    lines = ingoing.split(',')
    lines = [int(number) for number in lines]
    print(f'Solution part 1: {part_1(lines)}')
    print(f'Solution part 2: {part_2(lines)}')
