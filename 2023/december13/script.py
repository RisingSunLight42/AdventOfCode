with open("./input.txt", 'r', encoding='utf-8') as file:
    grids = [block.splitlines() for block in file.read().split("\n\n")]
    

def find_mirror(grid):
    for i in range(1, len(grid)):
        above = grid[:i][::-1] # Flip the top of the grid to be aligned with the below
        below = grid[i:]
        
        # Remove what doesn't exist in both
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return i
    return 0


def part_one():
    total = 0
    for grid in grids:
        row = find_mirror(grid)
        total += 100 * row
        
        grid_flipped = list(zip(*grid)) # flip the grid to get horizontal on diagonal
        total += find_mirror(grid_flipped)
    print(total)


def find_mirror_with_smudge(grid):
    for i in range(1, len(grid)):
        above = grid[:i][::-1] # Flip the top of the grid to be aligned with the below
        below = grid[i:]
        
        mismatches = 0
        for x, y in zip(above, below):
            for a, b in zip(x, y):
                mismatches += a != b
        
        if mismatches == 1:
            return i
    return 0


def part_two():
    total = 0
    for grid in grids:
        row = find_mirror_with_smudge(grid)
        total += 100 * row
        
        grid_flipped = list(zip(*grid)) # flip the grid to get horizontal on diagonal
        total += find_mirror_with_smudge(grid_flipped)
    print(total)

part_one()
part_two()