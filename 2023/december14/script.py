with open("./input.txt", 'r', encoding='utf-8') as file:
    grid = tuple(file.read().splitlines())


def part_one(grid=grid):
    grid = list(map("".join, zip(*grid)))
    new_grid = []
    for row in grid:
        new_row = []
        for group in row.split("#"):
            move_rocks = sorted(list(group), reverse=True)
            new_row.append("".join(move_rocks))
        new_grid.append("#".join(new_row))
    grid = list(map("".join, zip(*new_grid)))

    print(sum(row.count("O") * (len(grid) - i) for i, row in enumerate(grid)))


part_one()

def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid) # oneliner version of part_one
        grid = tuple(row[::-1] for row in grid) # make a rotation clockwise

def part_two(grid=grid):
    global grid
    seen = {grid}
    array = [grid]
    iteration = 0
    while True:
        iteration += 1
        cycle()
        if grid in seen:
            break
        seen.add(grid)
        array.append(grid)
        
    first = array.index(grid)
        
    grid = array[(1_000_000_000 - first) % (iter - first) + first]
    print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))


part_two()