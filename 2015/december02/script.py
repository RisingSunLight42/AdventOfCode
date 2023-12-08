import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

lines = [list(map(int,re.findall("\d+", line))) for line in lines]

def part_one(lines=lines):
    square_feet_paper_total = 0
    for line in lines:
        length, width, height = line[0], line[1], line[2]
        calculation = (length*width, width*height, height*length)
        square_feet_paper_total += sum(calculation)*2 + min(calculation)
    print(square_feet_paper_total)

def part_two(lines=lines):
    ribbon_feet_total = 0
    for line in lines:
        length, width, height = line[0], line[1], line[2]
        ribbon_feet_total += 2*min(length+width, width+height, height+length)+length*width*height
    print(ribbon_feet_total)
        
part_one()
part_two()