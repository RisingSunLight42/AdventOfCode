from hashlib import md5

input_value = "ffykfhsq"

def part_one(input_value=input_value):
    nb = 0
    str_result = ''
    for i in range(100_000_000_000):
        hashedValue = md5((input_value + str(i)).encode()).hexdigest()
        if hashedValue[:5] == '00000':
            str_result += hashedValue[5]
            nb += 1
            if nb == 8:
                break
    print(str_result)


def part_two():
    nb = 0
    str_result = [-1,-1,-1,-1,-1,-1,-1,-1]
    for i in range(100_000_000_000_000):
        hashedValue = md5((input_value + str(i)).encode()).hexdigest()
        if hashedValue[:5] == '00000':
            if hashedValue[5].isdigit() and int(hashedValue[5]) < 8 and str_result[int(hashedValue[5])] == -1:
                str_result[int(hashedValue[5])] = hashedValue[6]
                nb += 1
                if nb == 8:
                    break
    print(''.join(str_result))

#part_one()
part_two()