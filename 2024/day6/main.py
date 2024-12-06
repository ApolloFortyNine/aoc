import copy

with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

start_index = [0, 0]
for i, x in enumerate(instructions_raw):
    for j, char in enumerate(x):
        if char == "^":
            start_index = [i, j]
print(start_index)
instructions_raw = [list(x) for x in instructions_raw]
insts = copy.deepcopy(instructions_raw)
print(instructions_raw[start_index[0]][start_index[1]])
current_dir = "up"
current_loc = start_index
seen_locs = set()
seen_locs.add(f"{current_loc[0]},{current_loc[1]}")


def get_next_dir(dir):
    if dir == "up":
        return "right"
    if dir == "right":
        return "down"
    if dir == "down":
        return "left"
    if dir == "left":
        return "up"


while True:
    next_pos = [0, 0]
    if current_dir == "up":
        next_pos = [current_loc[0] - 1, current_loc[1]]
    if current_dir == "down":
        next_pos = [current_loc[0] + 1, current_loc[1]]
    if current_dir == "right":
        next_pos = [current_loc[0], current_loc[1] + 1]
    if current_dir == "left":
        next_pos = [current_loc[0], current_loc[1] - 1]
    if next_pos[0] > (len(instructions_raw) - 1) or next_pos[0] < 0:
        break
    if next_pos[1] > (len(instructions_raw[0]) - 1) or next_pos[1] < 0:
        break
    if instructions_raw[next_pos[0]][next_pos[1]] == "#":
        current_dir = get_next_dir(current_dir)
    else:
        current_loc = next_pos
        seen_locs.add(f"{current_loc[0]},{current_loc[1]}")
        # print(next_pos)
        instructions_raw[next_pos[0]][next_pos[1]] = "X"
#   print(current_dir)
#   print(next_pos)
print(len(seen_locs))
# for x in instructions_raw:
#   print(x)

## PART 2


def is_loop(target_pos):
    looped = False
    count = 0
    current_dir = 'up'
    current_loc = start_index
    local_list = copy.deepcopy(insts)
    local_list[target_pos[0]][target_pos[1]] = '#'
    # for x in local_list:
    #     print(x)
    while True:
        next_pos = [0, 0]
        if current_dir == "up":
            next_pos = [current_loc[0] - 1, current_loc[1]]
        if current_dir == "down":
            next_pos = [current_loc[0] + 1, current_loc[1]]
        if current_dir == "right":
            next_pos = [current_loc[0], current_loc[1] + 1]
        if current_dir == "left":
            next_pos = [current_loc[0], current_loc[1] - 1]
        if next_pos[0] > (len(local_list) - 1) or next_pos[0] < 0:
            break
        if next_pos[1] > (len(local_list[0]) - 1) or next_pos[1] < 0:
            break
        if local_list[next_pos[0]][next_pos[1]] == "#":
            current_dir = get_next_dir(current_dir)
        else:
            current_loc = next_pos
            # seen_locs.add(f"{current_loc[0]},{current_loc[1]}")
            # print(next_pos)
            count += 1
            if count > 20000:
                return True
        if count > 20000:
            return True
    return False
current_loc = start_index
# print(is_loop(start_index))
pots = []
for x in seen_locs:
    i, j = x.split(',')
    pots.append([int(i), int(j)])
# print(pots)
# print(instructions_raw[pots[0][0]][pots[0][1]])
for x in insts:
    print(x)
print("-----")
total = 0
# pots =[[5,4]]
for x in pots:
    # print(x)
    if is_loop(x):
        total += 1
print(total)