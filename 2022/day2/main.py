with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

total = 0
for instruction in instructions_raw:
    inst = instruction.split(' ')
    them = inst[0]
    me = inst[1]
    me = chr(ord(me) - 23)
    result = 0
    if them == me:
        result = 3
    else:
        test = (ord(them) - ord(me)) % 3
        if test == 1:
            result = 0
        else:
            result = 6
    total += result
    total += ord(me) - 64
print(total)
# part 2
total = 0
for instruction in instructions_raw:
    inst = instruction.split(' ')
    print(inst)
    them = inst[0]
    them = ord(them) - 65
    desired = inst[1]
    result = 0
    # x lose y draw z win
    match desired:
        case 'X':
            shape = (them + 2) % 3
            result = 0
        case 'Y':
            shape = (them) % 3
            result = 3
        case 'Z':
            shape = (them + 1) % 3
            result = 6
    print(shape)
    total += result
    total += (shape + 1)
print(total)