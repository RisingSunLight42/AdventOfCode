from functools import cache

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = [ line.split(" ") for line in file.read().splitlines()]


springs = [line[0] for line in lines]
numbers = [tuple(map(int, line[1].split(","))) for line in lines]

@cache
def count_possible_arrangements(springs, numbers):
    if springs == "":
        # if there's no more springs, the only case it is valid is when
        # we look to find no more broken springs
        if numbers == ():
            return 1
        return 0

    if numbers == ():
        # If we're looking to find no more springs in numbers
        # but there's broken springs, then it is not valid
        if "#" in springs:
            return 0
        return 1
    
    result = 0
    if springs[0] == '.' or springs[0] == '?':
        # we test the next case
        result += count_possible_arrangements(springs[1:], numbers)
        
    if springs[0] == '#' or springs[0] == '?':
        # if the wanted number of combination if greater than the lenght of the remaining springs, it's incorrect
        # no functionnal springs should be in the range of the number of damaged springs wanted
        # if the number is equal to the length of remaining springs or the next spring (after the sequence) is not a damaged one
        # then it is a valid combination for the number
        if numbers[0] <= len(springs) \
        and "." not in springs[:numbers[0]] \
        and (numbers[0] == len(springs) or springs[numbers[0]] != '#'):
            # we remove the number of damaged springs wanted + 1 for the gap, and the number
            result += count_possible_arrangements(springs[numbers[0] + 1:], numbers[1:])
    return result


def part_one(springs=springs, numbers=numbers):
    total = 0
    for i in range(len(springs)):
        total += count_possible_arrangements(springs[i], numbers[i])
    print(total)


def part_two(springs=springs, numbers=numbers):
    springs = ["?".join([spring] * 5) for spring in springs]
    numbers = [number * 5 for number in numbers]
    total = 0
    for i in range(len(springs)):
        total += count_possible_arrangements(springs[i], numbers[i])
    print(total)


part_one()
part_two()