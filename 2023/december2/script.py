import re

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Part one


def part_one():
    total = 0
    fine_list = []
    for line in lines:
        dict_actual_game = { "red": 0, "blue": 0, "green": 0 }
        game_list = line.split(":")
        game_id = int(game_list[0].split(" ")[1])
        colors = game_list[1]
        tries = colors.split(";")
        for trying in tries:
            list_of_colors = trying.split(",")
            for color_number in list_of_colors:
                [number, color] = color_number.strip().split(" ")
                number = int(number)
                if (dict_actual_game[color] < number):
                    dict_actual_game[color] = number
        if (dict_actual_game["red"] <= 12 and dict_actual_game["green"] <= 13 and dict_actual_game["blue"] <= 14):
            fine_list.append(int(game_id))
    
    for element in fine_list:
        total += element

    print(total)
        

# Part two

def part_two():
    total = 0
    fine_list = []
    for line in lines:
        dict_actual_game = { "red": 0, "blue": 0, "green": 0 }
        game_list = line.split(":")
        game_id = int(game_list[0].split(" ")[1])
        colors = game_list[1]
        tries = colors.split(";")
        for trying in tries:
            list_of_colors = trying.split(",")
            for color_number in list_of_colors:
                [number, color] = color_number.strip().split(" ")
                number = int(number)
                if (dict_actual_game[color] < number):
                    dict_actual_game[color] = number
        fine_list.append(dict_actual_game["green"] * dict_actual_game["red"] * dict_actual_game["blue"])
    
    for element in fine_list:
        total += element

    print(total)
    

part_two()

