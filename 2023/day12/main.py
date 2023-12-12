from functools import cache
import time

with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    
@cache
def generate_permutations(s, index=0, max_springs=100):
    if index == len(s):
        if s.count('#') > max_springs:
            return []
        else:
            return [s]
    
    permutations = []
    if s[index] == '?':
        permutations.extend(generate_permutations(s[:index] + '#' + s[index + 1:], index + 1))
        permutations.extend(generate_permutations(s[:index] + '.' + s[index + 1:], index + 1))
    else:
        permutations.extend(generate_permutations(s, index + 1))

    return permutations

def count_groups(x):
    groups = []
    for y in x.split("."):
        num = y.count("#")
        if num > 0:
            groups.append(num)
    return groups

possible = 0
for instruct in instructions_raw:
    splits = instruct.split(" ")
    string = splits[0]
    wanted_groups = splits[1].split(',')
    wanted_groups = list(map(lambda x: int(x), wanted_groups))
    permutations = generate_permutations(string)
    for x in permutations:
        found_groups = count_groups(x)
        if found_groups == wanted_groups:
            possible += 1
print(possible)

@cache
def recurse(string, groups):
    if (not string or string == '.') and not groups:
        return 1
    if not string:
        return 0
    elif string[0] == '.':
        return recurse(string[1:], groups)
    elif string[0] == '?':
        return recurse(string.replace('?', '.', 1), groups) + recurse(string.replace('?', '#', 1), groups)
    elif string[0] == '#':
        if not groups:
            return 0
        if '.' not in string[:groups[0]] and string[groups[0]] != '#':
            return recurse(string[groups[0] + 1:], groups[1:])
        else:
            return 0

possible = 0
start = time.time()
for instruct in instructions_raw:
    # print(instruct)
    splits = instruct.split(" ")
    string = "?".join([splits[0]] * 5)
    string += '.'
    wanted_groups = splits[1].split(',')
    wanted_groups = tuple(map(lambda x: int(x), wanted_groups * 5))
    result = recurse(string, wanted_groups)
    # print(result)
    possible += result
print(f"{(time.time() - start) * 1000} ms")
print(possible)