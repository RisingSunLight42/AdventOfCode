import re
from collections import deque

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read() 

lines = lines.split("\n\n")

def parse_input_part_one(lines) :
    seeds = deque(map(int, re.findall(r"\d+", lines[0])))
    lines = lines[1:]
    maps = []
    for line in lines:
        map_single = []
        for map_s in line.split("\n")[1:]:
            map_single.append(list(map(int, re.findall(r"\d+",map_s))))
        maps.append(map_single)
    dict_seeds = {i: deque() for i in range(len(maps) + 1)}
    dict_seeds[0] = seeds
    return maps, dict_seeds

def part_one(lines):
    maps, dict_seeds = parse_input_part_one(lines)
    i = 0
    for map_single in maps:
        added_seeds = set()
        for seed in dict_seeds[i]:
            for convert in map_single:
                if convert[1] <= seed < (convert[1] + convert[2]):
                    dict_seeds[i+1].append(convert[0] + (seed - convert[1]))
                    added_seeds.add(seed)
                    break
        for not_added_seed in set(dict_seeds[i]).difference(added_seeds):
            dict_seeds[i+1].append(not_added_seed)
        i += 1
    print(min(dict_seeds[7]))


part_two(lines)