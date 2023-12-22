from collections import deque

def sort_bricks(bricks):
    return bricks.sort(key=lambda brick: brick[2]) # sort by z ascending


def get_bricks():
    with open("./input.txt", 'r', encoding='utf-8') as file:
        bricks = [list(map(int, line.replace("~", ",").split(","))) for line in file.read().splitlines()]
        sort_bricks(bricks)
        return bricks


def overlaps(brick_a, brick_b):
    # 0 & 3 correspond to x, 1 & 4 to y
    return max(brick_a[0], brick_b[0]) <= min(brick_a[3], brick_b[3]) \
        and max(brick_a[1], brick_b[1]) <= min(brick_a[4], brick_b[4])


def make_bricks_fall(bricks):
    for index, brick in enumerate(bricks):
        max_z_after_drop = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                # check[3] is equal to top z position, so check[3] + 1 is equal to the maximum possible
                # value our brick can drop
                max_z_after_drop = max(max_z_after_drop, check[5] + 1)
        brick[5] -= brick[2] - max_z_after_drop
        brick[2] = max_z_after_drop
    sort_bricks(bricks)


def check_supporting(bricks):
    k_supports_v = {supporter: set() for supporter in range(len(bricks))} # i support everything in the set
    v_supports_k = {supported: set() for supported in range(len(bricks))} # i supported by everything in the set
    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)
    return k_supports_v, v_supports_k


def can_be_desintegrated(bricks, k_supports_v, v_supports_k):
    nb_can_disintegrate = 0
    for i in range(len(bricks)):
        if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
            nb_can_disintegrate += 1
    return nb_can_disintegrate


def part_one():
    bricks = get_bricks()
    make_bricks_fall(bricks)
    k_supports_v, v_supports_k = check_supporting(bricks)
    result = can_be_desintegrated(bricks, k_supports_v, v_supports_k)
    print(result)


def part_two():
    bricks = get_bricks()
    make_bricks_fall(bricks)
    k_supports_v, v_supports_k = check_supporting(bricks)
    
    total = 0
    for i in range(len(bricks)):
        queue = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(queue) # equivalent to a seen set for this problem
        falling.add(i)
        
        while queue:
            j = queue.popleft()
            for k in k_supports_v[j] - falling:
                # with sets, <= is equivalent to check if v_supports_k is a subset (or equivalent) to falling
                if v_supports_k[k] <= falling:
                    queue.append(k)
                    falling.add(k)
        total += len(falling) - 1
    print(total)


part_one()
part_two()