with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

raw_hashes = instructions_raw[0].split(',')

all_hashes = []
for raw_hash in raw_hashes:
    total = 0
    for char in raw_hash:
        total += ord(char)
        total *= 17
        total %= 256
    all_hashes.append(total)
print(sum(all_hashes))

def get_hash(label):
    total = 0
    for char in label:
        total += ord(char)
        total *= 17
        total %= 256
    return total
# Part 2 Hashmap of hashmaps, order is guaranteed
boxes = {x:{} for x in range(256)}
for instruct in raw_hashes:
    label = ''
    focal_length = None
    if instruct.find('=') != -1:
        split = instruct.split('=')
        label = split[0]
        focal_length = split[1]
        label_hash = get_hash(label)
        if label in boxes[label_hash]:
            boxes[label_hash][label] = int(focal_length)
        else:
            boxes[label_hash][label] = int(focal_length)
    else:
        split = instruct.split('-')
        label = split[0]
        label_hash = get_hash(label)
        boxes[label_hash].pop(label, None)


total = 0
for key, value in boxes.items():
    i = 1
    for x, y in value.items():
        total += ((key+1) * i * y)
        i += 1
print(total)
