chars = ""

with open("./input.txt", 'r', encoding='utf-8') as file:
    chars = file.read()


def all(size_substr: int):
    for i in range(size_substr, len(chars), 1):
        start_of_packet = chars[i-size_substr:i]
        if (len(set(start_of_packet))) == len(start_of_packet):
            return i


print(all(4))
print(all(14))
