import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    bank_numbers = list(map(int, re.findall(r"\d+",file.read())))


def part_one(bank_numbers=bank_numbers):
    seen = [bank_numbers.copy()]
    
    no_cycle = True
    steps = 0
    while no_cycle:
        index = bank_numbers.index(max(bank_numbers))
        redistributed_value = bank_numbers[index]
        bank_numbers[index] = 0
        while redistributed_value != 0:
            index = (index + 1) % len(bank_numbers)
            bank_numbers[index] += 1
            redistributed_value -= 1
        steps += 1
        if bank_numbers in seen:
            no_cycle = False
        else:
            seen.append(bank_numbers.copy())
    print(steps)


def part_two():
    seen = [bank_numbers.copy()]
    
    no_cycle = True
    steps = 0
    while no_cycle:
        index = bank_numbers.index(max(bank_numbers))
        redistributed_value = bank_numbers[index]
        bank_numbers[index] = 0
        while redistributed_value != 0:
            index = (index + 1) % len(bank_numbers)
            bank_numbers[index] += 1
            redistributed_value -= 1
        steps += 1
        if bank_numbers in seen:
            print(len(seen) - seen.index(bank_numbers))
            no_cycle = False
        else:
            seen.append(bank_numbers.copy())

#part_one()
part_two()