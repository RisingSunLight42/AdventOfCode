import re
from numpy import diff

with open("./input.txt", 'r', encoding='utf-8') as file:
    sequences = [list(map(int, re.findall(r"-?\d+", line))) for line in file.read().splitlines()]


def part_one(forward=True):
    sequences_diff = {i: [sequences[i]] for i in range(len(sequences))}
    for key in sequences_diff.keys():
        while any(sequences_diff[key][-1]):
            sequences_diff[key].append(list(diff(sequences_diff[key][-1])))
    
    total = 0
    for key in sequences_diff.keys():
        for i in range(len(sequences_diff[key]) -1, 0, -1):
            sequences_diff[key][i-1].append(sequences_diff[key][i-1][-1] + sequences_diff[key][i][-1])
            if i-1 == 0:
                total += sequences_diff[key][i-1][-1]
    print(total)


def part_two():
    sequences_diff = {i: [sequences[i]] for i in range(len(sequences))}
    for key in sequences_diff.keys():
        while any(sequences_diff[key][-1]):
            sequences_diff[key].append(list(diff(sequences_diff[key][-1])))
    
    total = 0
    for key in sequences_diff.keys():
        for i in range(len(sequences_diff[key]) -1, 0, -1):
            sequences_diff[key][i-1].insert(0, sequences_diff[key][i-1][0] - sequences_diff[key][i][0])
            if i-1 == 0:
                total += sequences_diff[key][i-1][0]
    print(total)

part_one()
part_two()