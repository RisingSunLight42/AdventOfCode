dict_pile = {}
list_actions = []

with open("./input.txt", 'r', encoding='utf-8') as file:
    list_pile = []
    for line in file.readlines():
        if "[" in line:
            pile_section = []
            for crates_list in line.split("    "):
                for crate in crates_list.split(" "):
                    pile_section.append(crate)
            list_pile.append(pile_section)
        elif "move" in line:
            actions = line.split(" ")
            list_actions.append([int(actions[1]),
                                 int(actions[3]),
                                 int(actions[5]),
                                 ])
    for i in range(len(list_pile[0])):
        dict_pile[i + 1] = []
    for i in range(len(list_pile) - 1, -1, -1):
        for j in range(len(list_pile[i])):
            if list_pile[i][j] != '':
                dict_pile[j + 1].append(list_pile[i][j][1])


def first_part():
    for actions in list_actions:
        for i in range(actions[0]):
            dict_pile[actions[2]].append(dict_pile[actions[1]][-(i + 1)])
        dict_pile[actions[1]] = dict_pile[actions[1]
                                          ][:len(dict_pile[actions[1]]) - actions[0]]
    char_response = ""
    for key in dict_pile.keys():
        char_response += dict_pile[key][len(dict_pile[key]) - 1]
    print(char_response)


# first_part()


def second_part():
    for actions in list_actions:
        temp_pile = []
        for i in range(actions[0]):
            temp_pile.append(dict_pile[actions[1]][-(i + 1)])
        for i in range(len(temp_pile) - 1, -1, -1):
            dict_pile[actions[2]].append(temp_pile[i])
        dict_pile[actions[1]] = dict_pile[actions[1]
                                          ][:len(dict_pile[actions[1]]) - actions[0]]
    char_response = ""
    for key in dict_pile.keys():
        char_response += dict_pile[key][len(dict_pile[key]) - 1]
    print(char_response)


second_part()
