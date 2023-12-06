import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read()
    
dict_matching_coords_x = { "^": 1, "v": -1, "<": 0, ">": 0}
dict_matching_coords_y = { "^": 0, "v": 0, "<": -1, ">": 1}

def part_one(lines=lines):
    coords = [0, 0]
    visited_coords = set()
    for direction in lines:
        coords[1] += dict_matching_coords_x[direction]
        coords[0] += dict_matching_coords_y[direction]
        visited_coords.add(tuple(coords))
    visited_coords.add(tuple([0, 0]))
    print(len(visited_coords))

def part_two(lines=lines):
    coords_santa = [0, 0]
    coords_robot = [0, 0]
    visited_coords = set()
    is_santa = True
    for direction in lines:
        coords = coords_santa if is_santa else coords_robot
        coords[1] += dict_matching_coords_x[direction]
        coords[0] += dict_matching_coords_y[direction]
        visited_coords.add(tuple(coords))
        is_santa = not is_santa
    visited_coords.add(tuple([0, 0]))
    print(len(visited_coords))
        
part_one()
part_two()