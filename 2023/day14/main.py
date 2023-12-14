import numpy as np
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
test = np.rot90(arr)
x = test[0]
I = np.where(x == '#')
# print(np.split(x, I[0]))

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

print(move_north(arr))