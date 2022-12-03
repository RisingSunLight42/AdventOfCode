import string

first_half = []
second_half = []
all = []

with open("./input.txt", 'r', encoding='utf-8') as file:
    for element in file.readlines():
        element = element.replace("\n", "")
        all.append(element)
        first_half.append(element[:len(element)//2])
        second_half.append(element[len(element)//2:])


def first_part():
    priorities_sum = 0
    for i in range(len(first_half)):
        for j in range(len(first_half[i])):
            if first_half[i][j] in second_half[i]:
                if first_half[i][j].isupper():
                    priorities_sum += string.ascii_lowercase.index(
                        first_half[i][j].lower()) + 27
                else:
                    priorities_sum += string.ascii_lowercase.index(
                        first_half[i][j]) + 1
                break
    print(priorities_sum)


def second_part():
    priorities_sum = 0
    for i in range(2, len(all), 3):
        for j in range(len(all[i - 2])):
            if all[i - 2][j] in all[i - 1] and all[i - 2][j] in all[i]:
                if all[i - 2][j].isupper():
                    priorities_sum += string.ascii_lowercase.index(
                        all[i - 2][j].lower()) + 27
                else:
                    priorities_sum += string.ascii_lowercase.index(
                        all[i - 2][j]) + 1
                break
    print(priorities_sum)


second_part()
