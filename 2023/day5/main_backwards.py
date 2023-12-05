from collections import deque
from tqdm import tqdm
import multiprocessing

with open("input.txt.test") as file:
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
def main():
    maps = [[], [], [], [], [], [], []]
    order = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    current_map = -1
    for x in instructions_raw[1:]:
        if x.find('-to-') != -1:
            second = x.split('-to-')
            third = second[1].split()
            current_map +=1
            maps[current_map] = []
        else:
            if not x:
                continue
            instruct = x.split()
            instruct = list(map(lambda x: int(x), instruct))
            maps[current_map].append(instruct)
    def process_seed(seed):
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
    # Backwards?
    my_set = set()
    lowest = 1000000
    for i in tqdm(range(0, len(seeds), 2), ascii=True):
        pair = seeds[i:i+2]
        for i in range(pair[1]):
            my_set.add(pair[0] + i)
    arr = []
    for x in maps[-1]:
        for y in range(x[2]):
            arr.append(x[0] + y)
    
    new_maps = maps[:len(maps) - 1]
    arr = sorted(arr)
    for k in arr:
        if k == 46:
            pass
        current_val = k
        for x in new_maps[::-1]:
            for y in x:
                for z in range(y[1],y[1] + y[2]):
                    if (current_val < (x[1] + x[2])) and (current_val >= x[1]):
                        # Do the map
                        diff = x[1] - x[0]
                        current_val = current_val - diff
                        break
        if current_val in my_set:
            print(k)
        # print(current_val)



main()

