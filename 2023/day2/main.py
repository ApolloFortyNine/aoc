import re

with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    

max_red = 12
max_green = 13
max_blue = 14
not_too_big = set()
for x in instructions_raw:
    p = re.compile(r'Game (\d+):')
    result = p.findall(x)
    game_id = result[0]
    games = x.split(';')
    flag = True
    for y in games:
        p = re.compile(r'(\d+)\s+(\w+)')
        result = p.findall(y)
        for z in result:
            current_color_max = eval('max_'+z[1])
            if int(z[0]) > int(current_color_max):
                flag = False
    if flag:
        if int(game_id) not in not_too_big:
            not_too_big.add(int(game_id))
print(sum(not_too_big))

# Part 2
arr = []
for x in instructions_raw:
    max_color = {'red': 0, 'blue': 0, 'green': 0}
    p = re.compile(r'Game (\d+):')
    result = p.findall(x)
    game_id = result[0]
    games = x.split(';')
    flag = True
    for y in games:
        p = re.compile(r'(\d+)\s+(\w+)')
        result = p.findall(y)
        for z in result:
            if int(z[0]) > max_color[z[1]]:
                max_color[z[1]] = int(z[0])
    arr.append(max_color['red'] * max_color['blue'] * max_color['green'])
print(sum(arr))