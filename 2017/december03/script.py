from collections import defaultdict


def part_one(target):
	grid = {}
	pos = [0, 0]
	number = 1
	grid[(0,0)] = number
	# right 1, up 1, left 2, down 2, right 3, up 3...
	counter = 1
	# 1: right, 2: up, 3: left, 4: down, 5: right...
	direction = 1
	while True:
		for times in range(counter):
			number += 1
			if direction % 4 == 1: pos[1] += 1
			elif direction % 4 == 2: pos[0] -= 1
			elif direction % 4 == 3: pos[1] -= 1
			elif direction % 4 == 0: pos[0] += 1

			grid[(pos[0], pos[1])] = number
			if number == target:
				return abs(pos[0]) + abs(pos[1])

		if direction % 2 == 0: counter += 1
		direction += 1


def getvalue(grid, pos):
	return  grid[(pos[0]+1, pos[1])] +\
		    grid[(pos[0]-1, pos[1])] +\
			grid[(pos[0], pos[1]+1)] +\
			grid[(pos[0], pos[1]-1)] +\
			grid[(pos[0]+1, pos[1]+1)] +\
			grid[(pos[0]+1, pos[1]-1)] +\
			grid[(pos[0]-1, pos[1]+1)] +\
			grid[(pos[0]-1, pos[1]-1)]


def part_two(target):
	grid = defaultdict(int)
	pos = [0, 0]
	grid[(0, 0)] = 1
	# right 1, up 1, left 2, down 2, right 3, up 3...
	counter = 1
	# 1: right, 2: up, 3: left, 4: down, 5: right...
	direction = 1
	while True:
		for times in range(counter):
			if direction % 4 == 1: pos[1] += 1
			elif direction % 4 == 2: pos[0] -= 1
			elif direction % 4 == 3: pos[1] -= 1
			elif direction % 4 == 0: pos[0] += 1

			if getvalue(grid, pos) > target: return getvalue(grid, pos)
			grid[(pos[0],pos[1])] = getvalue(grid, pos)	

		if direction % 2 == 0: counter += 1
		direction += 1

input_value = 347991
print("Part 1:", part_one(input_value))
print("Part 2:", part_two(input_value))