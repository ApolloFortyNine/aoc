from collections import deque
from tqdm import tqdm
from multiprocessing import Pool


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
longer_seeds = deque()
for i in tqdm(range(0, len(seeds), 2), ascii=True):
    pair = seeds[i:i+2]
    for i in range(pair[1]):
        longer_seeds.append(pair[0]+i)


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
    return current_val

# for seed in tqdm(longer_seeds, ascii=True):
#     arr.append(process_seed(seed))

def backwards():
    pass

def main():
    num_processes = 8
    lowest = 100000000000
    chunk_size = 1000  # Adjust based on your dataset size and memory constraints

    with Pool(num_processes) as pool:
        for result in tqdm(pool.imap(process_seed, longer_seeds, chunksize=chunk_size), total=len(longer_seeds)):
            lowest = min(lowest, result)
    
    print(lowest)
if __name__ == '__main__':
    main()
