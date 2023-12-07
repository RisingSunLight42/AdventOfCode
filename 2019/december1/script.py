from math import floor

with open("./input.txt", 'r', encoding='utf-8') as file:
    mass_list = [int(line) for line in file.read().splitlines()]


def part_one():
    print(sum([floor(mass/3)-2 for mass in mass_list]))


def part_two():
    total = 0
    for mass in mass_list:
        calc = subtotal = floor(mass/3)-2
        while calc != 0:
            calc = floor(calc/3)-2
            calc = 0 if calc < 0 else calc
            subtotal += calc
        total += subtotal
    print(total)

part_one()
part_two()