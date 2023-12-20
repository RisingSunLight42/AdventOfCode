from collections import deque
from math import lcm
from ModuleClass import Module


with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = [line.split(" -> ") for line in file.read().splitlines()]


def generate_module_and_broadcast():
    modules = {}
    broadcast_targets = []
    for left, right in lines:
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type_module = left[0]
            name = left[1:]
            modules[name] = Module(name, type_module, outputs)
    return modules, broadcast_targets


def initialize_memory(modules):
    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "low"


def update_queue(queue, module):
    for x in module.outputs:
        queue.append((module.name, x, module.outgoing))


def part_one():
    modules, broadcast_targets = generate_module_and_broadcast()
    initialize_memory(modules)
    count_pulse = { "low": 0, "high": 0}
    for _ in range(1000):
        count_pulse["low"] += 1
        
        # origin, target, pulse
        queue = deque([("broadcaster", x, "low") for x in broadcast_targets])
        
        while queue:
            origin, target, pulse = queue.popleft()
            count_pulse[pulse] += 1
            
            if target not in modules: # case target is the end
                continue
            
            module = modules[target]
            
            if module.type == "%":
                if pulse == "low":
                    module.switchMemory()
                    update_queue(queue, module)
            else:
                module.updateMemory(origin, pulse)
                update_queue(queue, module)
    print(count_pulse["low"] * count_pulse["high"])


# assumption, rx is feed by a conjonction module. All modules the feed the module feeding
# rx will produce a low pulse every single button press, except at regular interval, where
# it will produce a high instead
def part_two():
    modules, broadcast_targets = generate_module_and_broadcast()
    initialize_memory(modules)
    # (blabla,) authorize the unpack for only one value
    (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]
    
    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}
    
    presses = 0
    while True:
        presses += 1
        # origin, target, pulse
        queue = deque([("broadcaster", x, "low") for x in broadcast_targets])
        
        while queue:
            origin, target, pulse = queue.popleft()
            
            if target not in modules:
                continue
            
            module = modules[target]
            if module.name == feed and pulse == "high":
                seen[origin] += 1
                
                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lengths[origin]
                    
                """assertion to check if cycle exist or not if all(x > 10 for x in seen.values()):
                    exit(0)"""
                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = lcm(x, cycle_length)
                    print(x)
                    return
            
            if module.type == "%":
                if pulse == "low":
                    module.switchMemory()
                    update_queue(queue, module)
            else:
                module.updateMemory(origin, pulse)
                update_queue(queue, module)


part_one()
part_two()