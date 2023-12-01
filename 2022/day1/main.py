with open("input.txt") as file:
    instructions_raw = file.read().split('\n\n')
print(instructions_raw)

elf_arr = []
runner = 0
big_elf = 0
for x in instructions_raw:
    elf = x.split('\n')
    elf = sum([int(y) if y else 0 for y in elf])
    elf_arr.append(elf)
    big_elf = max(elf, big_elf)
print(big_elf)
elf_arr.sort()
print(sum(elf_arr[-3:]))
    