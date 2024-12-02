with open("./input.txt", 'r', encoding='utf-8') as file:
    inputData = [list(map(int, line.split(" "))) for line in file.read().splitlines()]

def is_safe(line):
    differences = [x - y for x, y in zip(line, line[1:])]
    return all(1 <= x <= 3 for x in differences) or all(-1 >= x >= -3 for x in differences)

# one-liner ver
def is_safe(line):
    return all(1 <= x <= 3 for x in [x - y for x, y in zip(line, line[1:])]) or all(-1 >= x >= -3 for x in [x - y for x, y in zip(line, line[1:])])

# Part one
def part_one():
    print(sum([is_safe(line) for line in inputData]))

# Part two
def part_two():
    print(sum([any(is_safe(line[:index] + line[index + 1:]) for index in range(len(line))) for line in inputData]))


part_one()
part_two()