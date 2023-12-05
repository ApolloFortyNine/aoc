from collections import deque
from tqdm import tqdm
from numba import jit

with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    
first = instructions_raw[0].split(": ")
seeds = first[1].split()
seeds = list(map(lambda x: int(x), seeds))
print(seeds)

maps = {}
order = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
current_map = ''
for x in instructions_raw[1:]:
    if x.find('-to-') != -1:
        second = x.split('-to-')
        third = second[1].split()
        current_map = third[0]
        print(current_map)
        maps[current_map] = []
    else:
        if not x:
            continue
        instruct = x.split()
        instruct = list(map(lambda x: int(x), instruct))
        maps[current_map].append(instruct)

arr = []
for seed in seeds:
    current_val = seed
    for item in order:
        for x in maps[item]:
            if (current_val < (x[1] + x[2])) and (current_val >= x[1]):
                # Do the map
                diff = x[1] - x[0]
                current_val = current_val - diff
                break
        else:
            pass
    arr.append(current_val)
print(min(arr))

# Part 2
@jit
def process_seed(seed):
    current_val = seed
    for item in order:
        for x in maps[item]:
            if (current_val < (x[1] + x[2])) and (current_val >= x[1]):
                # Do the map
                diff = x[1] - x[0]
                current_val = current_val - diff
                break
        else:
            pass

lowest = 1000000
for i in tqdm(range(0, len(seeds), 2), ascii=True):
    pair = seeds[i:i+2]
    for i in range(pair[1]):
        lowest = min(lowest,process_seed(seed))
    print("hello")





print(lowest)

