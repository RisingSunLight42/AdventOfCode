import re

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

keypad = [["1","2","3"], ["4","5","6"], ["7","8","9"]]

def part_one():
    numpad = ""
    x = 1
    y = 1
    for line in lines:
        for mov in line:
            y += 1 if mov == "D" else -1 if mov == "U" else 0
            x += 1 if mov == "R" else -1 if mov == "L" else 0
            x = 0 if x < 0 else 2 if x > 2 else x
            y = 0 if y < 0 else 2 if y > 2 else y
        numpad += keypad[y][x]
    print(numpad)

weird_keypad = [["-1"   , "-1"  , "1"   , "-1"  , "-1"],
                ["-1"   , "2"   , "3"   , "4"   , "-1"],
                ["5"    , "6"   , "7"   , "8"   , "9" ],
                ["-1"   , "A"   , "B"   , "C"   , "-1"],
                ["-1"   , "-1"  , "D"   , "-1"  , "-1"]]

def part_two():
    numpad = ""
    x = 0
    y = 2
    for line in lines:
        for mov in line:
            old_y = y
            old_x = x
            y += 1 if mov == "D" else -1 if mov == "U" else 0
            x += 1 if mov == "R" else -1 if mov == "L" else 0
            x = 0 if x < 0 else 4 if x > 4 else x
            y = 0 if y < 0 else 4 if y > 4 else y
            if weird_keypad[y][x] == "-1":
                y, x = old_y, old_x
        numpad += weird_keypad[y][x]
    print(numpad)

part_one()
part_two()