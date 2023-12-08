import re
from math import lcm

with open("./input.txt", 'r', encoding='utf-8') as file:
    directions, nodes = file.read().split("\n\n")

nodes = {re.findall(r"[A-Z]{3}", node)[0]: (re.findall(r"[A-Z]{3}", node)[1], re.findall(r"[A-Z]{3}", node)[2]) for node in nodes.split("\n")}

directions_mapping = { "L": 0, "R": 1 }

def part_one(nodes=nodes, directions=directions, start="AAA", end={"ZZZ"}):
    current_node = start
    steps = 0
    while current_node not in end:
        next_direction = directions[steps % len(directions)]
        current_node = nodes[current_node][directions_mapping[next_direction]]
        steps += 1
    return steps


def part_two(nodes=nodes, directions=directions):
    start_nodes = {node for node in nodes if node.endswith("A")}
    end_nodes = {node for node in nodes if node.endswith("Z")}
    step_count = [part_one(nodes, directions, starting_node, end_nodes) for starting_node in start_nodes]
    print(lcm(*step_count))

print(part_one())
part_two()