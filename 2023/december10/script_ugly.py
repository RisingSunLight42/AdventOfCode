import re
import sys

sys.setrecursionlimit(100000)

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

class Direction:
    NORTH   = (-1,0)
    SOUTH   = (1,0)
    EAST    = (0,1)
    WEST    = (0,-1)

dict_neightbors = {
    '|': (Direction.NORTH, Direction.SOUTH),
    '-': (Direction.EAST, Direction.WEST),
    'L': (Direction.NORTH, Direction.EAST),
    'J': (Direction.NORTH, Direction.WEST),
    '7': (Direction.SOUTH, Direction.WEST),
    'F': (Direction.SOUTH, Direction.EAST),
    '.': (),
    'S': (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST) 
}

def find_start():
    for index, line in enumerate(lines):
        if 'S' in line:
            return (index, line.index('S'))
        

def part_one(loop=set(),lines=lines, possibly_inside=set()):
    start = find_start()
    while True:
        loop.add(start)
        yS, xS = start
        for neighbor in dict_neightbors[lines[yS][xS]]:
            yN, xN = neighbor
            navY, navX = (yS + yN, xS + xN)
            # Check if out of bound
            if not (0 <= navY < len(lines) and 0 <= navX < len(lines[0])):
                continue
            # Check if we're not going back on our steps
            if lines[navY][navX] == 'S' and len(loop) > 2:
                print(len(loop)//2) # Since it's a cycle, the farthest point is at the length divided by 2
                return loop, possibly_inside
            # Check if it is ground
            if lines[navY][navX] == '.':
                continue
            if (navY, navX) in loop:
                continue
            # Check if the symbol is correctly oriented
            if (-1*yN, -1*xN) not in dict_neightbors[lines[navY][navX]]:
                continue
            determine_possible_inside(possibly_inside, (yN, xN), navY, navX)
            start = (navY, navX)
            break


def is_inside(inside_val, loop, inside):
    inside.add(inside_val)
    yI, xI = inside_val
    for neighbor in dict_neightbors['S']:
        yN, xN = neighbor
        navY, navX = (yI+yN, xI+xN)
        if not (-1 <= navY < len(lines)+1 and -1 <= navX < len(lines[0])+1):
            continue
        if (navY, navX) not in loop and (navY, navX) not in inside:
            is_inside((navY, navX), loop, inside)


def determine_possible_inside(possibly_inside, neighbor, navY, navX):
    match neighbor:
        case Direction.NORTH:
            possibly_inside.add((navY+1, navX+1))
            possibly_inside.add((navY, navX+1))
        case Direction.EAST:
            possibly_inside.add((navY+1, navX-1))
            possibly_inside.add((navY+1, navX))
        case Direction.SOUTH:
            possibly_inside.add((navY-1, navX-1))
            possibly_inside.add((navY, navX-1))
        case Direction.WEST:
            possibly_inside.add((navY-1, navX+1))
            possibly_inside.add((navY-1, navX))

def part_two():
    loop, inside = part_one()
    inside = inside.difference(loop) # Remove parts of the loop (they're not counted as 'inside')
    for inside_val in inside.copy(): # can't mutate a set while it is looped
        is_inside(inside_val, loop, inside)
    print(len(inside))

# part_one()
part_two()