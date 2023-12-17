from heapq import heappush, heappop

with open("./input.txt", 'r', encoding='utf-8') as file:
    grid = [list(map(int, line.strip())) for line in file]


def part_one(grid=grid):
    seen = set()
    priority_queue = [(0, 0, 0, 0, 0, 0)] # heat lost, coordinates (row/col), direction (row/col), number of steps in the direction
    while priority_queue:
        heat_loss, row, col, dir_row, dir_col, step_same_dir = heappop(priority_queue)
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            # it works thanks to priority queue making the pop with the lesser heat_loss in the queue
            print(heat_loss)
            break
        
        if (row, col, dir_row, dir_col, step_same_dir) in seen:
            # heat loss not included to avoid loops, since heatloss will increase at each step
            continue
        seen.add((row, col, dir_row, dir_col, step_same_dir))
        
        # try to continue in the same direction
        if step_same_dir < 3 and (dir_row, dir_col) != (0 ,0):
            next_row = row + dir_row
            next_col = col + dir_col
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                new_movement = (heat_loss + grid[next_row][next_col], next_row, next_col, dir_row, dir_col, step_same_dir + 1)
                heappush(priority_queue, new_movement)

        # test others direction
        for next_dir_row, next_dir_col in [(0, 1), (1,0), (0,-1), (-1,0)]:
            # we don't want to test the same direction and the reverse one, since it is useless
            if (next_dir_row, next_dir_col) == (dir_row, dir_col) \
            or (next_dir_row, next_dir_col) == (-dir_row, -dir_col):
                continue
            next_row = row + next_dir_row
            next_col = col + next_dir_col
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                new_movement = (heat_loss + grid[next_row][next_col], next_row, next_col, next_dir_row, next_dir_col, 1)
                heappush(priority_queue, new_movement)

def part_two():
    seen = set()
    priority_queue = [(0, 0, 0, 0, 0, 0)] #heat lost, coordinates (row/col), direction (row/col), number of steps in the direction
    while priority_queue:
        heat_loss, row, col, dir_row, dir_col, step_same_dir = heappop(priority_queue)
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1 and step_same_dir >= 4:
            print(heat_loss)
            break
        
        if (row, col, dir_row, dir_col, step_same_dir) in seen:
            # heat loss not included to avoid loops, since heatloss will increase at each step
            continue
        seen.add((row, col, dir_row, dir_col, step_same_dir))
        
        # try to continue in the same direction
        if step_same_dir < 10 and (dir_row, dir_col) != (0 ,0):
            next_row = row + dir_row
            next_col = col + dir_col
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                new_movement = (heat_loss + grid[next_row][next_col], next_row, next_col, dir_row, dir_col, step_same_dir + 1)
                heappush(priority_queue, new_movement)

        if step_same_dir < 4 and (dir_col, dir_row) != (0, 0): # second test is to handle the starting state
            continue

        # test others direction
        for next_dir_row, next_dir_col in [(0, 1), (1,0), (0,-1), (-1,0)]:
            # we don't want to test the same direction and the reverse one, since it is useless
            if (next_dir_row, next_dir_col) == (dir_row, dir_col) \
            or (next_dir_row, next_dir_col) == (-dir_row, -dir_col):
                continue
            next_row = row + next_dir_row
            next_col = col + next_dir_col
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                new_movement = (heat_loss + grid[next_row][next_col], next_row, next_col, next_dir_row, next_dir_col, 1)
                heappush(priority_queue, new_movement)

part_one()
part_two()