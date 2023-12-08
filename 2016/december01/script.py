import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    direction_distance = [(direction_and_distance[0], int(direction_and_distance[1:])) for direction_and_distance in re.findall(r"\w\d+", file.read())]

rotation = { "L": -90, "R": 90}


def part_one():
    x = 0
    y = 0
    angle = 0
    for direction, distance in direction_distance:
        angle += rotation[direction]
        angle = angle % 360
        if angle == 0:
            y += distance
        elif angle == 90:
            x += distance
        elif angle == 180:
            y -= distance
        elif angle == 270:
            x -= distance
    print(abs(x) + abs(y))


heading_value = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}
def part_two():
    x = 0
    y = 0
    angle = 0
    visited = set()
    visited.add((x, y))
    for direction, distance in direction_distance:
        angle += rotation[direction]
        angle = angle % 360
        heading = heading_value[angle]
        for _ in range(distance):
            x += heading[0]
            y += heading[1]
            if ((x,y) in visited):
                print(abs(x) + abs(y))
                return
            else: visited.add((x, y))

part_one()
part_two()