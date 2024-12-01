first_row = []
second_row = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        splitted_line = line.split("   ")
        first_row.append(int(splitted_line[0]))
        second_row.append(int(splitted_line[1].replace("\n", "")))


# Part one
def part_one():
    distance = 0
    first_row.sort()
    second_row.sort()
    for i in range(len(first_row)):
        distance += abs(first_row[i]-second_row[i])


# Part two
def part_two():
    dict_result = {}
    for element in first_row:
        dict_result[element] = second_row.count(element)
    score = 0
    for key in dict_result.keys():
        score += key * dict_result[key]
    print(score)

part_two()