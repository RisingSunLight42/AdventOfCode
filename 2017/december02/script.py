import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = [list(map(int, re.findall(r"\d+",line))) for line in file.read().splitlines()]


def part_one():
    print(sum([max(numbers) - min(numbers) for numbers in lines]))


def part_two(lines=lines):
    total = 0
    for numbers in lines:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i == j:
                    continue
                if (numbers[i] % numbers[j]) == 0:
                    total += int(numbers[i] / numbers[j])
    print(total)

part_one()
part_two()