import copy

with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
instructions_raw = [[int(k) for k in x] for x in instructions_raw]


def traverse(y, x, found_num):
    if found_num == 9:
        return [[y, x]]
    global instructions_raw
    results = []
    next_up = [y - 1, x]
    next_down = [y + 1, x]
    next_right = [y, x + 1]
    next_left = [y, x - 1]
    if y - 1 >= 0 and instructions_raw[next_up[0]][next_up[1]] == (found_num + 1):
        results.extend(traverse(next_up[0], next_up[1], found_num + 1))
    if y + 1 <= (len(instructions_raw) - 1) and instructions_raw[next_down[0]][
        next_down[1]
    ] == (found_num + 1):
        results.extend(traverse(next_down[0], next_down[1], found_num + 1))
    if x - 1 >= 0 and instructions_raw[next_left[0]][next_left[1]] == (found_num + 1):
        results.extend(traverse(next_left[0], next_left[1], found_num + 1))
    if x + 1 <= (len(instructions_raw[0]) - 1) and instructions_raw[next_right[0]][
        next_right[1]
    ] == (found_num + 1):
        results.extend(traverse(next_right[0], next_right[1], found_num + 1))
    return results


total = 0
for i, x in enumerate(instructions_raw):
    for j, y in enumerate(x):
        if y == 0:
            res = traverse(i, j, y)
            new_set = set()
            for x in res:
                new_set.add((x[0], x[1]))
            total += len(new_set)
print(total)


# Part 2
total = []
for i, x in enumerate(instructions_raw):
    for j, y in enumerate(x):
        if y == 0:
            total += traverse(i, j, y)
print(len(total))
