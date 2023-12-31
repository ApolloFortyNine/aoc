from collections import deque
from tqdm import tqdm
from multiprocessing import Pool




# Part 2



def process_seed(seed, order, maps):
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
    return current_val

# for seed in tqdm(longer_seeds, ascii=True):
#     arr.append(process_seed(seed))

def process_seed_range(pair, order, maps):
    print(pair)
    lowest = 10000000000
    for i in range(pair[1]):
            lowest = min(process_seed(pair[0] + i, order, maps), lowest)
    print('done')
    return lowest

def main():
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
    lowest = 100000000000
    longer_seeds = set()
    args = []
    for i in tqdm(range(0, len(seeds), 2), ascii=True):
        pair = seeds[i:i+2]
        args.append((pair, order, maps))

    with Pool(12) as pool:
        for result in pool.starmap(process_seed_range, args):
            lowest = min(lowest, result)

        lowest = min(process_seed_range(pair, order, maps), lowest)
    
    print(lowest)
if __name__ == '__main__':
    main()