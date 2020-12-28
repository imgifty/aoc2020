def part_1(input):
    ids = []
    highest = 0
    for boarding_pass in input:
        row, column, seat_id = decode_seat(boarding_pass)
        ids.append(seat_id)

        if highest < seat_id:
            highest = seat_id

    return highest


def part_2(input):
    ids = []
    highest = 0
    for boarding_pass in input:
        row, column, seat_id = decode_seat(boarding_pass)
        ids.append(seat_id)

        if highest < seat_id:
            highest = seat_id

    return [seat
            for seat in range(min(ids), max(ids)) if seat not in ids][0]


def decode_seat(code):
    row_code = code[:-3]

    low = 0
    high = 127

    for i, letter in enumerate(row_code):
        middle = (high - low + 1) // 2

        if letter == 'F':
            high = high - middle
        else:
            low = low + middle

        if i == 6 and letter == 'F':
            row = high
        elif i == 6 and letter == 'B':
            row = low

    low = 0
    high = 7
    column_code = code[-3:]

    for i, letter in enumerate(column_code):
        middle = (high - low + 1) // 2

        if letter == 'L':
            high = high - middle
        else:
            low = low + middle

        if i == 2 and letter == 'L':
            column = low
        elif i == 2 and letter == 'R':
            column = high

    seat_id = row * 8 + column

    return row, column, seat_id


if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
