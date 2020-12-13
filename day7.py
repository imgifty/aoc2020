import re

def main(input):
    found = set()

    state = [key for key, value in input.items() if 'shiny gold' in value]

    while len(state) != 0:
        found.add(state) 

        for succ in state:
            new_states = [key for key, value in input.items() if succ in value]
            print(new_states)


if __name__ == '__main__':

    ingoing = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''

    lines = ingoing.split('\n')[:-1]

    PATTERN = re.compile(r'(?P<color>.*) bags contain (?P<rest>.*)')
    BAG_PATTERN = re.compile(r'(\d \w+ \w+) (?:bag|bags)')
    constraints = {}
    for line in lines:
        match = PATTERN.match(line)
        color = match.group('color')
        rest = match.group('rest')

        out = BAG_PATTERN.findall(rest)
        cs = []
        for o in out:
            splits = o.split(' ')
            number = splits[0]
            c = splits[1] + ' ' + splits[2]
            # cs.append((number, c))
            cs.append(c)
        constraints[color] = cs
    
    print(constraints)
    print(main(constraints))