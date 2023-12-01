with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    
first = None
last = None
arr = []

for x in instructions_raw:
    for y in x:
        if ord(y) < 63:
            first = y
            break
    for y in x[::-1]:
        if ord(y) < 63:
            last = y
            break
    arr.append(int(first + last))
print(sum(arr))

# Part 2
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
arr = []
for x in instructions_raw:
    if x == 'four863mrrnrsxrkone':
        pass
    for i, y in enumerate(x):
        if y.isdigit():
            first = [i, y]
            break
    for i, y in enumerate(numbers):
        index = x.find(y)
        if index == -1:
            continue
        if index < first[0]:
            first = [index, str(i+1)]
    rev_x = x[::-1]
    for i, y in enumerate(rev_x):
        if y.isdigit():
            last = [i, y]
            break
    for i, y in enumerate(numbers):
        index = x.find(y)
        if index == -1:
            continue
        index = len(x) - index
        if index < last[0]:
            last = [index, str(i+1)]
    arr.append(int(first[1]+last[1]))
# print(arr)
print(sum(arr))
# attempt 2
arr = []
for x in instructions_raw:
    x = x.replace('eighthree', 'eightthree')
    x = x.replace('sevenine', 'sevennine')
    x = x.replace('twone', 'twoone')
    x = x.replace('nineight', 'nineeight')
    x = x.replace('oneight', 'oneeight')
    x = x.replace('fiveight', 'fiveeight')
    for i, y in enumerate(numbers):
        x = x.replace(y, str(i + 1))
    for i, y in enumerate(x):
        if y.isdigit():
            first = [i, y]
            break
    rev_x = x[::-1]
    for i, y in enumerate(rev_x):
        if y.isdigit():
            last = [i, y]
            break
    arr.append(int(first[1]+last[1]))
print(sum(arr))

# Attempt 3
arr = []
for x in instructions_raw:
    if x == 'four863mrrnrsxrkone':
        pass
    nums = []
    for i, y in enumerate(x):
        if y.isdigit():
            nums.append(y)
        else:
            nums.append('x')
    for z in range(len(x)):
        for i, y in enumerate(numbers):
            index = x[z:].find(y)
            if index == -1:
                continue
            index = index + z
            nums[index] = str(i + 1)
    for y in nums:
        if(y.isdigit()):
            first = y
            break
    for y in nums[::-1]:
        if(y.isdigit()):
            last = y
            break
    arr.append(int(first+last))
print(sum(arr))