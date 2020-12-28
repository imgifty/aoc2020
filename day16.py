import re
from collections import defaultdict


RULES_PATTERN = re.compile(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)')
TICKET_PATTERN = re.compile(r'(\d+),(\d+)')


def parse_tickets(input):
    tickets = []
    accepted_numbers = set()
    validation = {}

    for line in input:
        m = RULES_PATTERN.match(line)
        if m is not None:
            g = [g for g in m.groups() if g is not None]
            first = range(int(g[1]), int(g[2])+1)
            second = range(int(g[3]), int(g[4])+1)
            joined = set(first) | set(second)

            validation[g[0]] = joined
            accepted_numbers |= joined

        tm = TICKET_PATTERN.match(line)
        if tm is not None:
            numbers = [int(n) for n in line.split(',')]
            tickets.append(numbers)

    return tickets, accepted_numbers, validation


def part_1(input):
    tickets, accepted_numbers, _ = parse_tickets(input)

    errors = []
    for ticket in tickets[1:]:
        for a in ticket:
            if a not in accepted_numbers:
                errors.append(a)

    return sum(errors)


def part_2(input):
    tickets = []
    tickets, accepted_numbers, validation = parse_tickets(input)

    valid_tickets = []
    for ticket in tickets[1:]:
        invalid = False
        for a in ticket:
            if a not in accepted_numbers:
                invalid = True

        if not invalid:
            valid_tickets.append(ticket)

    not_possibles = defaultdict(set)
    for ticket in valid_tickets:
        for a in range(len(ticket)):
            for key in validation.keys():
                if ticket[a] not in validation[key]:
                    not_possibles[a].add(key)

    def is_valid_partial_mapping(mapping):
        for ticket in valid_tickets:
            for i in range(len(mapping)):
                if mapping[i] is not None:
                    if ticket[i] not in validation[mapping[i]]:
                        return False
        return True

    def backtrack(state):
        if not is_valid_partial_mapping(state):
            return None

        if len(state) == len(validation.keys()) and None not in state.values():
            return state

        variables_left = [i for i in range(len(state)) if state[i] is None]
        domains = {i: set(validation.keys()) -
                   set([s for s in state.values() if s is not None]) -
                   not_possibles[i]
                   for i in variables_left}
        variables_left = sorted(variables_left, key=lambda x: len(domains[x]))

        chosen = variables_left[0]
        left = set(validation.keys()) - \
            set([s for s in state.values() if s is not None]) - \
            not_possibles[chosen]

        for key in left:
            state_n = state.copy()
            state_n[chosen] = key

            out = backtrack(state_n)
            if out is not None:
                return out

        return None

    state = {i: None for i in range(len(validation.keys()))}
    solution = backtrack(state)

    result = 1

    for a in [i for i, v in solution.items() if 'departure' in v]:
        result *= tickets[0][a]

    return result


if __name__ == '__main__':
    with open('day16.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')
        print(f'Solution part 1: {part_1(lines)}')
        print(f'Solution part 2: {part_2(lines)}')
