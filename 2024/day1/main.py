with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

left = []
right = []
for x in instructions_raw:
    left_x, right_x = x.split()
    left.append(int(left_x))
    right.append(int(right_x))

left.sort()
right.sort()

total = 0
for x in zip(left, right):
    total += abs (x[0] - x[1])
print(total)

# part 2
count_dict = {}
for x in right:
    count_dict[x] = count_dict.get(x, 0) + 1

total_2 = 0
for x in left:
    res = count_dict.get(x, 0)
    total_2 += (x * res)
print(total_2)