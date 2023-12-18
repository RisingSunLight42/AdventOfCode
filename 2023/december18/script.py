with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

# use https://en.wikipedia.org/wiki/Shoelace_formula and https://en.wikipedia.org/wiki/Pick%27s_theorem

dict_direction = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

def part_one():
    points = [(0,0)]
    
    boundary_points = 0
    
    for line in lines:
        direction, number, _ = line.split(" ")
        direction_row, direction_col = dict_direction[direction]
        number = int(number)
        boundary_points += number
        row, col = points[-1]
        points.append((row + direction_row * number, col + direction_col * number))
        
    # Shoelace formula SUM Xi(Yi+1 - Yi-1)
    area = sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))
    area = abs(area) // 2
    
    interior_points = area - boundary_points // 2 + 1 # Pick's theorem
    print(interior_points + boundary_points)


def part_two():
    points = [(0,0)]
    
    boundary_points = 0
    
    for line in lines:
        _, _, bad_value = line.split(" ")
        bad_value = bad_value[2:-1]
        direction = "RDLU"[int(bad_value[-1])]
        direction_row, direction_col = dict_direction[direction]
        number = int(bad_value[:-1], 16)
        boundary_points += number
        row, col = points[-1]
        points.append((row + direction_row * number, col + direction_col * number))
        
    # Shoelace formula SUM Xi(Yi+1 - Yi-1)
    area = sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))
    area = abs(area) // 2
    
    interior_points = area - boundary_points // 2 + 1
    print(interior_points + boundary_points)

part_one()
part_two()