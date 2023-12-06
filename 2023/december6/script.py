import re
from math import floor, ceil, sqrt

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

def computeSolution(time_with_distance):
    solutions = [((time-sqrt(time*time-4*distance))/2, (time+sqrt(time*time-4*distance))/2) for time, distance in time_with_distance.items()]
    mult = 1
    for mini, maxi in solutions:
        mini = mini+1 if mini.is_integer() else ceil(mini)
        maxi = maxi-1 if maxi.is_integer() else floor(maxi)
        mult *= maxi-mini+1
    print(mult)

def part_one(lines=lines):
    time_with_distance = dict(zip(map(int, re.findall("\d+", lines[0])), map(int, re.findall("\d+", lines[1]))))
    computeSolution(time_with_distance)


def part_two(lines=lines):
    time_with_distance = dict(zip(map(int, re.findall("\d+", lines[0].replace(" ", ""))), map(int, re.findall("\d+", lines[1].replace(" ", "")))))
    computeSolution(time_with_distance)

part_one()
    