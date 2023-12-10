import re
from collections import Counter

with open("./input.txt", 'r', encoding='utf-8') as file:
    rooms = [ [re.sub(r"-\d+",'',line[0]), int(re.findall(r"\d+",line[0])[0]), line[1][:-1]]for line in [line.split("[") for line in file.read().splitlines()]]

# too high
def part_one():
    total = 0
    passing_element = []
    for room in rooms:
        encrypt, sector, checksum = room
        counter = Counter(encrypt)
        counter = counter.most_common()
        counter = list(filter(lambda a: a[0] in checksum, counter))
        if len(counter) < 5:
            continue
        char_check = ''
        for letter, number in list(sorted(counter, key=lambda a: (-a[1], a[0]))):
            char_check += letter
        if char_check == checksum:
            passing_element.append(encrypt)
            total += sector
    print(total)



def part_two():
    total = 0
    passing_element = []
    for room in rooms:
        encrypt, sector, checksum = room
        counter = Counter(encrypt)
        counter = counter.most_common()
        counter = list(filter(lambda a: a[0] in checksum, counter))
        if len(counter) < 5:
            continue
        char_check = ''
        for letter, number in list(sorted(counter, key=lambda a: (-a[1], a[0]))):
            char_check += letter
        if char_check == checksum:
            passing_element.append([encrypt, sector])
            total += sector
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for element, sector in passing_element:
        string = ''
        for character in element:
            if character == '-':
                string += ' '
            else:
                string += alphabet[(alphabet.index(character) + sector) % 26]
        if 'pole' in string:
            print(sector)
            break

part_one()
part_two()