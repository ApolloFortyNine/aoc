with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    


instructions = {}
for i, x in enumerate(instructions_raw):
    instructions[i] = x
print(instructions)

acc = 0
instructions_ran = []

# While true instead
pc = 0
def parse_num(arg):
    if (arg[0]=='+'):
        return int(arg[1:])
    else:
        return -1 * int(arg[1:])

while True:
    instruction = instructions.get(pc, None)
    # print(instruction)
    # print(acc)
    # print(pc)
    if pc not in instructions_ran:
        instructions_ran.append(pc)
    else:
        print(acc)
        break
    inst, arg = instruction.split(' ')
    match inst:
        case 'acc':
            acc += parse_num(arg)
            pc += 1
        case 'jmp':
            next_pc_offset = parse_num(arg)
            pc += next_pc_offset
        case 'nop':
            pc += 1

def part2(instructions):
    pc = 0
    run_count = 0
    acc = 0
    while True:
        instruction = instructions.get(pc, None)
        run_count += 1
        # print(instruction)
        # print(acc)
        # print(pc)
        if not instruction:
            print("reached end")
            print(acc)
            break
        if run_count > 10000:
            break
        inst, arg = instruction.split(' ')
        match inst:
            case 'acc':
                acc += parse_num(arg)
                pc += 1
            case 'jmp':
                next_pc_offset = parse_num(arg)
                pc += next_pc_offset
            case 'nop':
                pc += 1

for key, value in instructions.items():
    inst, arg = value.split(' ')
    run_it = False
    if inst == 'nop':
        inst = 'jmp'
        run_it = True
    elif inst == 'jmp':
        inst = 'nop'
        run_it = True
    if run_it:
        new_dict = instructions.copy()
        new_dict[key] = f"{inst} {arg}"
        part2(new_dict)
    