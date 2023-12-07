import re
from collections import Counter

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


def convertion(character, part_one):
    if character.isnumeric(): return int(character)
    return { "A": 14, "K": 13, "Q": 12, "J": 11 if part_one else 1, "T": 10 }[character]


def convert_card(hand, part_one=True):
    return tuple(convertion(card, part_one) for card in hand)


def get_highest_corresponding_value(highest, counter):
    if highest == 5: return 6
    elif highest == 4: return 5
    elif len(counter) == 2: return 4 # For full house (cause in fact, there's two different type of cards in hand)
    elif highest == 3: return 3
    elif len(counter) == 3: return 2 # For two pairs because there's 2 type of cards for pairs + 1 remaining card
    elif highest == 2: return 1
    else: return 0
 

class Hand:
    def __init__(self, hand, bid, part_one=True):
        self.bid = bid
        self.cards = hand
        self.type = self.getType(part_one)

    def getType(self, part_one):
        counter = Counter(self.cards)
        highest = max(counter.values())
        if not part_one:
            # Permet de récupérer le nombre de cartes Joker puis de récupérer le nombre
            # d'autres cartes le plus élevé pour avoir l'effet du joker
            wilds = counter[1]
            del counter[1]
            highest = wilds
            if counter: highest += max(counter.values())
        return get_highest_corresponding_value(highest, counter)

    def __lt__(self, other):
        return self.type < other.type or (self.type == other.type and self.cards < other.cards)

    def __repr__(self):
        return str(self.cards)+f" bid : {self.bid}"
   

def part_one():
    hands = [[convert_card(re.findall(r"\w+ ", line)[0].strip()),int(re.findall(r" \d+", line)[0].strip())] for line in lines]
    list_matching_values = [Hand(hand, bid) for hand, bid in hands]
    list_matching_values.sort()
    total_winnings = 0
    for i, hand in enumerate(list_matching_values):
        total_winnings += (i+1)*hand.bid
    print(total_winnings)


def part_two():
    hands = [[convert_card(re.findall(r"\w+ ", line)[0].strip(), False),int(re.findall(r" \d+", line)[0].strip())] for line in lines]
    list_matching_values = [Hand(hand, bid, False) for hand, bid in hands]
    list_matching_values.sort()
    total_winnings = 0
    for i, hand in enumerate(list_matching_values):
        total_winnings += (i+1)*hand.bid
    print(total_winnings)

part_one()
part_two()