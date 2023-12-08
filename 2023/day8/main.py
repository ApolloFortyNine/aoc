with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

directions = instructions_raw[0]

nodes = {}
steps = 0

for x in instructions_raw[2:]:
    split = x.split(' = ')
    node = split[0]
    split = split[1][1:-1]
    split = split.split(', ')
    left = split[0]
    right = split[1]
    nodes[node] = [left,right]

current_node = 'AAA'
while True:
    instruct = directions[steps % len(directions)]
    combo = nodes[current_node]
    steps += 1
    if instruct == 'L':
        current_node = combo[0]
    elif instruct == 'R':
        current_node = combo[1]
    elif nodes[current_node][0] == current_node:
        print('reset')
        current_node = 'AAA'
    else:
        print('panic')
        break
    if current_node == 'ZZZ':
        print(steps)
        break