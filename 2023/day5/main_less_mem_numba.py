from collections import deque
from tqdm import tqdm
from multiprocessing import Pool
from numba import njit
import numpy as np

with open("input.txt.test") as file:
    instructions_raw = file.read().splitlines()
    
first = instructions_raw[0].split(": ")
seeds = first[1].split()
seeds = list(map(lambda x: int(x), seeds))
print(seeds)

maps = [[], [], [], [], [], [], []]
order = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
current_map = -1
for x in instructions_raw[1:]:
    if x.find('-to-') != -1:
        second = x.split('-to-')
        third = second[1].split()
        current_map += 1
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
    for y in maps:
        for x in y:
            if (current_val < (x[1] + x[2])) and (current_val >= x[1]):
                # Do the map
                diff = x[1] - x[0]
                current_val = current_val - diff
                break
    arr.append(current_val)
print(min(arr))

# Part 2


@njit
def process_seed(seed, maps):
    current_val = seed
    for y in maps:
        for x in y:
            if (current_val < (x[1] + x[2])) and (current_val >= x[1]):
                # Do the map
                diff = x[1] - x[0]
                current_val = current_val - diff
                break
        else:
            pass
    return current_val

# for seed in tqdm(longer_seeds, ascii=True):
#     arr.append(process_seed(seed))

def backwards():
    pass

def main():
    lowest = 1000
    longer_seeds = set()
    for i in tqdm(range(0, len(seeds), 2), ascii=True):
        pair = seeds[i:i+2]
        for i in range(pair[1]):
            lowest = min(process_seed(pair[0] + i, maps), lowest)
    
    print(lowest)
main()
