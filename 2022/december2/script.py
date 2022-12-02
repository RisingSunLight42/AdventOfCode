elf_play = []
self_play = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    for element in file.readlines():
        elf_play.append(element.split(" ")[0])
        self_play.append(element.split(" ")[1].replace("\n", ""))

dict_win = {"A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0,
                                                 "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}}
dict_movement_val = {"X": 1, "Y": 2, "Z": 3}

dict_win_condition = {"X": {"A": "Z", "B": "X", "C": "Y"}, "Y": {
    "A": "X", "B": "Y", "C": "Z"}, "Z": {"A": "Y", "B": "Z", "C": "X"}}

# Part one


def part_one():
    total_score = 0
    for i in range(len(elf_play)):
        score = dict_win[elf_play[i]][self_play[i]
                                      ] + dict_movement_val[self_play[i]]
        if (i % 10 == 0):
            print(f"{score} {elf_play[i]} {self_play[i]}")
        total_score += score
    print(total_score)


# part_one()
# Part two


def part_two():
    total_score = 0
    for i in range(len(elf_play)):
        move_to_play = dict_win_condition[self_play[i]][elf_play[i]]
        score = dict_win[elf_play[i]][move_to_play
                                      ] + dict_movement_val[move_to_play]
        total_score += score
    print(total_score)


part_two()
