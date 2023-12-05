from collections import deque
from tqdm import tqdm
from multiprocessing import Pool,Manager, Value
from itertools import islice

lowest = Value("i", 100000000000)  # Shared memory for tracking the lowest value
def process_seed(seed, maps, order):
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
def worker(seed, maps, order):
    global lowest
    result = process_seed(seed, maps, order)
    with lowest.get_lock():  # Ensure thread safety while updating the lowest value
        lowest.value = min(lowest.value, result)
def main():
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


    # for seed in tqdm(longer_seeds, ascii=True):
    #     arr.append(process_seed(seed))

    def backwards():
        pass

    longer_seeds = deque()
    for i in tqdm(range(0, len(seeds), 2), ascii=True):
        pair = seeds[i:i+2]
        for i in range(pair[1]):
            longer_seeds.append(pair[0]+i)



    num_processes = 8



    # Splitting longer_seeds into smaller chunks to manage memory usage
    chunk_size = 1  # Adjust this based on your system's capabilities
    chunks = [list(islice(longer_seeds, i, i + chunk_size)) for i in range(0, len(longer_seeds), chunk_size)]

    with Pool(num_processes) as pool:
        for chunk in tqdm(chunks, ascii=True):
            # Using starmap to pass the shared 'lowest' object to each worker
            pool.starmap(worker, [(seed, maps, order) for seed in chunk])

    print(lowest.value)
    
if __name__ == '__main__':
    main()
