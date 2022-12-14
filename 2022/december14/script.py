x_min, x_max = 500, 500
y_min, y_max = 0, 0
dict_emp_roche = {}

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        rocks_path = line.split(" -> ")
        for i in range(len(rocks_path) - 1):
            rocks_pos_src = rocks_path[i].split(",")
            rocks_pos_dest = rocks_path[i + 1].split(",")
            rocks_pos_src = (
                int(rocks_pos_src[0]), int(rocks_pos_src[1]))
            rocks_pos_dest = (
                int(rocks_pos_dest[0]), int(rocks_pos_dest[1]))
            if (x_min > rocks_pos_src[0]):
                x_min = rocks_pos_src[0]
            if (x_min > rocks_pos_dest[0]):
                x_min = rocks_pos_dest[0]
            if (x_max < rocks_pos_src[0]):
                x_max = rocks_pos_src[0]
            if (x_max < rocks_pos_dest[0]):
                x_max = rocks_pos_dest[0]

            if (y_min > rocks_pos_src[1]):
                y_min = rocks_pos_src[1]
            if (y_min > rocks_pos_dest[1]):
                y_min = rocks_pos_dest[1]
            if (y_max < rocks_pos_src[1]):
                y_max = rocks_pos_src[1]
            if (y_max < rocks_pos_dest[1]):
                y_max = rocks_pos_dest[1]

            if (rocks_pos_src[0] == rocks_pos_dest[0]):

                if (rocks_pos_src[1] < rocks_pos_dest[1]):
                    for j in range(rocks_pos_src[1], rocks_pos_dest[1] + 1):
                        dict_emp_roche[(rocks_pos_src[0], j)] = "#"

                elif (rocks_pos_src[1] > rocks_pos_dest[1]):
                    for j in range(rocks_pos_dest[1], rocks_pos_src[1] + 1):
                        dict_emp_roche[(rocks_pos_src[0], j)] = "#"

            elif (rocks_pos_src[1] == rocks_pos_dest[1]):

                if (rocks_pos_src[0] < rocks_pos_dest[0]):
                    for j in range(rocks_pos_src[0], rocks_pos_dest[0] + 1):
                        dict_emp_roche[(j, rocks_pos_src[1])] = "#"

                elif (rocks_pos_src[0] > rocks_pos_dest[0]):
                    for j in range(rocks_pos_dest[0], rocks_pos_src[0] + 1):
                        dict_emp_roche[(j, rocks_pos_src[1])] = "#"

    # print(dict_emp_roche)
    # print(x_min, x_max)
    # print(y_min, y_max)


def genere_carte():
    carte = []
    for i in range(y_min, y_max + 1):
        medium_carte = []
        for j in range(x_min, x_max + 1):
            if ((j, i) in dict_emp_roche.keys()):
                medium_carte.append("#")
            else:
                medium_carte.append(".")
        carte.append(medium_carte)
    return carte


def part_one():
    carte = genere_carte()
    limite_reach = False
    sand_number = 0
    while not limite_reach:
        if carte[0][500 % x_min] == "o":
            limite_reach = True
        sand_coord = [0, 500 % x_min]
        carte[0][500 % x_min] = "o"
        sand_number += 1
        can_move = True
        while can_move:
            if sand_coord[0] + 1 <= y_max:
                if carte[sand_coord[0] + 1][sand_coord[1]] == ".":
                    carte[sand_coord[0]][sand_coord[1]] = "."
                    sand_coord[0] += 1
                    carte[sand_coord[0]][sand_coord[1]] = "o"
                else:
                    if sand_coord[1] - 1 >= 0:
                        if carte[sand_coord[0] + 1][sand_coord[1] - 1] == ".":
                            carte[sand_coord[0]][sand_coord[1]] = "."
                            sand_coord[0] += 1
                            sand_coord[1] -= 1
                            carte[sand_coord[0]][sand_coord[1]] = "o"
                        else:
                            if sand_coord[1] + 1 <= x_max % x_min:
                                if carte[sand_coord[0] + 1][sand_coord[1] + 1] == ".":
                                    carte[sand_coord[0]][sand_coord[1]] = "."
                                    sand_coord[0] += 1
                                    sand_coord[1] += 1
                                    carte[sand_coord[0]][sand_coord[1]] = "o"
                                else:
                                    can_move = False
                            else:
                                limite_reach = True
                                can_move = False
                    else:
                        limite_reach = True
                        can_move = False
            else:
                limite_reach = True
                can_move = False
    print(sand_number - 1)


# part_one()


def part_two():
    carte = genere_carte()
    sand_number = 0
    for i in range(len(carte)):
        sand_number += 1 + 2*i
        rock_number = 0
        for c in carte[i]:
            if c == "#":
                rock_number += 1
        if (i > 0):
            for j in range(1, len(carte[i]) - 1):
                # Get the top 3 spaces
                pos1 = carte[i - 1][j - 1]
                pos2 = carte[i - 1][j]
                pos3 = carte[i - 1][j + 1]

                # If this is an empty space and the top 3 spaces are rocks, then sand cannot
                # go here. We also replace this space with a rock so that the effect cascades down.
                if carte[i][j] == '.' and pos1 == '#' and pos2 == '#' and pos3 == '#':
                    carte[i][j] = '#'
                    sand_number -= 1

        sand_number -= rock_number
    print(sand_number)


def genere_carte_dumb(x_min, x_max):
    carte = []
    for i in range(y_min, y_max + 1):
        medium_carte = []
        for j in range(x_min, x_max + 1):
            if ((j, i) in dict_emp_roche.keys()):
                medium_carte.append("#")
            else:
                medium_carte.append(".")
        carte.append(medium_carte)
    return carte


def part_two_dumb(x_min, x_max):
    x_min -= 500
    x_max += 500
    print(x_min, x_max)
    carte = genere_carte_dumb(x_min, x_max)
    limite_reach = False
    sand_number = 0
    while not limite_reach:
        if carte[0][500] == "o":
            limite_reach = True
        sand_coord = [0, 500]
        carte[0][500] = "o"
        sand_number += 1
        can_move = True
        while can_move:
            if sand_coord[0] + 1 <= y_max:
                if carte[sand_coord[0] + 1][sand_coord[1]] == ".":
                    carte[sand_coord[0]][sand_coord[1]] = "."
                    sand_coord[0] += 1
                    carte[sand_coord[0]][sand_coord[1]] = "o"
                else:
                    if sand_coord[1] - 1 >= 0:
                        if carte[sand_coord[0] + 1][sand_coord[1] - 1] == ".":
                            carte[sand_coord[0]][sand_coord[1]] = "."
                            sand_coord[0] += 1
                            sand_coord[1] -= 1
                            carte[sand_coord[0]][sand_coord[1]] = "o"
                        else:
                            if sand_coord[1] + 1 <= x_max:
                                if carte[sand_coord[0] + 1][sand_coord[1] + 1] == ".":
                                    carte[sand_coord[0]][sand_coord[1]] = "."
                                    sand_coord[0] += 1
                                    sand_coord[1] += 1
                                    carte[sand_coord[0]][sand_coord[1]] = "o"
                                else:
                                    can_move = False
                            else:
                                can_move = False
                    else:
                        can_move = False
            else:
                can_move = False
    print(sand_number - 1)


part_two_dumb(x_min, x_max)
