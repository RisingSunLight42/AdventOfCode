from collections import deque

with open("./input.txt", 'r', encoding='utf-8') as file:
    grid = file.read().splitlines()


def determine_source():
    for i in range(len(grid)):
        if "S" in grid[i]:
            return i, grid[i].index("S")


def fill(src_row, src_col, steps_given):
    answer = set()
    seen = {(src_row, src_col)}
    queue = deque([(src_row, src_col, steps_given)])
    
    while queue:
        row, col, steps = queue.popleft()
        
        if steps % 2 == 0:
            answer.add((row, col))
        if steps == 0:
            continue
        
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]) \
            or grid[next_row][next_col] == "#" or (next_row, next_col) in seen:
                continue
            seen.add((next_row, next_col))
            queue.append((next_row, next_col, steps - 1))
    return len(answer)


def part_one():
    src_row, src_col = determine_source()
    print(fill(src_row, src_col, 64))


# S is in a row and column empty and every border of the input are empty too (.)
def part_two():
    src_row, src_col = determine_source()
    
    assert len(grid) == len(grid[0]) # assume it is a square
    size = len(grid)
    steps = 26501365
    assert src_row == src_col == size // 2
    assert steps % size == size // 2 # no works for test data, but confident it is correct because steps // size = 202300
    
    grids_count = steps // size - 1
    odd_grids_count = (grids_count // 2 * 2 + 1) ** 2
    even_grids_count = ((grids_count +1) // 2 * 2) ** 2
    
    odd_points = fill(src_row, src_col, size * 2 + 1) # determine the number of odd points reached when we're walking in all the grid
    even_points = fill(src_row, src_col, size * 2) # determine the number of even points reached when we're walking in all the grid
    
    # now we need to determine the number of points reached for the last grid in the infinite expansion
    # which can't be completely full travelled, so we need to handler corners
    corner_top = fill(size-1, src_col, size - 1) # size - 1 to enter at the bottom row of the grid
    corner_right = fill(src_row, 0, size - 1)
    corner_bottom = fill(0, src_col, size - 1)
    corner_left = fill(src_row, size - 1, size - 1)
    
    # Now we need to handle the cases where we can read another grid that is at the end, but on a diagonal
    # (it can be represented by a small triangle created by a line crossing an L shape)
    small_top_right = fill(size - 1, 0, size // 2 - 1)
    small_top_left = fill(size - 1, size - 1, size // 2 - 1)
    small_bottom_right = fill(0, 0, size // 2 - 1)
    small_botton_left = fill(0, size-1, size // 2 - 1)
    
    # Now we need to handle the cases where we're in a grid at the end, but in a diagonal arrangement
    # so we cannot reach all the points possible on this grid
    large_top_right = fill(size - 1, 0, size * 3 // 2 - 1)
    large_top_left = fill(size - 1, size - 1, size * 3 // 2 - 1)
    large_bottom_right = fill(0, 0, size * 3 // 2 - 1)
    large_botton_left = fill(0, size-1, size * 3 // 2 - 1)
    
    print(odd_grids_count * odd_points +
          even_grids_count * even_points +
          corner_top + corner_right +
          corner_bottom + corner_left +
          (grids_count + 1) * (small_top_right + small_top_left + small_bottom_right + small_botton_left) +
          grids_count * (large_top_right + large_top_left + large_bottom_right + large_botton_left))

part_one()
part_two()