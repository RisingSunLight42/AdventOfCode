with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read()


def part_one():
    print(sum([int(lines[i]) if lines[i] == lines[(i + 1) % len(lines)] else 0 for i in range(len(lines))]))


def part_two():
    print(sum([int(lines[i]) if lines[i] == lines[(i + (len(lines) // 2)) % len(lines)] else 0 for i in range(len(lines))]))

part_one()
part_two()