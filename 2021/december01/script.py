depth_measurement_list = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    depth_measurement_list = file.readlines()

# Part one


def part_one():
    measurements_larger_than_previous = 0
    for i in range(1, len(depth_measurement_list)):
        previous_one = int(depth_measurement_list[i - 1].replace("\n", ""))
        actual = int(depth_measurement_list[i].replace("\n", ""))
        measurements_larger_than_previous += previous_one < actual
    print(
        f"The number of measurements larger than the previous one is : {measurements_larger_than_previous}")


def part_two():
    measurements_larger_than_previous = 0
    previous_window_sum = int(depth_measurement_list[0].replace("\n", "")) + int(
        depth_measurement_list[1].replace("\n", "")) + int(depth_measurement_list[2].replace("\n", ""))
    for i in range(3, len(depth_measurement_list)):
        first_one_window = int(depth_measurement_list[i - 2].replace("\n", ""))
        second_one_window = int(
            depth_measurement_list[i - 1].replace("\n", ""))
        third_one_window = int(depth_measurement_list[i].replace("\n", ""))
        window_sum = first_one_window + second_one_window + third_one_window
        measurements_larger_than_previous += previous_window_sum < window_sum
        previous_window_sum = window_sum
    print(
        f"The number of measurements larger than the previous one is : {measurements_larger_than_previous}")


part_two()
