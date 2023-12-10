from collections import Counter

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


        

def part_one():
    column = []
    str_column = ''
    str_corrected = ''
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            str_column += lines[j][i]
        str_corrected += Counter(str_column).most_common()[0][0][0]
        str_column = ''
    print(str_corrected)


def part_two():
    column = []
    str_column = ''
    str_corrected = ''
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            str_column += lines[j][i]
        str_corrected += Counter(str_column).most_common()[-1][0][0]
        str_column = ''
    print(str_corrected)

part_one()
part_two()