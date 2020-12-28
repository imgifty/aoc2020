from collections import Counter


def part_2(input):
    count = 0
    for password in input:
        s, _, e = password[0].partition('-')
        letter = password[1][0]
        text = password[2]
        s, e = int(s), int(e)

        if bool(text[s-1] == letter) ^ bool(text[e-1] == letter):
            count += 1

    return count


def part_1(input):
    count = 0
    for password in input:
        s, _, e = password[0].partition('-')
        letter = password[1][0]
        text = password[2]
        s, e = int(s), int(e)

        letter_count = Counter(text)
        if s <= letter_count[letter] <= e:
            count += 1

    return count


if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        ingoing = f.read()
        lines = [line.split(' ') for line in ingoing.split('\n')]

        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
