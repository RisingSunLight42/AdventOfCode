import re

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Part one


def part_one(red=12, green=13, blue=14):
    total = 0
    for line in lines:
        dict_actual_game = { "red": 0, "blue": 0, "green": 0 }
        game_id = int(re.search(r"\d+", line).group())
        for number_and_cube in re.findall(r'\d+ red|\d+ green|\d+ blue', line):
            [number, color] = number_and_cube.split(" ")
            number = int(number)
            if (dict_actual_game[color] < number):
                dict_actual_game[color] = number
        total += game_id  * (dict_actual_game["red"] <= red and dict_actual_game["green"] <= green and dict_actual_game["blue"] <= blue)
    print(total)
        

# Part two

def part_two():
    total = 0
    for line in lines:
        dict_actual_game = { "red": 0, "blue": 0, "green": 0 }
        for number_and_cube in re.findall(r'\d+ red|\d+ green|\d+ blue', line):
            [number, color] = number_and_cube.strip().split(" ")
            number = int(number)
            if (dict_actual_game[color] < number):
                dict_actual_game[color] = number
        total += dict_actual_game["green"] * dict_actual_game["red"] * dict_actual_game["blue"]
    print(total)
    

part_two()
