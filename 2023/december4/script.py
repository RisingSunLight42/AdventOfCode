import re

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

cards_sets = []

for line in lines:
    numbers = line.split(':')[1]
    parts = numbers.split('|')
    cards_sets.append([set(map(int, re.findall(r"\d+", parts[0]))), set(map(int, re.findall(r"\d+", parts[1])))])      


def part_one():
    result = 0
    for winning, numbers in cards_sets:
        winning_results = winning.intersection(numbers)
        number_of_winning_results = len(winning_results)
        if number_of_winning_results == 0:
            continue
        subpoints = 1
        subpoints *= 2**(number_of_winning_results - 1)
        result += subpoints
    print(result)


def part_two():
    cards_number_with_sets = {}
    
    for i in range(len(cards_sets)):
        cards_number_with_sets[i+1] = cards_sets[i]

    number_of_cards = { card: 1 for card in cards_number_with_sets.keys() }

    for index, (winning, numbers) in cards_number_with_sets.items():
        winning_results = winning.intersection(numbers)
        card_under = index + 1
        for i in range(card_under, card_under + len(winning_results)):
            number_of_cards[i] += 1 * number_of_cards[index] # calculate number of duplicates based on the number of cards of the parent

    print(sum(number_of_cards.values()))

part_one()
part_two()