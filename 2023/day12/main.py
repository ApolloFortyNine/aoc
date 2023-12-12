from functools import cache

with open("input.txt.test") as file:
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

possible = 0
for instruct in instructions_raw:
    print(instruct)
    splits = instruct.split(" ")
    string = "?".join([splits[0]] * 5)
    wanted_groups = splits[1].split(',')
    wanted_groups = list(map(lambda x: int(x), wanted_groups)) * 5
    half = len(string) // 2
    permutations = generate_permutations(string[:half], max_springs=sum(wanted_groups))
    p2 = generate_permutations(string[half:], max_springs=sum(wanted_groups))
    possible1 = 0
    possible2 = 0
    for x in permutations:
        found_groups = count_groups(x)
        if found_groups == wanted_groups:
            possible1 += 1
    for x in p2:
        found_groups = count_groups(x)
        if found_groups == wanted_groups:
            possible2 += 1
    possible += possible1 * possible2
print(possible)