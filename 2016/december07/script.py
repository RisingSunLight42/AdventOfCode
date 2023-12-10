import regex as re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


def part_one():
    regex_abba = re.compile(r'([a-z])((?!\1)[a-z])\2\1')
    total = 0
    for line in lines:
        supernet = re.sub(r'\[[a-z]+\]', '-', line)
        hypernet = '-'.join(re.findall(r'\[[a-z]+\]', line))

        if regex_abba.search(supernet) and not regex_abba.search(hypernet):
            total += 1
    print(total)


def part_two():
    re_aba = re.compile(r'([a-z])((?!\1)[a-z])\1')
    total = 0
    for line in lines:
        supernet = re.sub(r'\[[a-z]+\]', '-', line)
        hypernet = '-'.join(re.findall(r'\[[a-z]+\]', line))
    
        for (a, b) in re_aba.findall(supernet, overlapped = True):
            if b + a + b in hypernet:
                total += 1
                break
    print(total)

part_one()
part_two()