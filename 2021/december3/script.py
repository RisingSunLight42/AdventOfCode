binaries_list = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    binaries_list = file.readlines()


def first_part():
    dict_apparition = {}
    for i in range(len(binaries_list[0]) - 1):
        dict_apparition[i] = {"0": 0, "1": 0}
    for binary in binaries_list:
        binary = binary.replace("\n", "")
        for i in range(len(binary)):
            dict_apparition[i][binary[i]] += 1
    # reconstruction binary for gamma and espilon
    print(dict_apparition)
    gamma = ""
    espilon = ""
    for val in dict_apparition.values():
        if (val['0'] < val['1']):
            gamma += '1'
            espilon += '0'
        else:
            gamma += '0'
            espilon += '1'
    print(int(gamma, 2) * int(espilon, 2))


first_part()
