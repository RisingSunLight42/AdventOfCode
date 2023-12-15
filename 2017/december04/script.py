with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


def part_one(lines=lines):
    total = 0
    for line in lines:
        line = line.split(" ")
        total += len(set(line)) == len(line)
    print(total)

def part_two():
    total = 0
    for line in lines:
        line = line.split(" ")
        if len(set(line)) != len(line):
            continue
        is_valid = True
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if "".join(sorted(line[i])) == "".join(sorted(line[j])):
                    is_valid = False
                    break
            if not is_valid:
                break
        total += is_valid
    print(total)

part_one()
part_two()