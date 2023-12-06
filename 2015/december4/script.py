from hashlib import md5

input_value = "iwrupvqb"

def part_one(input_value=input_value):
    for i in range(1_000_000):
        hashedValue = md5((input_value + str(i)).encode()).hexdigest()
        if hashedValue[:5] == '00000':
            print(i)
            break

def part_two(input_value=input_value):
    for i in range(10_000_000):
        hashedValue = md5((input_value + str(i)).encode("utf-8")).hexdigest()
        if hashedValue[:6] == '000000':
            print(i)
            break
        
part_one()
part_two()