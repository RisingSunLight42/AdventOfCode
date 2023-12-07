import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    entries = [int(line) for line in file.read().splitlines()]


def part_one():
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            if entries[i]+entries[j]==2020:
                print(entries[i] * entries[j])
                return


def part_two():
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            for k in range(i+2, len(entries)):
                if entries[i]+entries[j]+entries[k]==2020:
                    print(entries[i] * entries[j] * entries[k])
                    return

part_one()
part_two()