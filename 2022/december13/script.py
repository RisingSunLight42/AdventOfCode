from copy import deepcopy
#pairs_list = []

# Ne fonctionne pas correctement
# with open("input.txt", "r", encoding="utf-8") as file:
#    pairs = []
#    for line in file.readlines():
#        line = line.replace("\n", "")
#        if line == "":
#            pairs_list.append(pairs)
#            pairs = []
#        else:
#            pairs.append(line)


# def create_list(list_pair, pair_string):
#    while len(pair_string) != 0:
#        if pair_string[0] == "]":
#            break
#        el = pair_string[0]
#        pair_string = pair_string[1:]
#        if el == "[":
#            pair, pair_string = create_list([], pair_string)
#            list_pair.append(pair)
#        elif el != ",":
#            list_pair.append(int(el))
#    return (list_pair, pair_string[1:])


# pairs_formatted_list = []
# for pairs in pairs_list:
#    pair_formatted_list = []
#    for pair in pairs:
#        create_list(pair_formatted_list, pair)
#    pairs_formatted_list.append(pair_formatted_list)


def check_pair(pair1, pair2):
    for i in range(min(len(pair1), len(pair2))):
        if isinstance(pair1[i], int) and isinstance(pair2[i], int):
            if pair1[i] < pair2[i]:
                return 1
            if pair1[i] > pair2[i]:
                return -1
        if isinstance(pair1[i], list) and isinstance(pair2[i], list):
            val_retour = check_pair(pair1[i], pair2[i])
            if val_retour != 0:
                return val_retour
        if isinstance(pair1[i], int) and isinstance(pair2[i], list):
            val_retour = check_pair([pair1[i]], pair2[i])
            if val_retour != 0:
                return val_retour
        if isinstance(pair1[i], list) and isinstance(pair2[i], int):
            val_retour = check_pair(pair1[i], [pair2[i]])
            if val_retour != 0:
                return val_retour
    if len(pair1) < len(pair2):
        return 1
    if len(pair1) > len(pair2):
        return -1
    return 0


def part_one():
    input = open("input.txt", "r").read().split("\n\n")
    sum_i = 0
    indice = 1
    for i in input:
        pair1, pair2 = [eval(r) for r in i.splitlines()]
        val_retour = check_pair(
            pair1, pair2)
        if val_retour == 1:
            sum_i += indice
        indice += 1
    return sum_i


def part_two():
    input = open("input.txt", "r").read().replace("\n\n", "\n").splitlines()
    input.append("[[2]]")
    input.append("[[6]]")

    input_copy = deepcopy(input)
    input = deepcopy([])
    while deepcopy(input) != deepcopy(input_copy):
        input = deepcopy(input_copy)
        input_copy = deepcopy([])
        for i in range(0, len(input), 2):
            pair1, pair2 = input[i:i+2]
            pair1, pair2 = eval(pair1), eval(pair2)
            val_retour = check_pair(pair1, pair2)
            if val_retour == 1:
                input_copy.append(input[i])
                input_copy.append(input[i+1])
            else:
                input_copy.append(input[i+1])
                input_copy.append(input[i])
        input = deepcopy(input_copy)
        input_copy = deepcopy([])
        input_copy.append(input[0])
        for i in range(1, len(input)-1, 2):
            pair1, pair2 = input[i:i+2]
            pair1, pair2 = eval(pair1), eval(pair2)
            val_retour = check_pair(pair1, pair2)
            if val_retour == 1:
                input_copy.append(input[i])
                input_copy.append(input[i+1])
            else:
                input_copy.append(input[i+1])
                input_copy.append(input[i])
        input_copy.append(input[-1])
    print(input_copy.index("[[2]]"))
    print(input_copy.index("[[6]]"))
    print((input_copy.index("[[2]]")+1)*(input_copy.index("[[6]]")+1))


part_two()
