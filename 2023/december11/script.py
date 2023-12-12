from itertools import combinations

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

def part_one(value=2):
    galaxies = [[y,x] for x in range(len(lines[0])) for y in range(len(lines)) if lines[y][x] == '#']
    line_insert = [y for y, line in enumerate(lines) if line.count('#') == 0]
    col_insert = [x for x in range(len(lines[0])) if [line[x] for line in lines].count('#') == 0]
    
    for x in reversed(col_insert):
        for galaxy in galaxies:
            if galaxy[1] > x:
                galaxy[1] += value-1
                
    for y in reversed(line_insert):
        for galaxy in galaxies:
            if galaxy[0] > y:
                galaxy[0] += value-1
    
    print(sum(abs(galaxy_second[0]-galaxy_first[0]) + abs(galaxy_second[1]-galaxy_first[1]) for galaxy_first, galaxy_second in combinations(galaxies, 2)))

def part_two():
    part_one(1_000_000)

part_one()
part_two()