import re
import collections

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


# Part one
def part_one():
    valid_list = []
    for i in range(len(lines)):
        is_valid = False
        num = ''
        for j in range(len(lines[i])):
            if re.match(r"\d", lines[i][j]):
                num += lines[i][j]
                for x in range(max(0, i-1), min(i+2, len(lines))):
                    for y in range(max(0, j-1), min(j+2, len(lines[i]))):
                        if re.match(r"\W", lines[x][y]) and lines[x][y] != ".":
                            is_valid = True
            else:
                if is_valid:
                    valid_list.append(int(num))
                    is_valid = False
                num = ''
        if is_valid:
            valid_list.append(int(num))
            is_valid = False
            num = ''
    print(sum(valid_list))
     

# Part two
def part_two():
    total = 0
    
    print(total)
    

part_one()
