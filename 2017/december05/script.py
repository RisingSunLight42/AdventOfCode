import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    instructions = [int(re.findall(r"-?\d+",line)[0]) for line in file.read().splitlines()]


def part_one():
    steps = 0
    index = 0
    while index >= 0 and index < len(instructions):
        previous_index = index
        index += instructions[index]
        instructions[previous_index] += 1
        steps += 1
    print(steps)


def part_two():
    index = 0
    steps = 0
    while 0 <= index < len(instructions):
        value = instructions[index]
        if value >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1
        index += value
        steps += 1
    print(steps)

#part_one()
part_two()