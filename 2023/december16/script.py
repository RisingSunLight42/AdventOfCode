from collections import deque

with open("./input.txt", 'r', encoding='utf-8') as file:
    grid = file.read().splitlines()


def update_seen_and_queue(element, seen, queue):
    if element in seen:
        return
    seen.add(element)
    queue.append(element)


def part_one(grid=grid, row=0, column=-1, direction_row=0, direction_column=1):
    a = [(row, column, direction_row, direction_column)]
    seen = set()
    queue = deque(a)

    while queue:
        row, column, direction_row, direction_column = queue.popleft()

        row += direction_row
        column += direction_column

        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            continue

        char = grid[row][column]
        
        if char == "." or (char == "-" and direction_column != 0) or (char == "|" and direction_row != 0):
            update_seen_and_queue((row, column, direction_row, direction_column), seen, queue)
        elif char == "/":
            # if we analysis movement of beam changing when we meet a /, it's basically flipping the two direction and changing their sign
            # e.g. : (0, 1) -> (-1, 0), when we come from left, we go down
            direction_row, direction_column = -direction_column, -direction_row
            update_seen_and_queue((row, column, direction_row, direction_column), seen, queue)
        elif char == "\\":
            # same here, but sign doesn't change
            direction_row, direction_column = direction_column, direction_row
            update_seen_and_queue((row, column, direction_row, direction_column), seen, queue)
        else:
            for direction_row, direction_column in [(1, 0), (-1, 0)] if char == "|" else [(0, 1), (0, -1)]:
                update_seen_and_queue((row, column, direction_row, direction_column), seen, queue)
                
    coords = {(row, column) for (row, column, _, _) in seen}
    return len(coords)


def part_two(grid=grid):
    max_value = 0
    
    for row in range(len(grid)):
        max_value = max(max_value, part_one(grid, row, -1, 0, 1))
        max_value = max(max_value, part_one(grid, row, len(grid[0]), 0, -1))
        
    for column in range(len(grid)):
        max_value = max(max_value, part_one(grid, -1, column, 1, 0))
        max_value = max(max_value, part_one(grid, len(grid), column, -1, 0))
    
    print(max_value)

print(part_one())
part_two()