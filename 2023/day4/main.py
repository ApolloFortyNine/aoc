with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    
total = 0
for x in instructions_raw:
    split = x.split(': ')
    split_2 = split[1].split(' | ')
    card = split[0]
    winning_nums = split_2[0]
    picked_nums = split_2[1]
    winning_nums = winning_nums.split()
    picked_nums = picked_nums.split()
    winning_nums = [int(i) for i in winning_nums]
    picked_nums = [int(i) for i in picked_nums]
    winning_nums = set(winning_nums)
    picked_nums = set(picked_nums)
    new_set = winning_nums & picked_nums
    result = 0
    if len(new_set) == 1:
        result = 1
    elif len(new_set) > 1:
        result = 2 ** (len(new_set) - 1 )
    total += result
print(total)
# Part 2

dp = [1] * len(instructions_raw)
for i, x in enumerate(instructions_raw):
    split = x.split(': ')
    split_2 = split[1].split(' | ')
    card = split[0]
    winning_nums = split_2[0]
    picked_nums = split_2[1]
    winning_nums = winning_nums.split()
    picked_nums = picked_nums.split()
    winning_nums = [int(i) for i in winning_nums]
    picked_nums = [int(i) for i in picked_nums]
    winning_nums = set(winning_nums)
    picked_nums = set(picked_nums)
    new_set = winning_nums & picked_nums
    for x in range(len(new_set)):
        dp[i+x+1] += (1 * dp[i])
print(sum(dp))
print(dp)