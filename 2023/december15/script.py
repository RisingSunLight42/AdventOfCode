with open("./input.txt", 'r', encoding='utf-8') as file:
    instructions = file.read().split(",")

def hash(string):
    current_value = 0
    for character in string:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256
    return current_value


def part_one():
    print(sum(map(hash, instructions)))


def part_two():
    boxes = [[] for _ in range(256)]
    focals = {}
    for instruc in instructions:
        if "-" in instruc:
            label = instruc[:-1]
            box_index = hash(label)
            if label in boxes[box_index]:
                boxes[box_index].remove(label)
        else:
            label, length = instruc.split("=")
            length = int(length)
            box_index = hash(label)
            if label not in boxes[box_index]:
                boxes[box_index].append(label)
            focals[label] = length
    
    total = 0
    for box_index, box in enumerate(boxes, 1):
        for focal_index, label in enumerate(box, 1):
            total += box_index * focal_index * focals[label]
    print(total)

part_one()
part_two()