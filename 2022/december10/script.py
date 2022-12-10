instructions_list: str = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        instructions_list.append(line)


def part_one():
    x_value = 1
    cycle = 0
    strength_list = []
    for instru in instructions_list:
        if "addx" in instru and cycle + 1 in [20, 60, 100, 140, 180, 220]:
            strength_list.append((cycle + 1) * x_value)
        if "addx" in instru:
            cycle += 2
            if cycle in [20, 60, 100, 140, 180, 220]:
                strength_list.append(cycle * x_value)
            x_value += int(instru.split(" ")[1])
        else:
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                strength_list.append(cycle * x_value)

    print(strength_list)
    print(sum(strength_list))


# part_one()


def part_two():
    list_draw = []
    for _ in range(6):
        temp_list = []
        for _ in range(40):
            temp_list.append(".")
        list_draw.append(temp_list)
    x_value = 1
    cycle = 0
    sprite_pos = [0, 1, 2]
    for instru in instructions_list:
        if "addx" in instru:
            for i in range(2):
                if (cycle) % 40 in sprite_pos:
                    list_draw[cycle // 40 -
                              int(cycle % 40 == 0)][cycle % 40] = "#"
                cycle += 1
            x_value += int(instru.split(" ")[1])
            sprite_pos = [x_value - 1, x_value, x_value + 1]
        else:
            if (cycle) % 40 in sprite_pos:
                list_draw[cycle // 40 -
                          int(cycle % 40 == 0)][cycle % 40] = "#"
            cycle += 1
    for element in list_draw:
        line = ""
        for char in element:
            line += char
        print(line)


part_two()
