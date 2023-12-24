with open("./input.txt", 'r', encoding='utf-8') as file:
    grid = file.read().splitlines()


def search_interesting_points(grid):
    start = (0, grid[0].index("."))
    end = (len(grid) -1, grid[-1].index("."))
    
    points = [start, end]
    
    # search points of interest (where there's more than one path to go)
    # it is used to simplify the graph to draw in the graph only points where multiple
    # path are possible, instead of drawing tons of points where only one path is possible
    # we will, instead, mark the length of the path in the line connecting to points (instead of representing it directly by points)
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "#":
                continue
            neighbors = 0
            for next_row, next_col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))
    return start, end, points
    

def populate_graph(points, part_two=False):
    graph = {point: {} for point in points}
    
    directions =  {
        "^": [(-1, 0)],
        "v": [(1,0)],
        "<": [(0, -1)],
        ">": [(0, 1)],
        ".": [(-1,0), (1,0), (0,-1), (0,1)]
    } if not part_two else {
        "^": [(-1,0), (1,0), (0,-1), (0,1)],
        "v": [(-1,0), (1,0), (0,-1), (0,1)],
        "<": [(-1,0), (1,0), (0,-1), (0,1)],
        ">": [(-1,0), (1,0), (0,-1), (0,1)],
        ".": [(-1,0), (1,0), (0,-1), (0,1)]
    }
    
    for starting_row, starting_col in points:
        stack = [(0, starting_row, starting_col)]
        seen = {(starting_row, starting_col)}
        
        while stack:
            length, row, col = stack.pop()
            
            if length != 0 and (row, col) in points:
                graph[(starting_row, starting_col)][(row, col)] = length
                continue
            
            for dir_row, dir_col in directions[grid[row][col]]:
                next_row = dir_row + row
                next_col = dir_col + col
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) \
                and grid[next_row][next_col] != "#" and (next_row, next_col) not in seen:
                    stack.append((length + 1, next_row, next_col))
                    seen.add((next_row, next_col))
    return graph


def compute_answer(start, end, graph):
    seen = set()
    def search_longest_path(point):
        if point == end:
            return 0
        
        maximum = -float("inf")
        
        seen.add(point)
        for next_point in graph[point]:
            if next_point not in seen:
                maximum = max(maximum, search_longest_path(next_point) + graph[point][next_point])
        seen.remove(point)
        
        return maximum
    print(search_longest_path(start))


def part_one(grid=grid):
    start, end, points = search_interesting_points(grid)
    graph = populate_graph(points)
    compute_answer(start, end, graph)    


def part_two(grid=grid):
    start, end, points = search_interesting_points(grid)
    graph = populate_graph(points, True)
    compute_answer(start, end, graph)  


part_one()
part_two()