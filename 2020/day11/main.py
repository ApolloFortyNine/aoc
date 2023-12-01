import copy

with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

grid = [ [] for _ in range(len(instructions_raw))]
for i, x in enumerate(instructions_raw):
    for y in x:
        grid[i].append(y)

stop = False
def is_occupied(x, y, new_grid):
    global stop
    if x < 0 or y < 0:
        stop = True
        return False
    try:
        if (new_grid[x][y] == 'L'):
            stop = True
            return False
        if (new_grid[x][y] == '.'):
            stop = False
            return False
        if new_grid[x][y] == '#':
            stop = True
            return True
        print("WOOOOOAH")

    except:
        stop = True
        return False
    
def is_occupied2(x, y, new_grid):
    try:
        if x < 0 or y < 0:
            return False
        if new_grid[x][y] == 'L':
            return False
        elif new_grid[x][y] == '#':
            return True
    except:
        return False
    

def how_many_surrounding(x, y, new_grid):
    arr = []
    global stop
    for i in reversed(range(x)):
        if is_occupied(i, y, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for i in range(x+1,len(new_grid[0])+100):
        if is_occupied(i, y, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for j in range(y + 1,len(new_grid)+100):
        if is_occupied(x, j, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for j in reversed(range(y)):
        if is_occupied(x, j, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for z in range(1,100):
        if is_occupied(x - z, y - z, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for z in range(1, 100):
        if is_occupied(x - z, y + z, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for z in range(1, 100):
        if is_occupied(x + z, y - z, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    for z in range(1, 100):
        if is_occupied(x + z, y + z, new_grid):
            arr.append(True)
            break
        if stop:
            stop = False
            break
    # print(arr)
    the_count = arr.count(True)
    return the_count

def process_grid(grid):
    new_grid2 = copy.deepcopy(grid)
    new_grid = copy.deepcopy(grid)  
    for x in range(len(new_grid)):
        for y in range(len(new_grid[0])):
            surrounding = how_many_surrounding(x, y, new_grid)
            if new_grid[x][y] == 'L':
                if surrounding == 0:
                    # print("test1")
                    new_grid2[x][y] = '#'
            elif new_grid[x][y] == '#':
                if surrounding >= 5:
                    # print("test2")
                    new_grid2[x][y] = 'L'
    return new_grid2
def print_grid(grid):
    for x in grid:
        line = ""
        for y in x:
            line += y
        print(line)

count = 0
grid_copy = copy.deepcopy(grid)
while True:
    newer_grid = process_grid(grid_copy)
    # print_grid(new_grid)
    # break
    if newer_grid == grid_copy:
        print_grid(newer_grid)
        print("done")
        print(count)
        occupied = 0
        for x in newer_grid:
            for y in x:
                if y == '#':
                    occupied += 1
        print(occupied)
        break
    if count > 500:
        occupied = 0
        for x in newer_grid:
            for y in x:
                if y == '#':
                    occupied += 1
        print(occupied)
        print_grid(newer_grid)
        break
    else:
        grid_copy = copy.deepcopy(newer_grid)
        print(count)
        # print_grid(grid_copy)
        count += 1