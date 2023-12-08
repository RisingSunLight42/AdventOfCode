import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

def part_one(lines=lines):
    nice_string_nb = 0
    for string in lines:
        if re.search(r"([aeiou].*){3,}", string) and re.search(r"(.)\1", string) and not re.search(r"ab|cd|pq|xy", string):
            nice_string_nb += 1
    print(nice_string_nb)


def part_two(lines=lines):
    nice_string_nb = 0
    for string in lines:
        if re.search(r'(..).*\1', string) and re.search(r'(.).\1', string):
            nice_string_nb += 1
    print(nice_string_nb)

part_one()
part_two()