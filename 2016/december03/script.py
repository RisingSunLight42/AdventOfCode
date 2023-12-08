import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    triangles = [list(map(int, re.findall(r"\d+", line))) for line in file.read().splitlines()]


def part_one():
    valid = 0
    for triangle in triangles:
        two_smallest_side = []
        for i in range(2):
            mini = min(triangle)
            triangle.remove(mini)
            two_smallest_side.append(mini)
        valid += sum(two_smallest_side) > triangle[0]
    print(valid)


def part_two():
    valid = 0
    for i in range(len(triangles[0])):
        for j in range(0, len(triangles) - 2, 3):
            two_smallest_side = []
            triangle = [triangles[j][i], triangles[j+1][i], triangles[j+2][i]]
            for k in range(2):
                mini = min(triangle)
                triangle.remove(mini)
                two_smallest_side.append(mini)
            valid += sum(two_smallest_side) > triangle[0]
    print(valid)

# part_one()
part_two()