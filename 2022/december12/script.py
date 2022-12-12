list_nodes = []
nodes_unvisited = []
dict_nodes_neighbour = {}
start = 0
end = 0

with open("input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        line = []
        for j in range(len(lines[i])):
            if lines[i][j] != '\n':
                if lines[i][j] == "S":
                    start = (i, j)
                    line.append(ord("a") - ord("a"))
                elif lines[i][j] == "E":
                    end = (i, j)
                    line.append(ord("z") - ord("a"))
                else:
                    line.append(ord(lines[i][j]) - ord("a"))
            nodes_unvisited.append((i, j))
        list_nodes.append(line)


for i in range(len(list_nodes)):
    for j in range(len(list_nodes[i])):
        nodes_reachables = []
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if 0 <= i+m < len(list_nodes) and 0 <= j+n < len(list_nodes[i]) and abs(n)+abs(m) == 1:
                    if list_nodes[i+m][j+n] - list_nodes[i][j] <= 1:
                        nodes_reachables.append((i+m, j+n))
        dict_nodes_neighbour[(i, j)] = nodes_reachables


class Nodes:

    def __init__(self, unvisited, visited, starting_node, ending_node, dict_nodes_neighbour) -> None:
        self.unvisited = unvisited
        self.visited = visited
        self.starting_node = starting_node
        self.ending_mode = ending_node
        self.dict_nodes_neighbour = dict_nodes_neighbour
        self.node_distance = {}
        for unvisited_node in self.unvisited:
            self.node_distance[unvisited_node] = 999
        self.node_distance[self.starting_node] = 0

    def visit_node(self, node_currently_visited):
        for node in self.dict_nodes_neighbour[node_currently_visited]:
            if node not in self.visited:
                if self.node_distance[node_currently_visited] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[node_currently_visited] + 1
        self.unvisited.remove(node_currently_visited)
        self.visited.append(node_currently_visited)

    def check_nodes(self):
        while self.ending_mode not in self.visited:
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit_node(current_node)
        return self.node_distance[self.ending_mode]


dijkstra = Nodes(nodes_unvisited, [], start, end, dict_nodes_neighbour)
print(dijkstra.check_nodes())
