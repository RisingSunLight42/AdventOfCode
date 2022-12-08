forest = []

with open("./input.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        forest.append(line)


def check_visible(i, j):
    row_not_visible = 0
    for z in range(i):
        if (forest[i][j] <= forest[z][j]):
            row_not_visible += 1
            break
    for z in range(j):
        if (forest[i][j] <= forest[i][z]):
            row_not_visible += 1
            break
    for z in range(i + 1, len(forest), 1):
        if (forest[i][j] <= forest[z][j]):
            row_not_visible += 1
            break
    for z in range(j + 1, len(forest), 1):
        if (forest[i][j] <= forest[i][z]):
            row_not_visible += 1
            break
    return row_not_visible


def part_one():
    visible = 0
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[i]) - 1:
                visible += 1
                continue
            row_not_visible = check_visible(i, j)
            if (row_not_visible != 4):
                visible += 1
    print(visible)


def calculate_scenic(i, j):
    tree_visible = [0, 0, 0, 0]
    for z in range(i - 1, -1, -1):
        tree_visible[0] += 1
        if (forest[i][j] <= forest[z][j]):
            break
    for z in range(j - 1, -1, -1):
        tree_visible[1] += 1
        if (forest[i][j] <= forest[i][z]):
            break
    for z in range(i + 1, len(forest), 1):
        tree_visible[2] += 1
        if (forest[i][j] <= forest[z][j]):
            break
    for z in range(j + 1, len(forest), 1):
        tree_visible[3] += 1
        if (forest[i][j] <= forest[i][z]):
            break
    return tree_visible


def part_two():
    best_scenic = 0
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            scenic_tab = calculate_scenic(i, j)
            scenic_score = scenic_tab[0] * \
                scenic_tab[1] * scenic_tab[2] * scenic_tab[3]
            if (scenic_score > best_scenic):
                best_scenic = scenic_score
    print(best_scenic)


part_two()
