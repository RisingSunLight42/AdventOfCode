with open("./input.txt", 'r', encoding='utf-8') as file:
    block_input_1, block_input_2 = file.read().split("\n\n")


workflows = {}

for line in block_input_1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        comparator = comparison[1]
        number = int(comparison[2:])
        workflows[name][0].append((key, comparator, number, target))


operators = {
    # Basically, in Python, when we do a comparison with operators, int.__gt__(a,b) is called
    # I don't use eval only because it is safer (eval can run arbitrary code if the input is malicious for e.g.)
    ">": int.__gt__,
    "<": int.__lt__
}


def accept(item, name="in"):
    if name == "R":
        return False
    if name == "A":
        return True
    
    rules, fallback = workflows[name]
    for key, comparator, number, target in rules:
        if operators[comparator](item[key], number):
            return accept(item, target)
    return accept(item, fallback)


def part_one():
    total = 0
    for line in block_input_2.splitlines():
        item = {}
        for segment in line[1:-1].split(","):
            character, number = segment.split("=")
            item[character] = int(number)
        if accept(item):
            total += sum(item.values())
    print(total)


def count(ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1
        return product
    
    rules, fallback = workflows[name]
    
    total = 0
    
    for key, comparator, number, target in rules:
        low, high = ranges[key]
        if comparator == "<":
            true_half = (low, number - 1)
            false_half = (number, high)
        else:
            true_half = (number + 1, high)
            false_half = (low, number)
        if true_half[0] <= true_half[1]:
            copy = dict(ranges)
            copy[key] = true_half
            total += count(copy, target)
        if false_half[0] <= false_half[1]:
            ranges = dict(ranges)
            ranges[key] = false_half
        else:
            break
    else: # called when we break
        total += count(ranges, fallback)
            
    return total


def part_two():
    print(count({key: (1,4000) for key in "xmas"}))

part_one()
part_two()