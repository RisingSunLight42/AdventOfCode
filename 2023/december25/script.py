# See to understand why this script works https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm
from collections import defaultdict
import networkx as nx

with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()


def part_one():
    graph = defaultdict(dict)

    for line in lines:
        src, destinations = line.split(': ')
        for dest in destinations.split():
            graph[src][dest] = {'weight': 1}
        
    computed_graph = nx.from_dict_of_dicts(graph)
    result = next(nx.community.girvan_newman(computed_graph))
    print(len(result[0]) * len(result[1]))


def part_two():
    print("Merry Christmas ! :D")


part_one()
part_two()