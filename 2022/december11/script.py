from math import prod


class Monkey:

    def __init__(self, item_list, operation_list, test, ifTrue, ifFalse) -> None:
        self.items = []
        self.operation = []
        self.test = 0
        self.ifTrue = 0
        self.ifFalse = 0
        self.itemInspected = 0
        self.set_items(item_list)
        self.set_operation(operation_list)
        self.set_test(test)
        self.set_ifTrue(ifTrue)
        self.set_ifFalse(ifFalse)

    def __str__(self) -> str:
        print(self.items)
        print(self.operation)
        return f"Le singe a inspecté {self.itemInspected} objets. Le test est {self.test}, avec renvoi vers le singe {self.ifTrue} si vrai, {self.ifFalse} si faux."

    def set_items(self, item_list):
        for item in item_list:
            self.items.append(int(item))

    def set_operation(self, operation_list):
        self.operation.append(operation_list[0])
        if operation_list[1] == 'old':
            self.operation.append(operation_list[1])
        else:
            self.operation.append(int(operation_list[1]))

    def set_test(self, test):
        self.test = int(test)

    def set_ifTrue(self, ifTrue):
        self.ifTrue = int(ifTrue)

    def set_ifFalse(self, ifFalse):
        self.ifFalse = int(ifFalse)

    def get_itemInspected(self):
        return self.itemInspected

    def get_test(self):
        return self.test

    def add_item(self, item):
        self.items.append(item)

    def do_operation(self, item_pos):
        operation = self.operation[1]
        if self.operation[1] == 'old':
            operation = self.items[item_pos]
        match self.operation[0]:
            case '*':
                self.items[item_pos] *= operation
            case '/':
                self.items[item_pos] /= operation
            case '+':
                self.items[item_pos] += operation
            case '-':
                self.items[item_pos] -= operation

    def do_relief(self, item_pos, relief_number):
        if relief_number == 3:
            self.items[item_pos] = self.items[item_pos] // relief_number
        else:
            self.items[item_pos] = self.items[item_pos] % relief_number

    def do_test(self, item_pos: int):
        item = self.items[item_pos]
        if item % self.test == 0:
            return (item, self.ifTrue)
        return (item, self.ifFalse)

    def do_round(self, monkey_list, relief_number):
        for item_pos in range(len(self.items)):
            self.itemInspected += 1
            self.do_operation(item_pos)
            self.do_relief(item_pos, relief_number)
            test_result = self.do_test(item_pos)
            monkey_list[test_result[1]].add_item(test_result[0])
        self.items = []


def do_file():
    monkey_list = []
    with open("input.txt", 'r', encoding='utf-8') as file:
        item_list = None
        operation_list = None
        test = None
        ifTrue = None
        ifFalse = None
        for line in file.readlines():
            line = line.replace("\n", "")
            line = line.replace(":", "")
            if "Starting items" in line:
                line = line.replace("  Starting items ", "")
                item_list = line.split(", ")
            elif "Operation" in line:
                line = line.split(" ")
                operation_list = [line[-2], line[-1]]
            elif "Test" in line:
                test = line.split(" ")[-1]
            elif "If true" in line:
                ifTrue = line.split(" ")[-1]
            elif "If false" in line:
                ifFalse = line.split(" ")[-1]
            elif line == '':
                monkey = Monkey(item_list, operation_list,
                                test, ifTrue, ifFalse)
                monkey_list.append(monkey)
    return monkey_list


def execute(round, relief_number, monkey_list):
    for i in range(round):
        for monkey in monkey_list:
            monkey.do_round(monkey_list, relief_number)
    list_inspected = []
    for monkey in monkey_list:
        list_inspected.append(monkey.get_itemInspected())
    max1 = max(list_inspected)
    list_inspected.remove(max1)
    max2 = max(list_inspected)
    print(max1 * max2)


monkey_list = do_file()
factor = []
for monkey in monkey_list:
    factor.append(monkey.get_test())
cap = prod(factor)
execute(10000, cap, monkey_list)
