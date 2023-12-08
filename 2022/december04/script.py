first_pairs = []
second_pairs = []

with open("./input.txt", 'r', encoding='utf-8') as file:
    for element in file.readlines():
        el_splitted = element.split(",")
        first_pairs.append(el_splitted[0].split("-"))
        second_pairs.append(el_splitted[1].split("-"))


def first_part():
    number_fully_contained = 0
    for i in range(len(first_pairs)):
        if int(first_pairs[i][0]) <= int(second_pairs[i][0]) and int(first_pairs[i][1]) >= int(second_pairs[i][1]):
            number_fully_contained += 1
        elif int(first_pairs[i][0]) >= int(second_pairs[i][0]) and int(first_pairs[i][1]) <= int(second_pairs[i][1]):
            number_fully_contained += 1
    print(number_fully_contained)


# first_part()
def second_part():
    number_fully_contained = 0
    for i in range(len(first_pairs)):
        if int(second_pairs[i][0]) <= int(first_pairs[i][0]) <= int(second_pairs[i][0]) or int(second_pairs[i][0]) <= int(first_pairs[i][1]) <= int(second_pairs[i][1]):
            number_fully_contained += 1
        elif int(first_pairs[i][0]) <= int(second_pairs[i][0]) <= int(first_pairs[i][0]) or int(first_pairs[i][0]) <= int(second_pairs[i][1]) <= int(first_pairs[i][1]):
            number_fully_contained += 1
    print(number_fully_contained)


second_part()
