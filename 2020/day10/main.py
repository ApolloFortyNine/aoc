with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
chargers = []
for x in instructions_raw:
    chargers.append(int(x))
chargers.append(0)
chargers.append(max(chargers) + 3)
chargers.sort()
print(chargers)

diff = {}
for i, x in enumerate(chargers):
    next_i = True if (i + 1) < len(chargers) else False
    if next_i:
        diff_val = chargers[i+1] - x
        diff[diff_val] = diff.get(diff_val, 0) + 1
print(diff)

# Part 2
# Whenever multiple choices, save number of choices to array, then multiply them all together?

dp = [0] * len(chargers)
dp[0] = 1

for i in range(1, len(chargers)):
    for j in range(i):
        if (chargers[i] - chargers[j]) <= 3:
            dp[i] += dp[j]
print(dp[-1])