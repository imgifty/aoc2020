def part_1(input):
    summation = 0
    for group in input:
        found = {}
        for answer in group:
            if len(answer) != 1:
                for letter in answer:
                    if letter not in found:
                        found[letter] = True
            else:
                if answer not in found:
                    found[answer] = True
        summation += len(found)

    return summation


def part_2(input):
    summation = 0
    for group in input:
        found = {}
        people = len(group)
        for answer in group:
            if len(answer) != 1:
                for letter in answer:
                    if letter not in found:
                        found[letter] = 1
                    else:
                        found[letter] += 1
            else:
                if answer not in found:
                    found[answer] = 1
                else:
                    found[answer] += 1

        found = [key for key, value in found.items() if value == people]
        summation += len(found)

    return summation


if __name__ == '__main__':
    with open('day6.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        answers = [[]]
        for line in lines:
            if line != '':
                answers[-1].extend(line.split(' '))
            else:
                answers.append([])

        print(f'Solution part 1: {part_1(answers)}')
        print(f'Solution part 2: {part_2(answers)}')
