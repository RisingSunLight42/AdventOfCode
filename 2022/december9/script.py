instructions_list = []

with open("./input.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        instructions_list.append(line)

bridge_visited = []

for i in range(2000):
    temp_tab = []
    for j in range(2000):
        temp_tab.append('.')
    bridge_visited.append(temp_tab)
bridge_visited[1999][0] = '#'


def is_touching(coord_H, coord_T):
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if ((coord_H[0] + i) == coord_T[0] and (coord_H[1] + j) == coord_T[1]):
                return True
    return False


def move_tail(coord_H, coord_T):
    if (coord_H[0] == coord_T[0]):
        if (coord_H[1] > coord_T[1]):
            coord_T[1] += 1
        else:
            coord_T[1] -= 1
    elif (coord_H[1] == coord_T[1]):
        if (coord_H[0] > coord_T[0]):
            coord_T[0] += 1
        else:
            coord_T[0] -= 1
    elif (coord_H[0] > coord_T[0]):
        if (coord_H[1] > coord_T[1]):
            coord_T[0] += 1
            coord_T[1] += 1
        else:
            coord_T[0] += 1
            coord_T[1] -= 1
    elif (coord_H[0] < coord_T[0]):
        if (coord_H[1] > coord_T[1]):
            coord_T[0] -= 1
            coord_T[1] += 1
        else:
            coord_T[0] -= 1
            coord_T[1] -= 1
    return coord_T


def execute_tail(coord_H, coord_T, pos):
    if (not is_touching(coord_H, coord_T)):
        coord_T = move_tail(coord_H, coord_T)
        if (pos == 9):
            bridge_visited[coord_T[0]][coord_T[1]] = '#'
        return coord_T
    return coord_T


def check_how_much_visited():
    visited = 0
    for i in range(len(bridge_visited)):
        for j in range(len(bridge_visited[i])):
            if bridge_visited[i][j] == '#':
                visited += 1
    return visited


def part_one():
    all_tails = []
    for _ in range(10):
        all_tails.append([499, 0])
    for instruction in instructions_list:
        movement = instruction.split(" ")[0]
        count = int(instruction.split(" ")[1])
        if movement == 'U':
            for _ in range(count):
                all_tails[0][0] -= 1
                for j in range(9):
                    all_tails[j +
                              1] = execute_tail(all_tails[j], all_tails[j + 1], j + 1)
        elif movement == 'R':
            for _ in range(count):
                all_tails[0][1] += 1
                for j in range(9):
                    all_tails[j +
                              1] = execute_tail(all_tails[j], all_tails[j + 1], j + 1)
        elif movement == 'D':
            for _ in range(count):
                all_tails[0][0] += 1
                for j in range(9):
                    all_tails[j +
                              1] = execute_tail(all_tails[j], all_tails[j + 1], j + 1)
        elif movement == 'L':
            for _ in range(count):
                all_tails[0][1] -= 1
                for j in range(9):
                    all_tails[j +
                              1] = execute_tail(all_tails[j], all_tails[j + 1], j + 1)
    print(check_how_much_visited())


part_one()