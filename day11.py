class Seat:
    def __init__(self, state, row, col, max_row, max_col):
        self.state = state
        self.row = row
        self.col = col
        self.max_row = max_row
        self.max_col = max_col
    
    def adjacent_seats(self, array):
        left = Seat('.', self.row, self.col-1, self.max_row, self.max_col)
        right = Seat('.', self.row, self.col+1, self.max_row, self.max_col)
        up = Seat('.', self.row-1, self.col, self.max_row, self.max_col)
        down = Seat('.', self.row+1, self.col, self.max_row, self.max_col)
        ur = Seat('.', self.row-1, self.col+1, self.max_row, self.max_col)
        ul = Seat('.', self.row-1, self.col-1, self.max_row, self.max_col)
        dl = Seat('.', self.row+1, self.col-1, self.max_row, self.max_col)
        dr = Seat('.', self.row+1, self.col+1, self.max_row, self.max_col)

        seats = [left, right, up, down, ur, ul, dl, dr]
        valid_seats = [seat for seat in seats 
                       if 0 <= seat.row < self.max_row and 0 <= seat.col < self.max_col]

        for seat in valid_seats:
            seat.state = array[seat.row][seat.col].state
        
        return valid_seats
    
    def __repr__(self):
        return self.state

def part_1(input):
    max_row = len(input)
    max_col = len(input[0])

    seats = [[Seat(input[i][j], i, j, max_row, max_col) for j in range(max_col)] for i in range(max_row)]

    def apply_rules(seats):
        seats_new = seats.copy()

        for row in range(max_row):
            for col in range(max_col):
                seat = seats[row][col]
                new_seat = seats_new[col][row]

                if seat.state == 'L' and len([True for s in seat.adjacent_seats(seats) if s.state == '#']) == 0:
                    new_seat.state = '#'
                if seat.state == '#' and len([True for s in seat.adjacent_seats(seats) if s.state == '#']) >= 4:
                    new_seat.state = 'L'

        return seats_new

    import pprint; pprint.pprint(seats)
    while True:
        seats = apply_rules(seats)
        # print(seats)
        pprint.pprint(seats)
        breakpoint()


def part_2(input):
    pass


if __name__ == '__main__':
    with open('day11_part1.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        array = [[char for char in line] for line in lines]
        print(f'Solution part 1: {part_1(array)}')

    # with open('input.txt', 'r') as f:
    #     ingoing = f.read()
    #     lines = ingoing.split('\n')
    #     print(f'Solution part 2: {part_2(lines)}')