import re

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


def do_validation_part_one(valid_list, num, is_valid):
    if is_valid:
        valid_list.append(num)
    return False, '0'

# Part one
def part_one():
    valid_list = []
    is_valid = False
    num = '0'
    number_of_lines = len(lines)
    for i in range(number_of_lines):
        is_valid, num = do_validation_part_one(valid_list, int(num), is_valid)
        number_of_characters = len(lines[i])
        for j in range(number_of_characters):
            if re.match(r"\d", lines[i][j]):
                num += lines[i][j]
                for x in range(max(0, i-1), min(i+2, number_of_lines)):
                    for y in range(max(0, j-1), min(j+2, number_of_characters)):
                        if re.match(r"\W", lines[x][y]) and lines[x][y] != ".":
                            is_valid = True
            else:
                is_valid, num = do_validation_part_one(valid_list, int(num), is_valid)
    print(sum(valid_list))
     
def do_validation_part_two(dictionnary, coordinate_save, valid_list, num, is_valid):
    if not is_valid:
        return False, '0', []
    valid_list.append(num)
    str_valid = f"{coordinate_save[0],coordinate_save[1]}"
    if str_valid in dictionnary.keys():
        dictionnary[str_valid].append(num)
    else:
        dictionnary[str_valid] = [num]
    return False, '0', []

# Part two
def part_two():
    # Search for numbers in the lines and when found, check around them to find special character *
    # if the character is found, add the number corresponding in a dictionny with in key, the coordinates of the *
    valid_list = []
    valid_coordinates = {}
    num = '0'
    is_valid = False
    coordinate_save = []
    for i in range(len(lines)):
        is_valid, num, coordinate_save = do_validation_part_two(valid_coordinates, coordinate_save, valid_list, int(num), is_valid)
        for j in range(len(lines[i])):
            if re.match(r"\d", lines[i][j]):
                num += lines[i][j]
                for x in range(max(0, i-1), min(i+2, len(lines))):
                    for y in range(max(0, j-1), min(j+2, len(lines[i]))):
                        if lines[x][y] == "*":
                            is_valid = True
                            coordinate_save = [x, y]
            else:
                is_valid, num, _ = do_validation_part_two(valid_coordinates, coordinate_save, valid_list, int(num), is_valid)
    gear_ratio_sum = 0
    for gears in valid_coordinates.values():
        if len(gears) == 2:
            gear_ratio_sum += gears[0] * gears[1]
    print(gear_ratio_sum)
    

part_two()
