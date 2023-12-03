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

def second_part():
    oxygen_gen = binaries_list.copy()
    c02_rating = binaries_list.copy()
    iterator = 0
    for i in range(len(binaries_list[0]) - 1):
        count_oxygen = [0, 0]
        count_c02 = [0, 0]
        for binary in oxygen_gen:
            if binary[iterator] == '0':
                count_oxygen[0] += 1
            else:
                count_oxygen[1] += 1
        for binary in c02_rating:
            if binary[iterator] == '0':
                count_c02[0] += 1
            else:
                count_c02[1] += 1
        value_filter_oxygen = '1'
        value_filter_co0 = '0'
        if count_oxygen[0] > count_oxygen[1]:
            value_filter_oxygen = '0'
        if count_c02[0] > count_c02[1]:
            value_filter_co0 = '1'
        if len(oxygen_gen) != 1:
            oxygen_gen = list(filter(lambda given_item: given_item[iterator] == value_filter_oxygen, oxygen_gen))
        if len(c02_rating) != 1:
            c02_rating = list(filter(lambda given_item: given_item[iterator] == value_filter_co0, c02_rating))
        iterator += 1
    print(str(int(oxygen_gen[0].replace("\n", ""), 2)) + " " + str(int(c02_rating[0].replace("\n", ""), 2)))
    print(int(oxygen_gen[0].replace("\n", ""), 2) * int(c02_rating[0].replace("\n", ""), 2))
    
second_part()
