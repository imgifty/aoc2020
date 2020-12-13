def main(input):
    width, height = len(input[0]), len(input)

    tree_counts = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for right, left in slopes:
        position = [0, 0] #row, column
        tree_count = 0
        while position[0] != height-1:
            position[0] += left
            position[1] += right

            if input[position[0]][position[1] % width] == '#':
                tree_count += 1
        tree_counts *= tree_count
    
    return tree_counts


# def main(input):
#     width, height = len(input[0]), len(input)

#     tree_count = 0
#     position = [0, 0] #row, column
#     while position[0] != height-1:
#         position[0] += 1
#         position[1] += 3

#         if input[position[0]][position[1] % width] == '#':
#             tree_count += 1
    
#     return tree_count


if __name__ == '__main__':
    # input_string = '''..##.......
    # #...#...#..
    # .#....#..#.
    # ..#.#...#.#
    # .#...##..#.
    # ..#.##.....
    # .#.#.#....#
    # .#........#
    # #.##...#...
    # #...##....#
    # .#..#...#..'''
    input_string = '''.#......#..####.....#..#.......
#.#...#...#..#.#...#.#...##.##.
#.#....#..........#...##.....##
#.#.#.....##......#.#.......###
..#..###....#.#....#.#.#..#....
.......#.#....##..##...#...#...
..#..#..#..###.......#.....#.#.
.#.......#...##...##.##......##
#.#.##..##.#..#....#..###..#.#.
#.....#.#.........#.....##.#.#.
..#.#....##..#...#...##........
......#....#..##.#.#......###..
.......#.......#......##...#...
.##.....#.......#...###.....##.
.#...#.##..##.#..##....#.......
..#......##...#..#...#.#.##.###
.##.##.....##....#..#......#.#.
.#.....#..###..#.##.#.....##.#.
......##..........#..........#.
.##....#.....#..##.#..#.#..###.
..##.......#....#...##...#..#..
.##...#.....#.###.#.#..#...#.#.
.....##.#.##..##...#...........
..#..###.##.#.#.###...###..#.#.
.#........#..#.#........#.#...#
....##.......#....#.#.##.#.....
....##........######..###..#.#.
#.#.#............#.......#..#..
...##...#.##.....#.#..#......#.
......#.##.#....##..#.#..###...
##.....#.#....#....#.##.#.###..
#..#..#..##.#..##.##.##.#.##...
.###.####..#..#........#.....##
.......##..#.......#...........
.##...#............#.#.##...#..
....##.....#...##..#..#.#..###.
...#.....#####.#..#...##....##.
#.....#.#.#....##.......##.#.#.
......#.#..#.##.#######......#.
#.##...##....#..###.#.......#..
.....##...#....#...#....##.##.#
....###......#...###..#......##
..#...##..##.######..#.#......#
......##....#....##..#......##.
.#...#..##..#.###.#......#....#
##....##..#..####.#.....#...#..
.#.......#...#.......##......#.
......#...#...#........#.......
.#........#.###...#..####.#..#.
##...#.#............#.....###..
.....###.#.##...........###..#.
.#.#...#.....#.#.##..##...####.
..##.......#..#.##.#....#.....#
.#..#.#..####.....###.#.....#..
..#..###.....####..#.##.#.#.##.
.###..#.....#......#...####....
...#.#..#.#..#...#...#....##.##
..###....#.##.....#..........#.
###...#####......##............
..###.....#........##.#...#..#.
..##.##.#.....##........##..#.#
##..#.#...#.#..#..###.#....#..#
....#..#.#.....#..#####...#....
....#.........#......##.##.....
.#...####.##......##..##.#..#.#
...#...#.##..#...##..###...#...
###...#.....#.##.###.###..#.#..
..#......#.###.....#..##.#...#.
#.....##.########...#####....#.
........##..#..##..##.#........
....#.######....##..#..#.##..#.
#.......#..##..#..#.#.#..##.##.
...#.#..#..#.......#......###.#
.#.#..#.#..#.##.#.............#
#....#.##.#.#.....#..#.#..#....
...###..#...#....#.........#.#.
.#..#.....##..#.#..#.#.......#.
..#...##...#......#......####..
....#..#.......#.......#.#..#..
#...#..#...........#.#..#.....#
#...#.#.......#...#....###....#
.#..#.#.##....#......#........#
..#...#..##..#..#..#..#...#.#..
..#.#.........#....#....##.....
##.....##.#.#.#.........##.....
.##...#.##...........#...#...##
.##..##.#.#..........##..##....
#....#....#.#...#.#..#....#.#..
####....##.....#..##.###.......
#..#....#......##.#.#....#.....
.....#....#.###.##.........###.
#.......#.####..#..#..##.......
##.#.......#..##..#....#..#.#..
..###...#.#...#.....##.##.####.
....#...#.#....#..#..#.....#.##
#.....##.#.#..#.##..#..##......
................###..#....##...
..#.##.....#..........##.#...#.
..#.#..#.#....#.#.#..#..#..#.#.
#...#..##.#.#...#..#...#..#....
#..#.#.........#..###........#.
.#...#.............#..###..#..#
#.........#.#..#...#.#.....#..#
....#..#..#.#.#...#...#.....##.
##...###.#.####..#......#...#..
..#..##...#.#......#.#.......#.
#......###....##.#.##..........
#####....###..#...............#
##.#...####....#....#...#....#.
.#.......#..#.....#...#.....###
...#..#.#.#....##......##...#..
...#.....#...#.##.#..#.#....#..
#...###....#...#.#....#........
.#.......#........#...##.##.##.
.....#....#...##.....##...###.#
....#....#.#..#...##.##.##.....
.......#............#...#.#..#.
.#............#.....##.......#.
........#....#....##......##.##
.......##..#.#..#.##..###..##.#
#..##..##.........####.#.###...
#....#..#...##...#.............
#...#...###..........##..#..#..
....#...#..#.....##...#........
#.....#......#.#.....#...#..#..
..#.....#.....#....#..#........
..#..#.....#.#.........#..###..
................###..#.#....#..
#.....#.....#.#.#.#.#..#...#.#.
#....#....#.#..........#.#....#
....#..#......#..##.#...##.....
..#.#...#.####....#.#..#.#..#..
.........##......#.....##......
##.#.###.#.....#.....####.#..#.
.....#.....#..#....#..###.#....
##..#.#...#.##....#....#.......
.....#......#.#...##..#.#......
....##..#...#...##..##.#....#.#
............#..........##.#....
##..#..#.##..##..#.#....#.#.#..
.......#.#...#...#.#...#..#....
#....#.#...#...#........#..#...
...........#.......#...##..###.
.#..##......#.##.........##..#.
...#...#...###.#.##....##.#..#.
#...#..#.#.#.....##..#.......#.
.##..#.###.##......#.#....#.#.#
..#....#.......#..#..#.#.#.##..
#...#...###...###.........#....
.#.#...#.....##.#.#..#....#.##.
.........#.#.##.....#.#.###....
...#.#...#......#...####......#
...##..##....##......##...###..
###...#..#.......##.....#....#.
...#..#..#..###...##.##..#..#..
...#......#......##..#.#.##..#.
...#.........#....#.#....#.#...
##................#..#.#.....#.
....#.##...#..#.##...##.#.....#
......#..##.##..###.#..#.##.##.
.#.#...###.....###.....##...###
.##.....#.#.#..#..###..#..#..#.
#.......#..#..#....##.....#....
...#.#.##..#..#......##.##...#.
....##.#......#...#..#..#......
.####.#..#.....#..##.#...##..##
..#..#...#..........###..#....#
.#.#.##.##...#............#....
........##..##......#.##..#.###
...#.#....###......##.......#..
..##...#...#.#..#.....#.....#..
##..#...###..#..#.#.#...#...#..
.....#..#....##.....##.....###.
....##...###.#..#.#....##..#..#
#......#...#....#......#...##..
....#.##...#.#......#.#.##...#.
.......#.....#...#####...#.#...
...#.....##.#............#.....
...#.#........#.#.#..#.........
....###......#.#.#..#.####.#..#
#.....#.#.#.....#.#.#.....#..#.
..##.##......#...#.#...........
###..###....#.#####......###...
..##..............##.#.#....#.#
#..#...#..........#..#.#.#..###
##.###............#....#.#...#.
#.#..#.#..##.#.#....#...#......
#....#...#..##.....#..#.#..###.
..#.....#.#....#.#..#.##.#..##.
...##...#.#.##...#....###....#.
......###.####.......#..#.#.#.#
.#..............##........#....
...##.##...##....#..#.......#..
.....#.....#....###...#..#..#.#
.#.....#..#.....#......#.....##
#.#.##.#..#..#.....#.##..###...
..#......#...##.###..#.#...#..#
......#.....#...##......#......
##.#........#..........#.....#.
#........##.#............##....
...#......##...#.#.....##......
...##.......#....#.#..#.#.###..
..#....##..##.##.....###....#..
..#...#.#...#.....#..........#.
......#...#...#.#.##.#...#.#.#.
.#...#......#.##........#......
.##.##..#....#...#.#...##......
#..#......#.#...........#....#.
....##.#....#...#..#....#.#..##
#....##.##....#.#..##.#........
.##.##.#....##.....#..#....#..#
...#...#.....###.#.##..........
....#...#....##.......###......
#.........#......#.#.......#...
#..........#..##..#.#..........
.....#.......#..##.##....##...#
........................#.#....
#..#.........#.............#..#
#..#.....#.......#....#....#.#.
..##..##.......##....#...#.....
.##......#..##......#.###......
...#.#........#.......##..###..
..##...###.###......#...#....##
#...#...#.....###.#.#.#..#.....
#....#.........#..##...#...##..
#..###..#.#.#.##.#..#.#....#.##
#...#.#.....#.###.#.......#....
..##..#..#....#.#...........#.#
#.........#.#......#...##......
.######......#..#....#.#.#....#
##..#.#..####.###.........#....
###########.....##.##...#..#...
#...##.#.#....#.#....#......#..
...#..##..#..##..#......#....#.
.#....#...#....#.#..##....##...
#..#.#............#....#.#...#.
...#...#..#.#.##......#..#.#...
#.#...##.....#..#.##......####.
.#.#..##..#.....#.#..#.##......
#.#.##......##.....#..#.#..#...
#..##...#.##.#.......#.##......
..#.......#.#.#...##..##...#...
.#...#..#..#.#.........#..##...
#..#.......#....#.#...#.###...#
.......#..#.......##.#.#...#.#.
.#.................###.#..###..
..........#.#.....##..#####...#
#......#.#..##.#.#...#.##.#....
#......#.#..##.##.#...#....#...
....#..#......#....#....#######
.#...#......#....###......#.###
#.#....#.#...#.###......#..#..#
.###......#.#...#.####.#..####.
######.#.....###.#...#.#.....#.
.#.###....#..#.#.....#.....####
.......###.#.........#..#......
#...#.....##.#......####.......
..#.#..##.#.#...#...#..##..##..
.....#...##.....#...##......##.
##..#..#.##..#.#......#.....#..
##.........#.#.##.#..#.#....#.#
.#........###...#.........#....
...#..#.#..#....####...........
#.#....#..##..####.#...#.##....
.#.....#.......#..........#..##
...#.......#...###..#.....#..##
.........#.###.#..##...#.##...#
.#..........##..####...#..#.#.#
.#...##...#............##...#.#
...#....#.#..........#.#..#.#..
.#.#...##....##.#.#.#....#.....
....#..#.....#.#..#.#..#.##.###
.....#.#.....#..#......#.#.#...
.....#.#.#..###..#.#..###...#..
#.......####...#.#..#......##.#
....#..#..###......###.##....#.
##.....#.....#.............#..#
#..#..#...##.....##..#..#.#....
.....#.#.###...#...............
#.#.#.....#.#..#.#...#.......#.
..##.##............#....#..##..
#....##...#.....#.###...#.#....
#...##.#.........#...#....#....
##.##.#...#.#...###..#....##..#
....#....##..#..#.......#...##.
.#...#...#..#.....#..###.#..#.#
....#..###......#....##....#...
#.#.....#....##.#..#.#...###...
.......#............#......#...
.##..#.###.#.............###...
..##...##.#.#.#.....#........##
....#.###....#..#..#...#...#..#
.....#...#...#..#....#.....##..
###.#.#.....#......####.....#..
#.#.###............#......#....
..#.....#..#..#..#....#......#.
#...######...#....#.##...##.#.#
##.#.#.#..##......##.#..#.#...#
............#.#..#.##....#.....
......#............#.#...#..#.#
.#..##...##..#.#.#..###.....##.
#.###.#...........#...#....#...
....##.....#...##...#...###.#.#
.####.#.#.....#.#..#.#.##......
.#...##......###...#..##..#.#..
.#......#...#....##.....##..#..
..........##.....###.##.#...#.#
.#........##.#..............#..
#...###..#...#.....#....#.....#
...#......#..#...#...#..###.#..
.#...##..#........#.......#.#..
.#.#.##.........##.##......#..#
#...#.#.#...#.....#.#...#.#..#.
#.#..#...#...#...##..........#.
.#...........#....#..#.#..#.#..
#.......#......#..#...#........
.....#..#...##..###..##........
......#...#.....#..#.#.#....##.
....##..##..##....###.##.......
.#........##.#.#...#..#........
.....##...##...#......#..#...#.
..#.....#....###.#..##....#..#.
......#..#...####.#.....##.####'''
    ingoing = [line.lstrip() for line in input_string.split('\n')]
    # print(ingoing)
    print(main(ingoing))