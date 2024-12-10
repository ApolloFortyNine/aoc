import copy

with open("input.txt") as file:
    instructions_raw = file.read()

instructions = instructions_raw.split("\n")[0]

raw_drive = []

file_count = 0
free_space = False
for x in instructions:
    num = int(x)
    if not free_space:
        raw_drive.extend(list([str(file_count)] * num))
        # print(file_count)
        file_count += 1
    else:
        raw_drive.extend(list("." * num))
    free_space = not free_space
# print(raw_drive)


def get_next_loc(instructions):
    length = len(instructions) - 1
    for i, x in enumerate(instructions[::-1]):
        if x != ".":
            yield length - i


raw_drive_2 = copy.deepcopy(raw_drive)
next_loc = get_next_loc(raw_drive)
for i, x in enumerate(raw_drive):
    if x != ".":
        continue
    else:
        try:
            item = next(next_loc)
            if item <= i:
                print(raw_drive[i])
                print(raw_drive[i - 1])
                break
            raw_drive[i], raw_drive[item] = raw_drive[item], raw_drive[i]
        except StopIteration:
            break
total = 0
for i, x in enumerate(raw_drive):
    if x == ".":
        continue
    total += i * int(x)
print(total)

# Part 2
