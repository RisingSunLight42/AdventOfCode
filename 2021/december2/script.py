orders_list = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    orders_list = file.readlines()


def first_part():
    depth = 0
    horizontal = 0
    for element in orders_list:
        [order, howmuch] = element.split(" ")
        if order == "up":
            depth -= int(howmuch)
        elif order == "down":
            depth += int(howmuch)
        elif order == "forward":
            horizontal += int(howmuch)
    print(depth, horizontal, depth*horizontal)


def second_part():
    depth = 0
    horizontal = 0
    aim = 0
    for element in orders_list:
        [order, howmuch] = element.split(" ")
        if order == "up":
            aim -= int(howmuch)
        elif order == "down":
            aim += int(howmuch)
        elif order == "forward":
            horizontal += int(howmuch)
            depth += (aim * int(howmuch))
    print(aim)
    print(depth, horizontal, depth*horizontal)


second_part()
