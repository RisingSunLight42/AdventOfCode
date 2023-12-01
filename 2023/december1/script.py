import re

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Part one


def part_one():
    total = 0
    for line in lines:
        all_digit_matches = re.findall("\d", line)
        total += int(all_digit_matches[0] + all_digit_matches[-1])
    print(total)
        

# Part two

match_dict = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def part_two():
    total = 0
    for line in lines:
        all_matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        first = all_matches[0]
        last = all_matches[-1]
        first = first if first.isdigit() else match_dict[first]
        last = last if last.isdigit() else match_dict[last]
        total += int(first + last)
    print(total)
    

part_two()

