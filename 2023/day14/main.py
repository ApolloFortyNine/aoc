import numpy as np
from tqdm import tqdm
with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    
# Split each column by #, then move all Os inside each to top
mine = [list(x) for x in instructions_raw]
arr = np.array(mine)
# print(arr[:, 0])
# print(arr[0, :])
cube_rocks = np.where(arr[:, 2] == '#')
# print(cube_rocks)
# print(np.split(arr[:, 2], cube_rocks[0]))
test = np.rot90(arr, -1)
#test = np.rot90(test, -1)
print(test)
x = test[0]
I = np.where(x == '#')
# print(np.split(x, I[0]))
# exit()
def move_north(arr):
    order = {'#': 0, 'O': 1, '.': 2}
    total = 0
    for col in range(arr.shape[1]):
        current_col = arr[:,col]
        cube_rocks = np.where(current_col == '#')
        split_on_rocks = np.split(current_col, cube_rocks[0])
        new_col = []
        for split in split_on_rocks:
            sorted_split = np.array(sorted(split, key=lambda x: order[x]))
            new_col.extend(sorted_split)
            # print(sorted_split)
        new_col_np = np.array(new_col)
        round_rock_indicies = np.where(new_col_np == 'O')
        #print(round_rock_indicies)
        rock_total =  sum([len(new_col_np) - x for x in round_rock_indicies[0]])
        total += rock_total
        #print(split_on_rocks)
    return total

last_total = 0
results = {}
def move_up(arr):
    order = {'#': 0, 'O': 1, '.': 2}
    total = 0
    new_cols = []
    for col in range(arr.shape[1]):
        current_col = arr[:,col]
        cube_rocks = np.where(current_col == '#')
        split_on_rocks = np.split(current_col, cube_rocks[0])
        new_col = []
        for split in split_on_rocks:
            length = len(split)
            if len(split) == 0:
                continue
            if split[0] == '#':
                length -= 1
                new_col.append('#')
            rounds = np.where(split == 'O')
            num_periods = length - len(rounds[0])
            new_col.extend(['O'] * len(rounds[0]))
            new_col.extend(['.'] * num_periods)
            # sorted_split = np.array(sorted(split, key=lambda x: order[x]))
            # new_col.extend(sorted_split)
            # print(sorted_split)
        new_col_np = np.array(new_col)
        round_rock_indicies = np.where(new_col_np == 'O')
        #print(round_rock_indicies)
        rock_total =  sum([len(new_col_np) - x for x in round_rock_indicies[0]])
        total += rock_total
        new_cols.append(new_col_np)
        #print(split_on_rocks)
    # results[total] = results.get(total, 0) + 1
    return np.column_stack(new_cols)

def cycle(arr):
    northed = move_up(arr)
    rotated = np.rot90(northed, -1)
    wested = move_up(rotated)
    rotated = np.rot90(wested, -1)
    southed = move_up(rotated)
    rotated = np.rot90(southed, -1)
    easted = move_up(rotated)
    rotated = np.rot90(easted, -1)
    return rotated

def count(arr):
    total = 0
    for col in range(arr.shape[1]):
        current_col = arr[:, col]
        round_rock_indicies = np.where(current_col == 'O')
        rock_total =  sum([len(current_col) - x for x in round_rock_indicies[0]])
        total += rock_total
    return total


new_arr = arr
# for x in tqdm(range(1000000000)):
cycles = 1000000000
results_arr = []
req = 0
for i, x in enumerate(range(1000)):
    new_arr = cycle(new_arr)
    new_arr_bytes = new_arr.tobytes()
    the_count = count(new_arr)
    results_arr.append(int(the_count))
    if new_arr_bytes in results:
        loop_size = i - results[new_arr_bytes]
        print(loop_size)
        print(results[new_arr_bytes])
        req =(cycles - (results[new_arr_bytes] + 1)) % loop_size
        print(req)
        break
    else:
        results[new_arr_bytes] = i
for x in range(req):
    new_arr = cycle(new_arr)
    the_count = count(new_arr)
    results_arr.append(int(the_count))
print(count(new_arr))
# print(results_arr)
# print(results)
# print(move_north(arr))
# test = move_up(arr)