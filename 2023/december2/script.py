import re

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Part one


def part_one(red=12, green=13, blue=14):
    total = 0
    game_passing = []
    for line in lines:
        dict_actual_game = { "red": 0, "blue": 0, "green": 0 }
        game_list = line.split(":")
        game_id = int(game_list[0].split(" ")[1])
        cube_set_string = game_list[1]
        cube_sets = cube_set_string.split(";")
        for cubes in cube_sets:
            number_and_cube = cubes.split(",")
            for number_and_cube in number_and_cube_list:
                [number, color] = number_and_cube.strip().split(" ")
                number = int(number)
                if (dict_actual_game[color] < number):
                    dict_actual_game[color] = number
        if (dict_actual_game["red"] <= red and dict_actual_game["green"] <= green and dict_actual_game["blue"] <= blue):
            game_passing.append(int(game_id))
    
    for game_id in game_passing:
        total += game_id

    print(total)
        

# Part two

def part_two():
    total = 0
    for line in lines:
        dict_actual_game = { "red": 0, "blue": 0, "green": 0 }
        game_list = line.split(":")
        game_id = int(game_list[0].split(" ")[1])
        cube_set_string = game_list[1]
        cube_sets = cube_set_string.split(";")
        for cubes in cube_sets:
            number_and_cube_list = cubes.split(",")
            for number_and_cube in number_and_cube_list:
                [number, color] = number_and_cube.strip().split(" ")
                number = int(number)
                if (dict_actual_game[color] < number):
                    dict_actual_game[color] = number
        total += dict_actual_game["green"] * dict_actual_game["red"] * dict_actual_game["blue"]
    print(total)
    

part_two()

