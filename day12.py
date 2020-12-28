import math


def part_1(input):
    commands = []

    for a in input:
        command = a[0]
        rest = a[1:]
        commands.append((command, int(rest)))

    def get_direction(degrees):
        if 315 < degrees <= 360 or 0 <= degrees <= 45:
            return 'N'
        elif 45 < degrees <= 135:
            return 'E'
        elif 135 < degrees <= 180:
            return 'S'
        else:
            return 'W'

    current_deg = 90
    moved = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    for command, amount in commands:
        current_dir = get_direction(current_deg)

        if command in moved:
            moved[command] += amount
        else:
            if command == 'F':
                moved[current_dir] += amount
            elif command == 'L':
                current_deg = (current_deg - amount) % 360
            elif command == 'R':
                current_deg = (current_deg + amount) % 360

    return abs(moved['N'] - moved['S']) + abs(moved['E'] - moved['W'])


def part_2(input):
    commands = []

    for a in input:
        command = a[0]
        rest = a[1:]
        commands.append((command, int(rest)))

    def get_direction(degrees):
        if 315 < degrees <= 360 or 0 <= degrees <= 45:
            return 'N'
        elif 45 < degrees <= 135:
            return 'E'
        elif 135 < degrees <= 180:
            return 'S'
        else:
            return 'W'

    def get_rotation_matrix(deg):
        deg = math.radians(deg)
        return [(math.cos(deg), -math.sin(deg)),
                (math.sin(deg), math.cos(deg))]

    def rotate(vector, degrees):
        mat = get_rotation_matrix(degrees)
        return [vector[0]*mat[0][0] + vector[1]*mat[0][1],
                vector[0]*mat[1][0] + vector[1]*mat[1][1]]

    way_point = [1, 10]  # n/s and e/w
    moved = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    for command, amount in commands:
        if command in moved:
            if command == 'N':
                way_point[0] += amount
            if command == 'S':
                way_point[0] -= amount
            if command == 'E':
                way_point[1] += amount
            if command == 'W':
                way_point[1] -= amount
        else:
            if command == 'F':
                ns = amount * way_point[0]
                ew = amount * way_point[1]
                if ns < 0:
                    moved['S'] += -1*ns
                else:
                    moved['N'] += ns
                if ew < 0:
                    moved['W'] += -1*ew
                else:
                    moved['E'] += ew
            elif command == 'L':
                way_point = rotate(way_point, -amount)

            elif command == 'R':
                way_point = rotate(way_point, amount)

    return int(abs(moved['N'] - moved['S']) + abs(moved['E'] - moved['W']))


if __name__ == '__main__':
    with open('day12.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')[0:-1]
        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
