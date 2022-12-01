elf_calories_list = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    elf_calories_list = file.readlines()

# Part one


def part_one():
    max_calories = 0
    calories_sum = 0
    for calories in elf_calories_list:
        if calories == '\n':
            if calories_sum > max_calories:
                max_calories = calories_sum
            calories_sum = 0
        else:
            calories = calories.replace("\n", "")
            calories_sum += int(calories)
    print(f"Max sum of calories carried by an elf is : {max_calories}")

# Part two


def part_two():
    cal_sum = []
    calories_sum = 0
    for calories in elf_calories_list:
        if calories == '\n':
            cal_sum.append(calories_sum)
            calories_sum = 0
        else:
            calories = calories.replace("\n", "")
            calories_sum += int(calories)
    top_three = sorted(cal_sum, reverse=True)[:3]
    print(f"Top three is : {top_three}")
    print(f"The sum of the top three is : {sum(top_three)}")


part_two()
