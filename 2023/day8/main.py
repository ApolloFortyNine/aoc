import copy
import math
with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

directions = instructions_raw[0]

# nodes = {}
# steps = 0

# for x in instructions_raw[2:]:
#     split = x.split(' = ')
#     node = split[0]
#     split = split[1][1:-1]
#     split = split.split(', ')
#     left = split[0]
#     right = split[1]
#     nodes[node] = [left,right]

# current_node = 'AAA'
# while True:
#     instruct = directions[steps % len(directions)]
#     combo = nodes[current_node]
#     steps += 1
#     if instruct == 'L':
#         current_node = combo[0]
#     elif instruct == 'R':
#         current_node = combo[1]
#     elif nodes[current_node][0] == current_node:
#         print('reset')
#         current_node = 'AAA'
#     else:
#         print('panic')
#         break
#     if current_node == 'ZZZ':
#         print(steps)
#         break
# part 2
nodes = {}
steps = 0
nodes_end_with_a = []
for x in instructions_raw[2:]:
    split = x.split(' = ')
    node = split[0]
    split = split[1][1:-1]
    split = split.split(', ')
    left = split[0]
    right = split[1]
    nodes[node] = [left,right]
    if node[-1] == 'A':
        nodes_end_with_a.append(node)

# current_node = 'AAA'
# current_nodes = copy.deepcopy(nodes_end_with_a)
# while True:
#     if steps % 1000 == 0:
#         pass
#     instruct = directions[steps % len(directions)]
#     all_end_z = True
#     next_nodes = []
#     reset = False
#     steps += 1
#     for x in current_nodes:
#         combo = nodes[x]
#         if instruct == 'L':
#             next_nodes.append(combo[0])
#             if combo[0][-1] != 'Z':
#                 all_end_z = False
#         elif instruct == 'R':
#             next_nodes.append(combo[1])
#             if combo[1][-1] != 'Z':
#                 all_end_z = False
#         elif nodes[x][0] == x:
#             print('reset')
#             reset = True
#         else:
#             print('panic')
#             break
#     if all_end_z:
#         print(steps)
#         break
#     elif reset:
#         current_nodes = copy.deepcopy(nodes_end_with_a)
#     else:
#         current_nodes = next_nodes
    # Might need to move this

how_many_steps = []
for current_node in nodes_end_with_a:
    steps = 0
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
        if current_node[-1] == 'Z':
            how_many_steps.append(steps)
            break
print(how_many_steps)
print(math.lcm(*how_many_steps))