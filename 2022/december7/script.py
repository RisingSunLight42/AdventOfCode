path = []
dict_tree = {}

with open("./input.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        if "$ cd .." in line:
            del path[-1]
        elif "$ cd" in line:
            path.append(line.split("cd ")[1])
        if (line[0] != '$'):
            temp_dict = dict_tree
            for i in range(len(path)):
                if (path[i] not in temp_dict):
                    temp_dict[path[i]] = {}
                temp_dict = temp_dict[path[i]]
            if "dir" in line:
                temp_dict[line.split(" ")[1]] = {}
            else:
                splitted_line = line.split(" ")
                temp_dict[f"file {splitted_line[1]}"] = int(splitted_line[0])


def recursive_files_part_one(dict_tree: dict, file_list: list):
    dir_sum = 0
    for key in dict_tree.keys():
        if ("file" in key):
            dir_sum += dict_tree[key]
        else:
            dir_sum += recursive_files_part_one(dict_tree[key], file_list)
    if (dir_sum <= 100000):
        file_list.append(dir_sum)
    return dir_sum


def part_one():
    file_size_list = []
    recursive_files_part_one(dict_tree, file_size_list)
    print(sum(file_size_list))


def recursive_files_part_two(dict_tree: dict, space_needed, dir_to_delete_size: list):
    dir_sum = 0
    for key in dict_tree.keys():
        if ("file" in key):
            dir_sum += dict_tree[key]
        else:
            dir_sum += recursive_files_part_two(
                dict_tree[key], space_needed, dir_to_delete_size)
    if (space_needed <= dir_sum):
        if (dir_to_delete_size[0] != 0):
            if ((dir_sum < dir_to_delete_size[0])):
                dir_to_delete_size[0] = dir_sum
        else:
            dir_to_delete_size[0] = dir_sum
    return dir_sum


def part_two():
    file_size_list = []
    size_used = recursive_files_part_one(dict_tree, file_size_list)
    size_available = 70000000 - size_used
    dir_to_delete_size = [0]
    recursive_files_part_two(dict_tree, 30000000 -
                             size_available, dir_to_delete_size)
    print(dir_to_delete_size[0])


part_two()
