import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    frequencies = [int(re.findall(r".\d+", line)[0]) for line in file.read().splitlines()]


def part_one():
    print(sum(frequencies))


def part_two():
    iterator = 0
    is_found = False
    frequency = 0
    frequencies_seen = set()
    frequencies_seen.add(frequency)
    while not is_found:
        frequency += frequencies[iterator]
        if frequency in frequencies_seen:
            is_found = True
        else:
            frequencies_seen.add(frequency)
        iterator = (iterator + 1) % len(frequencies)
    print(frequency)

part_one()
part_two()