import re


def part_1(input):
    PATTERN = re.compile(r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):')
    # keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    valid_passwords = 0
    for password in input:
        found_keys = set()
        for line in password:
            found = PATTERN.findall(line)
            if found is not None:
                found_keys = found_keys | set(found)
        
        if len(found_keys) == 8:
            valid_passwords += 1
        if len(found_keys) == 7 and 'cid' not in found_keys:
            valid_passwords += 1

    return valid_passwords


def part_2(input):
    PATTERN = re.compile(r'(byr:[0-9]+)|(iyr:[0-9]+)|(eyr:[0-9]+)|(hgt:[0-9]+(?:cm|in))|(hcl):#[0-9a-f]{6}|(ecl):(?:amb|blu|brn|gry|grn|hzl|oth)|^(pid):\d{9}$|cid')
    SMALL = re.compile(r'([a-z]+):([0-9a-z]+)')

    valid_passwords = 0
    for password in input:
        found_keys = set()
        for line in password:
            found = PATTERN.findall(line)

            if found is not None:
                keys = [j 
                        for a in found 
                        for j in a if j != '']
                
                for k in keys:
                    m = SMALL.fullmatch(k)
                    if m is not None:
                        key = m.group(1)
                        text = m.group(2)
                        if key == 'byr' and 1920 <= int(text) <= 2002:
                            found_keys.add(key)

                        if key == 'iyr' and 2010 <= int(text) <= 2020:
                            found_keys.add(key)

                        if key == 'eyr' and 2020 <= int(text) <= 2030:
                            found_keys.add(key)

                        if key == 'hgt':
                            unit = text[-2:]
                            size = int(text[:-2])
                            if unit == 'cm':
                                if 150 <= size <= 193:
                                    found_keys.add(key)
                            elif unit == 'in':
                                if 59 <= size <= 76:
                                    found_keys.add(key)
                    else:
                        found_keys.add(k)

        if len(found_keys) == 8 or (len(found_keys) == 7 and 'cid' not in found_keys):
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    with open('day4.txt', 'r') as f:
        ingoing = f.read()
        lines = ingoing.split('\n')

        passports = [[]]
        for line in lines:
            if line != '':
                passports[-1].extend(line.split(' '))
            else:
                passports.append([])

        print(f'Solution part 1: {part_1(passports)}')
        print(f'Solution part 2: {part_2(passports)}')