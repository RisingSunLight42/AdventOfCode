import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read()

def part_one(lines=lines):
    print(sum([1 if parenthesis == "(" else -1 for parenthesis in lines]))
    # or print(lines.count('(')-lines.count(')')), but the first one is funnied and is probably better in term of perf

def part_two(lines=lines):
    value = 0
    for i in range(len(lines)):
        value += 1 if lines[i] == "(" else -1
        if (value == -1):
            print(i+1)
            break
        
part_one()
part_two()