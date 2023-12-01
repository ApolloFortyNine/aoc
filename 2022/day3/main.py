with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

total = 0
# Oh can have dupes on each side but can't have 1 in first half that's in other half
for x in instructions_raw:
    all_chars = set()
    for y in x[:int(len(x)/2) + 1]:
        all_chars.add(y)
    for y in x:
        if y in all_chars:
            if y.islower():
                val = ord(y) - 96
            else:
                val = ord(y) - 38
            total += val
print(total)
