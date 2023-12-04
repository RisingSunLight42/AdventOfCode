import re
import time
from functools import cache

lines = []
with open("./input.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

flow = {re.search(r"[A-Z]{2}", line).group(): int(re.search(r"\d+", line).group()) for line in lines}
tunnels = {re.search(r"[A-Z]{2}", line).group(): re.findall(r"[A-Z]{2}", line)[1:] for line in lines}

# frozenset are mandatory due to the fact that cache can only work with hashable objects
# that's why there a weird convertion frozenset -> set -> frozenset (because we need to store the opened valves)
# the cache decorator avoid a lot of calls already done
@cache
def part_one(current, time, opened):
    if time == 0:
        return 0

    max_flow = max(part_one(next_valve, time -1, opened) for next_valve in tunnels[current])
    
    if flow[current] > 0 and current not in opened:
        opened_not_frozen = set(opened)
        opened_not_frozen.add(current)
        max_flow = max(max_flow, (time - 1) * flow[current] + part_one(current, time - 1, frozenset(opened_not_frozen)))
    return max_flow

@cache
def part_two(current, time, opened, is_human=False):
    if time == 0:
        if is_human:
            return part_two("AA", 26, opened)
        return 0

    max_flow = max(part_two(next_valve, time -1, opened, is_human) for next_valve in tunnels[current])
    
    if flow[current] > 0 and current not in opened:
        opened_not_frozen = set(opened)
        opened_not_frozen.add(current)
        max_flow = max(max_flow, (time - 1) * flow[current] + part_two(current, time - 1, frozenset(opened_not_frozen), is_human))
    return max_flow

start = time.perf_counter()
print(part_two("AA", 26, frozenset(), True))
print(time.perf_counter() - start)